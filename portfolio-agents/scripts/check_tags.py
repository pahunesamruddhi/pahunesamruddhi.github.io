import re
with open('../outputs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('id="cs-vihar"')
end = content.find('id="cs-bhopal"')
vihar = content[start:end]

tags = ['section','div','figure','blockquote','table','thead','tbody',
        'tr','td','th','ul','li','span','p','h1','h2','h3','em','strong','figcaption']
void_tags = ['img','br','hr']

for t in tags:
    opens = len(re.findall(r'<' + t + r'[\s>]', vihar))
    closes = len(re.findall(r'</' + t + '>', vihar))
    if opens != closes:
        print(f'MISMATCH {t}: {opens} opens, {closes} closes')
    else:
        print(f'{t}: {opens} balanced')

for t in void_tags:
    count = len(re.findall(r'<' + t + r'[\s>]', vihar))
    print(f'{t}: {count} (void)')

print(f'\nVihar section length: {len(vihar)} chars')
