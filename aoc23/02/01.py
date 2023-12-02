CONFIG = {'red': 12, 'green': 13, 'blue': 14}

def main():
    with open('input/record.txt', 'r') as file:
        good = {}

        lines = file.readlines()

        for index, line in enumerate(lines, 1):
            clean_list = line.replace(':', '').replace(';', '').replace(',', '')

            new_list = clean_list.split()

            numbers = new_list[2:]
            good[index] = []

            reversed_list = list(reversed(numbers))
            length = len(reversed_list)

            for i in range(0, length, 2):
                color = reversed_list[i]
                num = reversed_list[i + 1]
                good[index].append(int(num) <= CONFIG[color])

        total = []
        for k, v in good.items():
            if all(x is True for x in v):
                total.append(k)

        calculated_sum = sum(total)
        print(calculated_sum)


if __name__ == '__main__':
    main()
