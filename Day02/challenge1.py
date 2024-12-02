with (open("input.txt") as input):
     reports = [line.strip().split() for line in input]

reports = [[int(level) for level in report] for report in reports]
safe_reports = 0

for report in reports:
    safe = True
    decreased = False #33221110
    increased = False #1112223335557
    length = len(report)
    for i in range(1,length):
        if report[i-1] < report[i]:
            increased = True
        if report[i - 1] > report[i]:
            decreased = True
        if increased and decreased:
            safe = False
            break
        if report[i - 1] == report[i]:
            safe = False
            break
        if abs(report[i - 1] - report[i]) > 3:
            safe = False
            break
    if safe: safe_reports += 1

print(safe_reports)