import re
from typing import List, Any

import numpy as np

file = open("input.txt")
instructions = file.readlines()
array = np.array([list(x.strip()) for x in instructions])

xmas = 0

#horizonatal search

for x in instructions:
    xmas_found = re.findall(r"XMAS", x)
    samx_found = re.findall(r"SAMX", x)
    xmas += len(samx_found) + len(xmas_found)
print(xmas)
#vertical search

instructions_T = ["".join(x.tolist()) for x in array.T]

for x in instructions_T:
    xmas_found = re.findall(r"XMAS", x)
    samx_found = re.findall(r"SAMX", x)
    xmas += len(samx_found) + len(xmas_found)

#diagonal search
rows, columns = array.shape

for i in range(rows - 3):
    for j in range(columns - 3):
        possibleXMAS1 = [array[i+n][j+n] for n in range(4)]
        possibleXMAS2 = [array[i+3-n][j+n] for n in range(4)]
        if "XMAS" == "".join(possibleXMAS1):
            xmas += 1
            print('xmas \\')
        elif "SAMX" == "".join(possibleXMAS1):
            xmas += 1
            print('samx \\')
        if "XMAS" == "".join(possibleXMAS2):
            xmas += 1
        elif "SAMX" == "".join(possibleXMAS2):
            xmas += 1

print(xmas)