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


def main():
    input = read_input()
    print(f"Read {len(input)} reports")

    # for report in input:
    #     print(report)
    #     print(report.split())
    #     print(is_report_safely_increasing(report.split()))
    #     print(is_report_safely_decreasing(report.split()))

    report_safety = [is_report_safely_increasing(report.split()) or is_report_safely_decreasing(report.split()) for report in input]
    print(f"There are {sum(report_safety)} safe reports")


if __name__ == "__main__":
    main()