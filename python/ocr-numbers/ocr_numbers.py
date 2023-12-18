ocr_nums = [[" _ ", "| |", "|_|", "   "], ["   ", "  |", "  |", "   "], [" _ ", " _|", "|_ ", "   "],
            [" _ ", " _|", " _|", "   "], ["   ", "|_|", "  |", "   "], [" _ ", "|_ ", " _|", "   "],
            [" _ ", "|_ ", "|_|", "   "], [" _ ", "  |", "  |", "   "], [" _ ", "|_|", "|_|", "   "],
            [" _ ", "|_|", " _|", "   "]]


def convert(input_grid: list[str]) -> str:
    if len(input_grid) % 4 != 0:
        # when the rows aren't multiples of 4
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(element) % 3 != 0 for element in input_grid):
        # when the columns aren't multiples of 3
        raise ValueError("Number of input columns is not a multiple of three")

    is_long = len(input_grid[0]) > 3

    if is_long:
        transformed_input = []
        for element in range(0, len(input_grid[0]), 3):
            sublist = []
            for line in input_grid:
                sublist.append(line[element:element + 3])
            transformed_input.append(sublist)
        input_grid = transformed_input

    answer = []
    for sublist in input_grid:
        if isinstance(sublist, list):
            answer.append(convert_ocr_to_num(sublist))
        else:
            answer.append(convert_ocr_to_num(input_grid))
            break

    return "".join(answer)

def convert_ocr_to_num(ocr):
    try:
        index_num = ocr_nums.index(ocr)
    except ValueError:
        index_num = '?'
    return str(index_num)



