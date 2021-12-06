
class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.p1_score = 0
        self.p2_score = 0
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player):
        if player == self.player1:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def player_score(self, score):
        return self.scores[score]

    def final_score(self):
        result = self.p1_score - self.p2_score
        if result == 1:
            return "Advantage " + self.player1
        if result == -1:
            return "Advantage " + self.player2
        if result > 1:
            return "Win for " + self.player1
        return "Win for " + self.player2
        
    def get_score(self):
        if self.p1_score == self.p2_score:
            if self.p1_score < 4:
                return self.player_score(self.p1_score)+"-All"
            return "Deuce"
            
        if self.p1_score >= 4 or self.p2_score >= 4:
            return self.final_score()
        
        return self.player_score(self.p1_score) + "-" + self.player_score(self.p2_score)