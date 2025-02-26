import re

def a_zero_or_more_b():
    with open('row.txt', 'r', encoding = 'utf-8') as file:
        content = file.read()
    pattern = r'аб*'
    return re.findall(pattern, content)

print(a_zero_or_more_b())