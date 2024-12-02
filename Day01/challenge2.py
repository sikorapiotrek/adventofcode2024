from collections import Counter

with (open("input.txt") as input):
    lines = input.readlines()
    length = len(lines)
    left = []
    right = []

    for line in lines:
        line = line.strip().split('   ')
        left.append(int(line[0]))
        right.append(int(line[1]))

    right_counted = Counter(right)
    right_numbers = right_counted.keys()

    similarity = 0

    for i in left:
        if i in right_numbers:
            similarity += i * right_counted[i]

    print(similarity)
