import re

def find_uppercase_lowercase():
    with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r'[А-Я][а-я]+'
    return re.findall(pattern, content)

print(find_uppercase_lowercase())