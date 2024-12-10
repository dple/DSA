# Silent Auction
if __name__ == '__main__':
    n = int(input())        # Get the number of auctioners
    winner = 0
    winner_name = ''
    for _ in range(n):
        name = input()
        bid = int(input())
        if bid > winner:
            winner = bid
            winner_name = name

    # Print the winner
    print(winner_name)