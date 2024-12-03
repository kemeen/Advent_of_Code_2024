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

def split_do_blocks(input: str) -> list[str]:
    return input.split('do()')

def filter_dont_blocks(input: list[str]) -> list[str]:
    return [x.split('don\'t()')[0] for x in input if x != '']

def calculate_result_for_instruction_block(input: str) -> int:
    result = 0
    for x,y in find_all_mul_pairs(input, MUL_PATTERN):
        # print(f'x={x}, y={y}')
        result += int(x) * int(y)
    return result

def main():
    input = read_input()
    print(f"Read {input} as input")

    # split into "DO" blocks
    input = split_do_blocks(input)

    # remove "don't" blocks
    input = filter_dont_blocks(input)

    print(f'Found the following do blocks: {input} to process')
    
    result = 0
    for instruction_block in input:
        print(f'Processing instruction block: {instruction_block}')
        block_result = calculate_result_for_instruction_block(instruction_block)
        print(f'Block Result: {block_result}')
        result += block_result
        print('='*100)

    print(f'Result: {result}')


if __name__ == "__main__":
    main()