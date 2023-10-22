from itertools import combinations

def triplets_with_sum(number: int) -> list[list[int]]:
    return [[a, b, c] for a in range(number // 3) if (number ** 2 - 2 * number * a) % (2 * (number - a)) == 0 and a < (
        b := (number ** 2 - 2 * number * a) / (2 * (number - a))) < (c := (number - a - b))]

