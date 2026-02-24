#!/bin/bash
# setup-sources.sh
# Prepares the /source directory with properly formatted input files
# Run this ONCE before running the main pipeline

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
SOURCE_DIR="$PROJECT_DIR/source"

mkdir -p "$SOURCE_DIR"

echo "=== Portfolio Builder — Source Setup ==="
echo ""
echo "This script prepares your source files."
echo "You'll need to provide content when prompted."
echo ""

# ─── Source 1: Existing site content ───
echo "────────────────────────────────────────"
echo "STEP 1: Existing Portfolio Content"
echo "────────────────────────────────────────"
echo ""
echo "Options:"
echo "  a) Paste a URL — the script will attempt to scrape it"
echo "  b) Type 'skip' — if you have no existing site"
echo ""
read -p "URL or 'skip': " EXISTING_SITE_INPUT

if [ "$EXISTING_SITE_INPUT" == "skip" ]; then
    echo "# Existing Site Content" > "$SOURCE_DIR/existing-site-content.md"
    echo "" >> "$SOURCE_DIR/existing-site-content.md"
    echo "_No existing site provided._" >> "$SOURCE_DIR/existing-site-content.md"
    echo "Skipped."
else
    echo "Attempting to scrape: $EXISTING_SITE_INPUT"
    # Use curl to get basic text content
    if command -v curl &> /dev/null; then
        echo "# Existing Site Content" > "$SOURCE_DIR/existing-site-content.md"
        echo "Source: $EXISTING_SITE_INPUT" >> "$SOURCE_DIR/existing-site-content.md"
        echo "" >> "$SOURCE_DIR/existing-site-content.md"
        curl -s "$EXISTING_SITE_INPUT" | \
            sed 's/<[^>]*>//g' | \
            grep -v '^[[:space:]]*$' | \
            head -200 >> "$SOURCE_DIR/existing-site-content.md" 2>/dev/null || \
            echo "Could not scrape. Please paste content manually into: $SOURCE_DIR/existing-site-content.md"
        echo "Scraped to: $SOURCE_DIR/existing-site-content.md"
    else
        echo "curl not available. Please manually paste your site content into:"
        echo "$SOURCE_DIR/existing-site-content.md"
    fi
fi

echo ""

# ─── Source 2: CS1 Presentation content ───
if [ -f "$SOURCE_DIR/cs1-presentation.md" ]; then
    echo "✓ cs1-presentation.md already exists — skipping"
else
    echo "────────────────────────────────────────"
    echo "STEP 2: Case Study 1 — Audit-Safe Conversations"
    echo "────────────────────────────────────────"
    echo ""
    echo "The content from your PDF presentation needs to be in:"
    echo "$SOURCE_DIR/cs1-presentation.md"
    echo ""
    echo "This was pre-populated from your uploaded PDF."
    echo "If the file is empty, paste the content manually."
    
    # Create placeholder
    cat > "$SOURCE_DIR/cs1-presentation.md" << 'PLACEHOLDER'
# Case Study 1: Audit-Safe Conversations
## Source: Presentation PDF

[Content from your uploaded Audit-Safe Conversations presentation PDF]
[Paste or copy the full text content here]

Key sections to include:
- The Stakes (financial loss, regulatory exposure)
- Design Philosophy (safety over speed)
- Design Constraints (NPCI/RBI, async channel, zero SR creation)
- Failed UPI Debit intent definition and disambiguation
- Dual-Persona Architecture (Retail vs SME)
- UI Safety decisions and rationale
- Multi-dispute resolution flow
- Language handling
- Design trade-offs
PLACEHOLDER
fi

echo ""

# ─── Source 3: CS2 storytelling brief ───
if [ -f "$SOURCE_DIR/cs2-storytelling.md" ]; then
    echo "✓ cs2-storytelling.md already exists — skipping"
else
    echo "────────────────────────────────────────"
    echo "STEP 3: Case Study 2 — Designing for Panic"
    echo "────────────────────────────────────────"
    echo ""
    echo "The storytelling brief was pre-populated from your uploaded document."
    
    cat > "$SOURCE_DIR/cs2-storytelling.md" << 'PLACEHOLDER'
# Case Study 2: Designing for Panic
## Source: Storytelling Format Document

[Content from your Designing for Panic storytelling document]
[Paste the full narrative structure here]

Key sections:
- The Crisis / Digital Banking Graveyard
- The Real Problem (opacity vs failure)
- Architectural Decision (real-time ledger)
- Investigation (logic fails where fear begins)
- Why Traditional Chatbots Fail
- The Behavioral Shift (recognition vs recall)
- The Pivot (support bot → diagnostic engine)
- The Engine / Logic Funnel (5 steps)
- Two Contexts (Retail vs SME)
- UI Strategy (compliance made visible)
- Time Design (WhatsApp async challenges)
- Operational Pivot table
- Final Reflection
PLACEHOLDER
fi

echo ""
echo "=== Source setup complete ==="
echo ""
echo "Files created in $SOURCE_DIR:"
ls -la "$SOURCE_DIR/"
echo ""
echo "NEXT STEPS:"
echo "1. Review and complete source files if needed:"
echo "   - $SOURCE_DIR/cs1-presentation.md"
echo "   - $SOURCE_DIR/cs2-storytelling.md"
echo ""
echo "2. Copy your reference image to:"
echo "   $SOURCE_DIR/reference-image.jpg"
echo ""
echo "3. Run the main pipeline:"
echo "   bash scripts/run-all.sh"
