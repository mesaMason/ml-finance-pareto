import argparse
from random import randint

class Player:

    def __init__(self, id_num, dollars):
        self.id_num = id_num
        self.dollars = dollars
    

def update(players):
    p1 = players.pop()
    p2 = players.pop()
    r = randint(0, 1)

    if r == 0:
        print(f"Player {p2.id_num} won")
        p1.dollars = p1.dollars - 1
        p2.dollars = p2.dollars + 1
    else:
        print(f"Player {p1.id_num} won")
        p1.dollars = p1.dollars + 1
        p2.dollars = p2.dollars - 1

    print(f"Player {p1.id_num} money: {p1.dollars}; player {p2.id_num} money: {p2.dollars}")
    if p1.dollars > 0:
        players.append(p1)
    if p2.dollars > 0:
        players.append(p2)
    return 

def main():
    parser = argparse.ArgumentParser(description='Pareto Equilibrium Game')
    parser.add_argument("-n",
                        "--num_players",
                        required=True,
                        type=int,
                        help='Number of players')
    parser.add_argument("-d",
                        '--dollars',
                        required=True,
                        type=int,
                        help='Number of dollars per player')
    args = parser.parse_args()
    num_players = args.num_players
    dollars = args.dollars
    players = []
    for i in range(num_players):
        players.append(Player(i, dollars))
        print(f"Adding player: {i} with money: {dollars}")

    while len(players) > 1:
        update(players)

    winner = players.pop()
    print(f"Winner: {winner.id_num}; money: {winner.dollars}")
    return 

if __name__ == '__main__':
    main()
