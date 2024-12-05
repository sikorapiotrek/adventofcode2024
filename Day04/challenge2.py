import numpy as np

file = open("input.txt")
instructions = file.readlines()
array = np.array([list(x.strip()) for x in instructions])

rows, columns = array.shape

square = array[0:3,0:3].ravel()

matches = ['MMASS','MSAMS','SSAMM','SMASM']
xmas = 0

for i in range(rows-2):
    for j in range(columns-2):
        square = array[i:i+3,j:j+3].ravel()
        square = "".join(square[0::2])
        if square in matches:
            xmas += 1
print(xmas)
