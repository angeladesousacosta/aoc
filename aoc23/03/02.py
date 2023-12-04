import math


SYMBOLS = {
    '*'
}


def main():
    with open('input/schematic.txt', 'r') as file:
        lst = []

        lines = file.readlines()

        for line in lines:
            lst.append(list(line.strip()))

        rows = len(lst)
        columns = len(lst[0])
        part_nums = set()
        calculated_sum = 0

        for r in range(rows):
            for c in range(columns):
                if lst[r][c] in SYMBOLS:
                    a = set()

                    for diagonal_row in range (-1, 2):
                        for diagonal_column in range (-1, 2):
                            new_row, new_column = r + diagonal_row, c + diagonal_column

                            if lst[new_row][new_column].isdigit() and (new_row, new_column) not in part_nums:
                                start_column = new_column

                                while start_column > 0 and lst[new_row][start_column - 1].isdigit():
                                    start_column = start_column - 1

                                end_column = new_column

                                while end_column < columns - 1 and lst[new_row][end_column + 1].isdigit():
                                    end_column = end_column + 1

                                total = int(''.join(lst[new_row][start_column:end_column + 1]))
                                a.add(total)

                                for col in range(start_column, end_column + 1):
                                    part_nums.add((new_row, col))

                    length = len(a)

                    if length == 2:
                        ratio = math.prod(a)
                        calculated_sum = calculated_sum + ratio

        print(calculated_sum)


if __name__ == '__main__':
    main()
