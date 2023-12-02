def main():
    with open('input/record.txt', 'r') as file:
        total_list = []

        lines = file.readlines()

        for index, line in enumerate(lines, 1):
            clean_list = line.replace(':', '').replace(';', '').replace(',', '')

            new_list = clean_list.split()

            numbers = new_list[2:]

            reversed_list = list(reversed(numbers))
            length = len(reversed_list)
            my_dict = {}

            for i in range(0, length, 2):
                color = reversed_list[i]
                num = int(reversed_list[i + 1])

                if color in my_dict:
                    my_dict[color].append(num)
                else:
                    my_dict[color] = [num]

            max_num = {color: max(num) for color, num in my_dict.items()}

            total = 1

            for i in max_num:
                total = total * int(max_num[i])

            total_list.append(total)

        calculated_sum = sum(total_list)
        print(calculated_sum)


if __name__ == '__main__':
    main()
