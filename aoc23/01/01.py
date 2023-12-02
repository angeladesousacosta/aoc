def main():
    with open('input/calibration.txt', 'r') as file:
        count = 0

        lines = file.readlines()

        for line in lines:
            numbers = [num for num in line if num.isdigit()]

            first = numbers[0]
            last = numbers[-1]

            calculated_sum = int(first + last)
            count = count + calculated_sum

        print(count)
          

if __name__ == '__main__':
    main()
