import re

def lowercase_underscore():
    with open('row.txt', 'r', encoding = 'utf-8') as file:
        content = file.read()
    pattern = r'[а-я]+_[а-я]+'
    return re.findall(pattern, content)

print(lowercase_underscore())