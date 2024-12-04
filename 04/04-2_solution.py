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

def get_x_words(matrix: str, coordinate: tuple[int,int], dimensions: tuple[int,int], length: int, offset: int) -> str:
    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
    words = []
    for dir in directions:
        starting_coordinate = (coordinate[0] + dir[0] * offset, coordinate[1] + dir[1] * offset)
        words.append(get_n_length_word_in_direction(matrix, starting_coordinate, dimensions, dir, length))
    return words

def main():
    input = read_input()
    # print(f"Read input:\n{input}")

    dimensions = get_matrix_dimensions(input)
    print(f"Dimensions: {dimensions}")

    # put input into matrix format
    input = convert_to_single_string(input)
    # print(input)

    # get all "X" shaped MAS characters and their matrix coordinates
    x_mas_coordinates = []
    for i, x in enumerate(input):
        if x == 'A':
            # get coordinate
            coordinate = get_matrix_coordinate_from_index(i, dimensions)
            
            x_words = get_x_words(input, coordinate, dimensions, 3, -1)

            if x_words.count('MAS') == 2:
                x_mas_coordinates.append((coordinate, x_words))
    print(f'Found {len(x_mas_coordinates)} XMAS coordinates')
           


if __name__ == "__main__":
    main()