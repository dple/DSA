if __name__ == '__main__':
    N = int(input())

    output = []
    for _ in range(N):
        line = input()
        count = 1
        c = line[0]
        encoded_line = ''
        for v in line[1:]:
            if v == c:
                count += 1
            else:
                encoded_line = encoded_line + str(count) + " " + c + " "
                c, count = v, 1
        encoded_line = encoded_line + str(count) + " " + c + " "

        output.append(encoded_line)
        encoded_line = ''

    for line in output:
        print(line)