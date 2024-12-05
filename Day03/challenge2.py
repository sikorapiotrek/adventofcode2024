import re

with open("test.txt") as file:
    instructions = file.read()

pattern = ['mul\([0-9]{1,3},[0-9]{1,3}\)', 'do\(\)', "don't\(\)"]
regex = re.compile(r'' + '|'.join(pattern))
out = [m.group() for m in regex.finditer(instructions)]

enabled = True
summ = 0

for x in out:
    if x == "do()":
        enabled = True
    elif x == "don't()":
        enabled = False
    elif enabled:
        a, b = x.strip('mul()').split(',')
        summ += int(a) * int(b)

print(summ)
