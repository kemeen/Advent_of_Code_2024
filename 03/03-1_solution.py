import re

INPUT = '03/input.txt'
MUL_PATTERN = r'mul\((?P<x>\d+),(?P<y>\d+)\)'

def read_input() -> str:
    with open(INPUT) as f:
        lines = f.read()
    return lines

def find_all_mul_pairs(input:str, pattern: str) -> list[tuple[str,str]]:
    mul_pattern = re.compile(pattern)
    return mul_pattern.findall(input)

def main():
    input = read_input()
    print(f"Read {input} as input")

    print(f'Found : {len(find_all_mul_pairs(input, MUL_PATTERN))} mul pairs')
    
    result = 0
    for x,y in find_all_mul_pairs(input, MUL_PATTERN):
        # print(f'x={x}, y={y}')
        result += int(x) * int(y)

    print(f'Result: {result}')


if __name__ == "__main__":
    main()