import re
with open('outputs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('id="cs-dottie"')
end = content.find('<!-- Case Study: Beyond Touchscreens')
dottie = content[start:end]

tags = ['section','div','figure','blockquote','table','thead','tbody',
        'tr','td','th','ul','li','span','p','h1','h2','h3','em','strong','figcaption','a','button']
void_tags = ['img','br','hr']

for t in tags:
    opens = len(re.findall(r'<' + t + r'[\s>]', dottie))
    closes = len(re.findall(r'</' + t + '>', dottie))
    if opens != closes:
        print(f'MISMATCH {t}: {opens} opens, {closes} closes')
    else:
        print(f'{t}: {opens} balanced')

for t in void_tags:
    count = len(re.findall(r'<' + t + r'[\s>]', dottie))
    print(f'{t}: {count} (void)')

print(f'\nDottie section length: {len(dottie)} chars')
