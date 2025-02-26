import re

def camel_to_snake():
    with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    return re.sub(r'(?<!^)([А-Я])', r'_\1', content).lower()

print(camel_to_snake())