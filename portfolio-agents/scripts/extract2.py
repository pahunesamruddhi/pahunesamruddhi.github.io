"""
Extract all visible text content from Framer-generated HTML files.
Text is embedded as rendered HTML in elements with class="framer-text".
Uses only Python standard library (html.parser).
"""
import re
from html.parser import HTMLParser
import os

FILES = {
    'Beyond Touchscreens': r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Beyond Touchscreens\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
    'Bhopal by Bike':      r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Bhopal by Bike\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
    'Dottie':              r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Dottie\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
    'Smartcoin':           r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Smartcoin\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
    'Vihar':               r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\Case Studies\Vihar\PORTFOLIO _ SAMRUDDHI PAHUNE.html',
}

SKIP_TAGS = {'script', 'style', 'link', 'meta', 'noscript', 'iframe', 'svg', 'defs', 'template'}
BLOCK_TAGS = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ul', 'ol', 'div'}

class FramerTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_skip = 0
        self.in_framer = 0
        self._stack = []
        self._buf = []
        self.text_blocks = []
        self.current_tag_name = None

    def _has_framer_text(self, attrs):
        for k, v in attrs:
            if k == 'class' and v and 'framer-text' in v.split():
                return True
        return False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        is_skip = tag in SKIP_TAGS
        is_ft = (not is_skip) and self._has_framer_text(attrs)
        self._stack.append((tag, is_skip, is_ft))
        if is_skip:
            self.in_skip += 1
            return
        if self.in_skip:
            return
        if is_ft:
            self.in_framer += 1
        if tag in BLOCK_TAGS:
            self._flush()
        self.current_tag_name = tag

    def handle_endtag(self, tag):
        tag = tag.lower()
        for i in range(len(self._stack)-1, -1, -1):
            if self._stack[i][0] == tag:
                _, was_skip, was_ft = self._stack.pop(i)
                if was_skip:
                    self.in_skip = max(0, self.in_skip - 1)
                elif was_ft and not self.in_skip:
                    self.in_framer = max(0, self.in_framer - 1)
                break
        if tag in BLOCK_TAGS and not self.in_skip:
            self._flush()

    def _flush(self):
        text = ''.join(self._buf).strip()
        if text and text != '\u200b':
            self.text_blocks.append(text)
        self._buf = []

    def handle_data(self, data):
        if self.in_skip:
            return
        if self.in_framer > 0:
            self._buf.append(data)

    def get_blocks(self):
        self._flush()
        return self.text_blocks


def extract_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    saved_url_m = re.search(r'<!-- saved from url=\(0+\)(.*?) -->', content)
    saved_url = saved_url_m.group(1).strip() if saved_url_m else 'unknown'
    parser = FramerTextExtractor()
    parser.feed(content)
    blocks = parser.get_blocks()
    # Deduplicate preserving order
    seen = set()
    unique = []
    for b in blocks:
        if b not in seen:
            seen.add(b)
            unique.append(b)
    return saved_url, unique


out_lines = ['# Extracted Case Study Text Content', '', '---', '']

for name, path in FILES.items():
    saved_url, blocks = extract_file(path)
    out_lines.append(f'## CASE STUDY: {name}')
    out_lines.append(f'**Source:** {saved_url}')
    out_lines.append('')
    for b in blocks:
        out_lines.append(b)
        out_lines.append('')
    out_lines.append('---')
    out_lines.append('')
    print(f'[{name}] {len(blocks)} text blocks extracted from {saved_url}')

out_path = r'c:\Users\pahun\Downloads\portfolio-agents\portfolio-agents\outputs\extracted-case-study-text.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
print(f'\nSaved: {out_path}')
