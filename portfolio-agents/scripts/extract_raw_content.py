import re
import os
from bs4 import BeautifulSoup

# Paths to the raw HTML files
files = {
    'Beyond Touchscreens': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\sams-portfolio-main\sams-portfolio-main\raw-beyond.html',
    'Bhopal by Bike': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\sams-portfolio-main\sams-portfolio-main\raw-bhopal.html',
    'Dottie': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\sams-portfolio-main\sams-portfolio-main\raw-dottie.html',
    'Smartcoin': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\sams-portfolio-main\sams-portfolio-main\raw-smartcoin.html',
    'Vihar': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\sams-portfolio-main\sams-portfolio-main\raw-vihar.html',
}

def clean_text(text):
    """Clean up extracted text."""
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def is_meaningful(text):
    """Filter out navigation, footer, and short snippets."""
    if len(text) < 20:
        return False
    if "Terms" in text or "Privacy" in text or "Copyright" in text:
        return False
    return True

output_file = r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\outputs\extracted_copy.md'

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write("# Extracted Project Copy\n\n")

    for project_name, file_path in files.items():
        print(f"Processing {project_name}...")
        outfile.write(f"## {project_name}\n\n")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                
                # Framer often puts content in specific containers, but let's try generic extraction first
                # Iterate over all text elements
                
                # Strategies for Framer sites:
                # 1. Look for text in headings and paragraphs
                # 2. Look for aria-label in some cases
                # 3. Exclude hidden elements
                
                # Get all text nodes
                text_nodes = soup.find_all(string=True)
                
                extracted_lines = []
                for node in text_nodes:
                    parent = node.parent
                    if parent.name in ['script', 'style', 'meta', 'link', 'noscript']:
                        continue
                    
                    text = clean_text(str(node))
                    if is_meaningful(text):
                        extracted_lines.append(text)
                
                # Deduplicate consecutive lines
                deduped_lines = []
                for line in extracted_lines:
                    if not deduped_lines or deduped_lines[-1] != line:
                        deduped_lines.append(line)
                
                for line in deduped_lines:
                    outfile.write(f"{line}\n\n")
                    
        except Exception as e:
            outfile.write(f"Error processing {project_name}: {str(e)}\n")
            print(f"Error processing {project_name}: {str(e)}")

print(f"Extraction complete. Saved to {output_file}")
