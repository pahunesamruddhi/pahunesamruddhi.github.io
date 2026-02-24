#!/usr/bin/env python3
"""
extract-output.py
Extracts agent output from Claude's raw response and saves to the target file.

Usage: python3 extract-output.py <raw_output_file> <target_output_path> <filename>
"""

import sys
import re
import os

def extract_output(raw_file: str, target_path: str, filename: str) -> bool:
    with open(raw_file, 'r') as f:
        content = f.read()

    # Pattern 1: Look for === OUTPUT FILE: ... === blocks
    pattern1 = r'=== OUTPUT FILE:.*?===\n(.*?)\n=== END OUTPUT ==='
    matches = re.findall(pattern1, content, re.DOTALL)
    
    if matches:
        # Take the last match (most complete version)
        extracted = matches[-1].strip()
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, 'w') as f:
            f.write(extracted)
        print(f"Extracted via pattern 1: {len(extracted)} chars")
        return True

    # Pattern 2: Look for markdown code blocks with the filename
    pattern2 = rf'```(?:markdown|html|md)?\n(.*?)\n```'
    matches = re.findall(pattern2, content, re.DOTALL)
    
    if matches:
        # Take the largest block (most likely the full output)
        largest = max(matches, key=len)
        if len(largest) > 200:  # Sanity check
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, 'w') as f:
                f.write(largest.strip())
            print(f"Extracted via pattern 2: {len(largest)} chars")
            return True

    # Pattern 3: If the output IS the file (Claude wrote it directly)
    # Look for the characteristic section headers
    if filename.endswith('.md'):
        if '# ' in content and len(content) > 500:
            # Find the first # heading and take from there
            idx = content.find('\n# ')
            if idx == -1:
                idx = content.find('# ')
            if idx != -1:
                extracted = content[idx:].strip()
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                with open(target_path, 'w') as f:
                    f.write(extracted)
                print(f"Extracted via pattern 3 (markdown): {len(extracted)} chars")
                return True

    if filename.endswith('.html'):
        if '<!DOCTYPE html>' in content or '<html' in content:
            idx = content.find('<!DOCTYPE html>')
            if idx == -1:
                idx = content.find('<html')
            extracted = content[idx:].strip()
            # Find closing tag
            end_idx = extracted.rfind('</html>') 
            if end_idx != -1:
                extracted = extracted[:end_idx + 7]
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, 'w') as f:
                f.write(extracted)
            print(f"Extracted via pattern 3 (html): {len(extracted)} chars")
            return True

    # Fallback: Save the raw output (let the user inspect)
    print(f"WARNING: Could not extract structured output. Saving raw response.")
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w') as f:
        f.write(content)
    return True


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: extract-output.py <raw_file> <target_path> <filename>")
        sys.exit(1)
    
    success = extract_output(sys.argv[1], sys.argv[2], sys.argv[3])
    sys.exit(0 if success else 1)
