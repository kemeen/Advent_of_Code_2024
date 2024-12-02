INPUT = '/Users/kevinengel/Library/CloudStorage/OneDrive-SharedLibraries-Onedrive/coding/Advent_of_code/2024/01/input.txt'

def main():
    with open(INPUT) as f:
        lines = f.readlines()

    list_a = sorted([int(line.rstrip("\n").split("   ")[0]) for line in lines])
    list_b = sorted([int(line.rstrip("\n").split("   ")[1]) for line in lines])

    sum = 0
    for a,b in zip(list_a,list_b):
        sum += abs(a-b)

    print(sum)