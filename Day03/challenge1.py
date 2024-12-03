#regexp mul\([0-9]{1,3},[0-9]{1,3}\)
import re

with open("input.txt") as file:
    instructions = file.read()

pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
results = re.findall(pattern,instructions)
results = [x.strip('mul()').split(',') for x in results]
summ = sum([int(x[0]) * int(x[1]) for x in results])
print(summ)
