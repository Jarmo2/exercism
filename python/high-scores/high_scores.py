class HighScores:
    def __init__(self, scores: list[int]):
        self.scores = []
        self.scores.extend(scores)
       
    def personal_top_three(self) -> list[int]:
        return sorted(self.scores, reverse=True)[:3]

    def latest(self) -> int:
        return self.scores[-1]

    def personal_best(self) -> int:
        return sorted(self.scores, reverse=True)[:1][0]
    
    
