import re

def insert_spaces():
    with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    return re.sub(r'(?<!^)([А-Я])', r' \1', content)

print(insert_spaces())