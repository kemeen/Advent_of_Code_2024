INPUT = '04/input.txt'

def read_input() -> str:
    with open(INPUT) as f:
        lines = f.read()
    return lines

def get_matrix_dimensions(input: str) -> tuple[int,int]:
    matrix = input.split('\n')

    # remove empty lines
    matrix = [x for x in matrix if x != '']

    return (len(matrix[0]), len(matrix))

def convert_to_single_string(input: str) -> str:   
    return input.replace('\n', '')

def get_matrix_coordinate_from_index(index: int, dimensions: tuple[int,int]) -> tuple[int,int]:
    return (index % dimensions[0], index // dimensions[0])

# get a word at a given matrix coordinate
def get_letter_at_matrix_coordinate(matrix: str, coordinate: tuple[int,int], dimensions: tuple[int,int]) -> str:
    return matrix [coordinate[1] * dimensions[1] + coordinate[0]]

# check if coordinate is valid
def is_valid_matrix_coordinate(coordinate: tuple[int,int], dimensions: tuple[int,int]) -> bool:
    return coordinate[0] >= 0 and coordinate[0] < dimensions[0] and coordinate[1] >= 0 and coordinate[1] < dimensions[1]

def get_n_length_word_in_direction(matrix: str, coordinate: tuple[int,int], dimensions: tuple[int,int], direction: tuple[int,int], length: int) -> str:
    if not is_valid_matrix_coordinate(coordinate, dimensions):
        return ""
    word = get_letter_at_matrix_coordinate(matrix, (coordinate[0], coordinate[1]), dimensions)
    while is_valid_matrix_coordinate((coordinate[0] + direction[0], coordinate[1] + direction[1]), dimensions):
        word += get_letter_at_matrix_coordinate(matrix, (coordinate[0] + direction[0], coordinate[1] + direction[1]), dimensions)
        coordinate = (coordinate[0] + direction[0], coordinate[1] + direction[1])
        if len(word) == length:
            return word
    return word

def main():
    input = read_input()
    # print(f"Read input:\n{input}")

    dimensions = get_matrix_dimensions(input)
    print(f"Dimensions: {dimensions}")

    # put input into matrix format
    input = convert_to_single_string(input)
    # print(input)

    search_directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

    # get all "X" characters and their matrix coordinates
    xmas_coordinates = []
    for i, x in enumerate(input):
        if x == 'X':
            # get coordinate
            coordinate = get_matrix_coordinate_from_index(i, dimensions)
            
            for dir in search_directions:
                word = get_n_length_word_in_direction(input, coordinate, dimensions, dir, 4)
                if word == 'XMAS':
                    xmas_coordinates.append((coordinate, dir))
                    # print(word, coordinate, dir)

    print(f'Found {len(xmas_coordinates)} XMAS coordinates')
           


if __name__ == "__main__":
    main()