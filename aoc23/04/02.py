def main():
    with open('input/scratchcards.txt', 'r') as file:
        lines = file.readlines()

        card_copies = [1] * len(lines)

        total = 0

        for index, line in enumerate(lines):
            clean_list = line.replace(':', '').replace('|', '')
            new_list = clean_list.split()

            numbers = new_list[2:]
            complete_list = [int(i) for i in numbers]

            winning_cards = complete_list[0:10]
            hand_cards = complete_list[10:35]

            matching = []

            for win in winning_cards:
                if win in hand_cards:
                    matching.append(win)

            for i in range(1, len(matching) + 1):
                if index + i < len(lines):
                    card_copies[index + i] = card_copies[index + i] + card_copies[index]

            total = total + card_copies[index]

        print(total)

if __name__ == '__main__':
    main()
