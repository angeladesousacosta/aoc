WORD_TO_NUM = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}


def main():
    with open('input/calibration.txt', 'r') as file:
        count = 0

        lines = file.readlines()

        for line in lines:
            matches = []

            length = len(line)

            for index in range(length):
                for word, digit in WORD_TO_NUM.items():
                    if line.startswith(word, index) or line[index] == digit:
                        pair = (index, digit)
                        matches.append(pair)

            matches.sort()

            first = matches[0][1] if matches else None
            last = matches[-1][1] if matches else None

            calculated_sum = int(first + last)
            count = count + calculated_sum

        print(count)


if __name__ == '__main__':
    main()
