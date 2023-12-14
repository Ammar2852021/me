import cssutils
from rcssmin import cssmin

def remove_duplicate_rules(input_css, output_css_file):
    # Parse the input CSS
    sheet = cssutils.CSSParser().parseString(input_css)

    # Use a set to track already used rules
    seen_rules = set()

    # Remove duplicate rules
    rules_to_remove = set()
    for rule in sheet:
        if rule.type == rule.STYLE_RULE and rule.cssText is not None:
            # Convert the rule to a lowercase string to ensure case-insensitive comparison
            rule_text = rule.cssText.lower()
            if rule_text in seen_rules:
                rules_to_remove.add(rule)
            else:
                seen_rules.add(rule_text)

    # Remove duplicate rules
    for rule in rules_to_remove:
        sheet.cssRules.remove(rule)

    # Minify the modified CSS for better formatting
    formatted_css = cssmin(sheet.cssText).decode('utf-8')

    # Write the formatted CSS to a new file
    with open(output_css_file, 'w', encoding='utf-8') as output_file:
        output_file.write(formatted_css)

input_css = """ 









"""
output_css_file = "output.css"
remove_duplicate_rules(input_css, output_css_file)
