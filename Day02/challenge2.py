def isSafe(report):
    safe = True
    decreased = False  # 33221110
    increased = False  # 1112223335557
    length = len(report)

    if length == 1:
        return True

    for i in range(1, length):
        if report[i - 1] < report[i]:
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
    return safe


with (open("input.txt") as input):
    reports = [line.strip().split() for line in input]

reports = [[int(level) for level in report] for report in reports]
safe_reports = 0

for report in reports:
    if isSafe(report):
        safe_reports += 1
    else:
        for i in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(i)
            if isSafe(report_copy):
                safe_reports += 1
                break
print(safe_reports)