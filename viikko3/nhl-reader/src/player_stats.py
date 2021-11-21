class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        filtered_players=[]
        for p in self._players:
            if p.nationality == nationality:
                filtered_players.append(p)
        filtered_players.sort(key=lambda x: x.goals + x.assists, reverse=True)
        return filtered_players
