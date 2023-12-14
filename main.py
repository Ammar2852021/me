from bs4 import BeautifulSoup
import cssbeautifier
import jsbeautifier

def beautify_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.prettify()

def beautify_css(css_content):
    return cssbeautifier.beautify(css_content)

def beautify_js(js_content):
    return jsbeautifier.beautify(js_content)

def process_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Beautify HTML
    beautified_html = beautify_html(content)

    # Beautify CSS
    css_styles = '\n'.join([tag.text for tag in BeautifulSoup(content, 'html.parser').find_all('style')])
    beautified_css = beautify_css(css_styles)

    # Beautify JavaScript
    js_scripts = '\n'.join([tag.text for tag in BeautifulSoup(content, 'html.parser').find_all('script')])
    beautified_js = beautify_js(js_scripts)

    # Combine everything
    final_content = f"{beautified_html}\n<style>\n{beautified_css}\n</style>\n<script>\n{beautified_js}\n</script>"

    # Save to a new file or overwrite the existing one
    with open('formatted_index.html', 'w', encoding='utf-8') as output_file:
        output_file.write(final_content)

if __name__ == "__main__":
    html_file_path = "D:/c/me/index.html"
    process_html_file(html_file_path)
