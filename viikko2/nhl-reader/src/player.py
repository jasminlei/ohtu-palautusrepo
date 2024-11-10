class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.team = dict["team"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]
        self.nationality = dict["nationality"]

    def total_points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name.ljust(20)} {self.team}  {str(self.goals).rjust(2)} + {str(self.assists).rjust(2)} = {self.total_points()}"
