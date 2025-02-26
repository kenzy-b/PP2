import re

def split_at_uppercase():
    with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    return re.findall(r'[А-Я][^А-Я]*', content)

print(split_at_uppercase())