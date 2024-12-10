# Fergusonball Ratings
if __name__ == '__main__':
    n = int(input())    # get number of players
    count = 0           # count the number of players rating greater than 40
    for i in range(n):
        points = int(input())
        fouls = int(input())
        stars = points*5 - fouls*3
        if stars > 40:
            count += 1

    if count == n:          # gold team where all players rating > 40
        print(count, end="")
        print('+')
    else:
        print(count)