import re

def snake_to_camel():
    with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    return re.sub(r'_([а-я])', lambda x: x.group(1).upper(), content)

print(snake_to_camel())