import requests
from player import Player
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("Players from FIN" + str(datetime.now()))

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )
        if player_dict['nationality'] == 'FIN':
            players.append(player)

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
