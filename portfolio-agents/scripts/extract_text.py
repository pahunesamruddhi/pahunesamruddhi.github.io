import re
import html as html_module
from html.parser import HTMLParser
import sys
import os

files = {
    'Beyond Touchscreens': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Beyond Touchscreens\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
    'Bhopal by Bike': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Bhopal by Bike\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
    'Dottie': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Dottie\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
    'Smartcoin': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Smartcoin\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
    'Vihar': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Vihar\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
}

def is_readable_text(s):
    """Filter out noise: hashes, CSS classes, URLs, code identifiers, short strings."""
    if len(s) < 8:
        return False
    # Skip URLs
    if s.startswith('http') or s.startswith('//') or s.startswith('www'):
        return False
    # Skip hex hashes / base64
    if re.match(r'^[a-f0-9A-F\-]{20,}$', s):
        return False
    # Skip things that look like code (camelCase identifiers, CSS selectors)
    if re.match(r'^[a-zA-Z][a-zA-Z0-9]{0,3}[A-Z][a-zA-Z0-9]+$', s) and len(s) < 30:
        return False
    # Skip file extensions / paths
    if re.search(r'\.(js|css|mjs|png|jpg|svg|woff|ttf|json)(\?|$)', s):
        return False
    # Must contain at least one space (real sentences/phrases have spaces)
    if ' ' not in s and len(s) < 30:
        return False
    # Skip if mostly non-alpha characters
    alpha_ratio = sum(1 for c in s if c.isalpha()) / len(s)
    if alpha_ratio < 0.4:
        return False
    return True

def extract_strings_from_json(obj, depth=0):
    """Recursively walk JSON and extract string values."""
    results = []
    if depth > 20:
        return results
    if isinstance(obj, str):
        s = html.unescape(obj)
        if is_readable_text(s):
            results.append(s)
    elif isinstance(obj, list):
        for item in obj:
            results.extend(extract_strings_from_json(item, depth+1))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            results.extend(extract_strings_from_json(v, depth+1))
    return results

output_lines = []

for name, path in files.items():
    output_lines.append(f'\n{"="*60}')
    output_lines.append(f'CASE STUDY: {name}')
    output_lines.append(f'{"="*60}')
    
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Strategy 1: Look for __NEXT_DATA__ JSON blob
    found_data = False
    m = re.search(r'<script[^>]*id=["\']__NEXT_DATA__["\'][^>]*>(.*?)</script>', content, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(1))
            strings = extract_strings_from_json(data)
            seen = set()
            unique_strings = []
            for s in strings:
                if s not in seen:
                    seen.add(s)
                    unique_strings.append(s)
            output_lines.append(f'\n[Source: __NEXT_DATA__ JSON - {len(unique_strings)} text strings found]\n')
            for s in unique_strings:
                output_lines.append(f'  • {s}')
            found_data = True
        except Exception as e:
            output_lines.append(f'  [__NEXT_DATA__ JSON parse failed: {e}]')
    
    # Strategy 2: Look for any large JSON object in script tags
    script_jsons = re.findall(r'<script[^>]*>(window\.__.*?)</script>', content, re.DOTALL)
    for js in script_jsons:
        # Find JSON objects within
        json_matches = re.findall(r'=\s*(\{.*?\});?\s*$', js, re.DOTALL | re.MULTILINE)
        for jm in json_matches[:3]:
            try:
                data = json.loads(jm)
                strings = extract_strings_from_json(data)
                if strings:
                    output_lines.append(f'\n[Source: window.* script JSON]\n')
                    seen = set()
                    for s in strings:
                        if s not in seen:
                            seen.add(s)
                            output_lines.append(f'  • {s}')
            except:
                pass
    
    # Strategy 3: Look for serialized component data - find "text" or "children" or "content" keys 
    # by searching raw content for patterns like "text":"...", "children":"..."
    text_patterns = re.findall(r'"(?:text|children|content|title|description|heading|label|value|placeholder|alt|caption|richText|styledText|plainText)":\s*"([^"]{8,500})"', content)
    if text_patterns:
        seen2 = set()
        readable = []
        for s in text_patterns:
            s2 = html.unescape(s)
            if s2 not in seen2 and is_readable_text(s2):
                seen2.add(s2)
                readable.append(s2)
        if readable:
            output_lines.append(f'\n[Source: text/children/content keys - {len(readable)} strings]\n')
            for s in readable:
                output_lines.append(f'  • {s}')
            found_data = True

    # Strategy 4: Find all strings between quotes that look like real English text
    # Look specifically at script tag content for long readable strings
    all_script = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
    long_strings = []
    seen3 = set()
    for script in all_script:
        # Look for strings with multiple words (contain spaces), longer than 20 chars
        matches = re.findall(r'"([A-Za-z][^"]{15,400})"', script)
        for s in matches:
            s2 = html.unescape(s)
            if s2 not in seen3 and is_readable_text(s2) and ' ' in s2:
                # Additional filter: must look like real prose (has common English words or mixed caps/lowercase)
                words = s2.split()
                if len(words) >= 3:
                    seen3.add(s2)
                    long_strings.append(s2)
    
    if long_strings:
        output_lines.append(f'\n[Source: Long readable strings from scripts - {len(long_strings)} found]\n')
        for s in long_strings:
            output_lines.append(f'  • {s}')
        found_data = True

    if not found_data:
        output_lines.append('\n  [No readable text content found with current strategies]')

# Write to output file and also print
output_text = '\n'.join(output_lines)
out_path = r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\outputs\extracted-case-study-text.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('# Extracted Case Study Text Content\n\n')
    f.write(output_text)

print(output_text)
print(f'\n\nSaved to: {out_path}')
