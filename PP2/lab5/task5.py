import re

def a_anything_b():
    with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r'а.*б'
    return re.findall(pattern, content)

print(a_anything_b())