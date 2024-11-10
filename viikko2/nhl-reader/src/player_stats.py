class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = []
        for player in self.players:
            if player.nationality == nationality:
                filtered_players.append(player)

        filtered_players.sort(key=lambda player: player.total_points(), reverse=True)

        return filtered_players
