import codecs
import re

def process_file(filepath, ids_to_keep):
    try:
        with codecs.open(filepath, 'r', 'utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return
        
    all_sections = ['powerhub', 'mini', 'pro', 'rack', 'battery']
    for sec in all_sections:
        if sec not in ids_to_keep:
            # Matches from the preceding comment block down to the end of the section tag
            pattern1 = re.compile(r'<!--\s*â• \s*â•.*?â• \s*-->\s*<section[^>]*id="' + sec + r'"[^>]*>.*?</section>', re.DOTALL)
            pattern2 = re.compile(r'<!--\s*[â•═]+\s*[\w\s—\-]+\s*[â•═]+\s*-->\s*<section[^>]*id="' + sec + r'"[^>]*>.*?</section>', re.DOTALL)
            pattern3 = re.compile(r'<!--.*?-->\s*<section[^>]*id="' + sec + r'"[^>]*>.*?</section>', re.DOTALL)
            pattern4 = re.compile(r'<section[^>]*id="' + sec + r'"[^>]*>.*?</section>', re.DOTALL)

            if pattern1.search(content):
                content = pattern1.sub('', content)
            elif pattern2.search(content):
                content = pattern2.sub('', content)
            elif pattern3.search(content):
                content = pattern3.sub('', content)
            else:
                content = pattern4.sub('', content)

    # Note: the CTA section is not removed.

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)
    print(f"Processed {filepath} - kept {ids_to_keep}")

if __name__ == '__main__':
    process_file('powerhub.html', ['powerhub', 'battery'])
    process_file('powerhubmini.html', ['mini'])
    process_file('powerhubpro.html', ['pro', 'battery'])
    process_file('powerrack.html', ['rack'])
