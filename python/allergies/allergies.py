from itertools import combinations
class Allergies:


    def __init__(self, score: int):
        self.allergie_collection = \
            {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8, 'tomatoes': 16, 'chocolate': 32, 'pollen': 64,
             'cats': 128,}
        self.score = score

    def allergic_to(self, item: str):
        for i in range(1, len(self.allergie_collection) + 1):
            for combo in combinations(self.allergie_collection.values(), i):
                if sum(combo) == self.score and self.allergie_collection[item] in combo:
                    return True
                else:
                    continue
        return False

    @property
    def lst(self):
        answer = []
        counter = 0
        sorted_allergic_collection = sorted(self.allergie_collection.items(), key=lambda x: x[1])
        print(sorted_allergic_collection)
        while counter < self.score:
            for k, v in sorted_allergic_collection:
                answer.append(k)
                counter += v
        return answer

