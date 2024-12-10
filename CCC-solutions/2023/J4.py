if __name__ == '__main__':
    C = int(input().strip())
    first_line = input().strip()
    second_line = input().strip()
    previous_first = '0'
    previous_second = '0'
    count = 0

    for i in range(2 * C - 1):
        if first_line[i] != ' ':
            if first_line[i] == '1':
                if previous_first == '1':
                    count += 1
                else:
                    count += 3

                if second_line[i] == '1':
                    if previous_second == '1':
                        count -= 1
                    else:
                        count += 1

            else:
                if second_line[i] == '1':
                    if previous_second == '1':
                        count += 1
                    else:
                        count += 3

            previous_first = first_line[i]
            previous_second = second_line[i]

    print(count)
