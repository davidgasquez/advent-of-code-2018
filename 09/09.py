from collections import deque


def play_game(num_players, num_marbles):
    players_scores = [0] * num_players
    circle = deque([0])

    for marble in range(1, num_marbles + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            players_scores[marble % num_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(players_scores)


with open("input.txt") as f:
    words = f.readline().split()

players = int(words[0])
marbles = int(words[6])


print(play_game(players, marbles))
print(play_game(players, marbles * 100))
