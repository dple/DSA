if __name__ == '__main__':
    N = int(input().strip())
    time = 0
    list_of_friend_time = []
    list_of_friends = []
    wait_time = []
    for _ in range(N):
        c, n = input().split()
        if c == 'W':
            time = time + int(n) - 1
        else:
            if n not in list_of_friends:
                list_of_friends.append(n)
            list_of_friend_time.append({n : time})
            time += 1

    # Dictionary of friends and their corresponding messages' timing
    dict_friend_times = {}
    for friend_time in list_of_friend_time:
        for friend in friend_time:
            if friend in dict_friend_times.keys():
                # add a timing of received/sent message to the list of [friend]
                dict_friend_times[friend].append(friend_time[friend])
            else:
                # initiate a list of messages' timing. Each friend has a list
                dict_friend_times[friend] = [friend_time[friend]]

    # printing result
    list_of_friends.sort()
    for friend in list_of_friends:
        # Get the list of messages' timing of friend [friend]
        times = dict_friend_times[friend]
        if len(times) % 2 == 1:
            print(friend + " -1")
        else:
            print(friend, sum((times[i + 1] - times[i]) for i in range(0, len(times), 2)))