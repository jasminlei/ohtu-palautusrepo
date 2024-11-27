class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    WIN_SCORE = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._tie_score()
        elif (
            self.player1_score >= self.WIN_SCORE or self.player2_score >= self.WIN_SCORE
        ):
            return self._advantage_or_win_score()
        else:
            return self._regular_score()

    def _tie_score(self):
        if self.player1_score < 3:
            return f"{self.SCORE_NAMES[self.player1_score]}-All"
        else:
            return "Deuce"

    def _advantage_or_win_score(self):
        score_diff = self.player1_score - self.player2_score
        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        elif score_diff == -1:
            return f"Advantage {self.player2_name}"
        elif score_diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _regular_score(self):
        return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"
