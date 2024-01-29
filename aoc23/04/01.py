def main():
    with open('input/scratchcards.txt', 'r') as file:
        lines = file.readlines()

        total = 0

        for line in lines:
            clean_list = line.replace(':', '').replace('|', '')
            new_list = clean_list.split()

            numbers = new_list[2:]
            complete_list = [int(i) for i in numbers]

            winning_cards = complete_list[0:10]
            hand_cards = complete_list[10:35]

            matching = []

            for win in winning_cards:
                for hand in hand_cards:
                    if win == hand:
                        matching.append(win)

            length = len(matching)

            if length == 0:
                total = total + 0
            elif length == 1:
                total = total + 1
            else:
                total = total + 2 ** (length - 1)

        print(total)


if __name__ == '__main__':
    main()
