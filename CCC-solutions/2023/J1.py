if __name__ == '__main__':
    P = int(input().strip())
    C = int(input().strip())
    score = P*50 - C*10
    if P > C:
        score += 500
    print(score)