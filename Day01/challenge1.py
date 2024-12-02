with (open("input.txt") as input):
    lines = input.readlines()
    length = len(lines)
    left = []
    right = []

    for line in lines:
        line = line.strip().split('   ')
        left.append(int(line[0]))
        right.append(int(line[1]))

    distance = 0
    for _ in range(length):
        left_min = min(left)
        left_index = left.index(left_min)
        right_min = min(right)
        right_index = right.index(right_min)
        distance += abs(left_min - right_min)
        left[left_index] = float('inf')
        right[right_index] = float('inf')

    print(distance)
