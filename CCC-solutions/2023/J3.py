if __name__ == '__main__':
    N = int(input().strip())
    no_attendance = [0, 0, 0, 0, 0]

    for _ in range(N):
        s = input().strip()
        for i in range(5):
            if s[i] == 'Y':
                no_attendance[i] += 1

    max_attendances = max(no_attendance)
    days = []

    for i in range(5):
        if no_attendance[i] == max_attendances:
            days.append(i + 1)

    for d in days[:-1]:
        print(str(d) + ',', end="")
    print(days[-1])