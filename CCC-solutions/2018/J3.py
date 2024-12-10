def distance(i, j, d):
    if i == j:
        return 0
    m = min(i, j)
    M = max(i, j)
    return sum(d[m + i] for i in range(M - m))


if __name__ == '__main__':
    inputs = list(map(int, input().split()))  # distances between consecutive pairs of consecutive cities
    n = len(inputs) + 1  # number of cities
    distances = []  # distances from city i to other cities

    for i in range(n):
        for j in range(n):
            distances.append(distance(i, j, inputs))
        print(*distances)
        distances = []
