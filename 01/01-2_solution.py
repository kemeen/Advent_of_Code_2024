INPUT = '/Users/kevinengel/Library/CloudStorage/OneDrive-SharedLibraries-Onedrive/coding/Advent_of_code/2024/01/input.txt'


def main():
    with open(INPUT) as f:
        lines = f.readlines()

    list_a = [int(line.rstrip("\n").split("   ")[0]) for line in lines]
    list_b = [int(line.rstrip("\n").split("   ")[1]) for line in lines]

    # init quantity map
    quantity_map = {}
    for i in list_a:
        if i in quantity_map:
            continue
        else:
            quantity_map[i] = 0

    for i in list_b:
        if i in quantity_map:
            quantity_map[i] += 1

    similarity_values = [quantity_map[i]*int(i) for i in list_a]
    print(sum(similarity_values))

if __name__ == "__main__":
    main()