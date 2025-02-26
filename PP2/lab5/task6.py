import re

def replace_space_comma_dot():
    with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', content)

print(replace_space_comma_dot())