import re

def match_a_two_to_three_b():
    with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r'аб{2,3}'
    return re.findall(pattern, content)

print(match_a_two_to_three_b())