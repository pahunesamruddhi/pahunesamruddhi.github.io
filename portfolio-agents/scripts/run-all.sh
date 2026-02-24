#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# Portfolio Builder — Master Orchestrator
# Runs 5 specialised Claude agents in sequence
# Each agent reads previous outputs before writing its own
# ═══════════════════════════════════════════════════════════════

set -e  # Exit on any error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
OUTPUTS_DIR="$PROJECT_DIR/outputs"

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

log() { echo -e "${CYAN}[$(date +%H:%M:%S)]${NC} $1"; }
success() { echo -e "${GREEN}✓${NC} $1"; }
warn() { echo -e "${YELLOW}⚠${NC} $1"; }
error() { echo -e "${RED}✗${NC} $1"; exit 1; }
header() { echo -e "\n${BOLD}${BLUE}═══ $1 ═══${NC}\n"; }

# ───────────────────────────────────────────────────────────────
# Pre-flight checks
# ───────────────────────────────────────────────────────────────

header "Pre-flight Checks"

# Check claude CLI is available
if ! command -v claude &> /dev/null; then
    error "Claude CLI not found. Install with: npm install -g @anthropic-ai/claude-code"
fi
success "Claude CLI found"

# Check source files exist
REQUIRED_SOURCES=(
    "$PROJECT_DIR/source/cs1-presentation.md"
    "$PROJECT_DIR/source/cs2-storytelling.md"
)

for f in "${REQUIRED_SOURCES[@]}"; do
    if [ ! -f "$f" ]; then
        error "Required source file missing: $f\nRun: bash scripts/setup-sources.sh first"
    fi
done
success "Source files present"

# Create outputs dir
mkdir -p "$OUTPUTS_DIR"
success "Outputs directory ready"

# ───────────────────────────────────────────────────────────────
# Agent runner function
# ───────────────────────────────────────────────────────────────

run_agent() {
    local agent_num="$1"
    local agent_name="$2"
    local agent_file="$PROJECT_DIR/agents/0${agent_num}-${agent_name}.md"
    local output_file="$3"
    local description="$4"

    header "Agent ${agent_num}: ${agent_name^}"
    log "Running: $description"
    log "Agent prompt: $agent_file"
    log "Output: $output_file"

    if [ ! -f "$agent_file" ]; then
        error "Agent file not found: $agent_file"
    fi

    # Build the prompt by combining the agent instruction + all context
    PROMPT=$(cat << EOF
You are running as a specialised agent in a multi-agent portfolio building system.

Your agent instructions are in the file below. Read them completely, then execute your job.

$(cat "$agent_file")

---

IMPORTANT: When your instructions say to write to a file path like "../outputs/filename.md",
write that content clearly marked with:

=== OUTPUT FILE: outputs/filename.md ===
[content here]
=== END OUTPUT ===

This allows the orchestrator to extract and save your output correctly.
EOF
)

    echo "$PROMPT" | claude --print > /tmp/agent_${agent_num}_raw_output.txt 2>&1

    if [ $? -ne 0 ]; then
        warn "Agent ${agent_num} returned non-zero exit. Checking output..."
        cat /tmp/agent_${agent_num}_raw_output.txt
    fi

    # Extract the output file content
    python3 "$SCRIPT_DIR/extract-output.py" \
        "/tmp/agent_${agent_num}_raw_output.txt" \
        "$output_file" \
        "$(basename $output_file)"

    if [ -f "$output_file" ] && [ -s "$output_file" ]; then
        local lines=$(wc -l < "$output_file")
        success "Agent ${agent_num} complete → $output_file ($lines lines)"
    else
        error "Agent ${agent_num} failed to produce output at $output_file"
    fi

    echo ""
}

# ───────────────────────────────────────────────────────────────
# OPTIONAL: Run specific agent only
# Usage: bash run-all.sh 3   (runs only agent 3)
# ───────────────────────────────────────────────────────────────

START_FROM=${1:-1}  # Default: start from agent 1

# ───────────────────────────────────────────────────────────────
# Run the pipeline
# ───────────────────────────────────────────────────────────────

header "Portfolio Builder — Starting Pipeline from Agent $START_FROM"
echo "Project: $PROJECT_DIR"
echo "Outputs: $OUTPUTS_DIR"
echo ""

if [ "$START_FROM" -le 1 ]; then
    run_agent 1 "strategist" \
        "$OUTPUTS_DIR/positioning-brief.md" \
        "Analyzing source material and defining positioning narrative"
fi

if [ "$START_FROM" -le 2 ]; then
    run_agent 2 "researcher" \
        "$OUTPUTS_DIR/evidence-gaps.md" \
        "Auditing case studies for missing evidence and unsupported claims"
fi

if [ "$START_FROM" -le 3 ]; then
    run_agent 3 "critic" \
        "$OUTPUTS_DIR/case-study-audit.md" \
        "Auditing narrative structure against Simon Pan + Jobs frameworks"
fi

if [ "$START_FROM" -le 4 ]; then
    run_agent 4 "narrator" \
        "$OUTPUTS_DIR/final-copy.md" \
        "Writing all portfolio copy — homepage, case studies, about"
fi

if [ "$START_FROM" -le 5 ]; then
    run_agent 5 "designer" \
        "$OUTPUTS_DIR/index.html" \
        "Building production-grade HTML portfolio from final copy"
fi

# ───────────────────────────────────────────────────────────────
# Final summary
# ───────────────────────────────────────────────────────────────

header "Pipeline Complete"

echo "Output files:"
for f in "$OUTPUTS_DIR"/*.md "$OUTPUTS_DIR"/*.html; do
    if [ -f "$f" ]; then
        lines=$(wc -l < "$f")
        size=$(du -h "$f" | cut -f1)
        success "$(basename $f) — $lines lines, $size"
    fi
done

echo ""
echo -e "${BOLD}Open your portfolio:${NC}"
echo "  open $OUTPUTS_DIR/index.html"
echo ""
echo -e "${BOLD}Review the narrative chain:${NC}"
echo "  cat $OUTPUTS_DIR/positioning-brief.md"
echo "  cat $OUTPUTS_DIR/evidence-gaps.md"
echo "  cat $OUTPUTS_DIR/case-study-audit.md"
echo "  cat $OUTPUTS_DIR/final-copy.md"
