INPUT = '02/input.txt'

def read_input() -> list[str]:
    with open(INPUT) as f:
        lines = f.readlines()
    return lines

def is_report_safely_increasing(report: list[str]) -> bool:
    last_level = int(report[0])
    for level in report[1:]:
        if int(level) <= last_level:
            return False
        if int(level) - last_level > 3:
            return False
        last_level = int(level)
    return True

def is_report_safely_decreasing(report: list[str]) -> bool:
    last_level = int(report[0])
    for level in report[1:]:
        if int(level) >= last_level:
            return False
        if last_level - int(level) > 3:
            return False
        last_level = int(level)
    return True

def is_report_safe_with_problem_dampener(report: list[str]) -> bool:
    if is_report_safely_increasing(report) or is_report_safely_decreasing(report):
        return True
    for i in range(len(report)):
        reduced_report = report.copy()
        reduced_report.pop(i)
        if is_report_safely_increasing(reduced_report) or is_report_safely_decreasing(reduced_report):
            return True
    return False

def main():
    input = read_input()
    print(f"Read {len(input)} reports")

    report_safety = [is_report_safe_with_problem_dampener(report.split()) for report in input]
    print(f"There are {sum(report_safety)} safe reports")


if __name__ == "__main__":
    main()