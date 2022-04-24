def count(expected, roll):
    return roll.count(expected)


def more_occurence(roll):
    return max(roll, key=roll.count)


def sum_is_valid(roll, required):
    maxNumber = more_occurence(roll)
    if count(maxNumber, roll) == required:
        if required == 5:
            return 50
        else:
            return sum(roll)
    else:
        return 0

class Yahtzee:
    @classmethod
    def turn(cls, roll, expected):
        if isinstance(expected, int):
            return count(expected, roll) * expected
        elif expected == "chance":
                return sum(roll)

        elif expected == "yahtzee":
            return sum_is_valid(roll,5)

        elif expected == "threeOfAKind":
            return sum_is_valid(roll, 3)

        elif expected == "fourOfAKind":
            return sum_is_valid(roll, 4)

        elif expected == "fullHouse":
            if count(more_occurence(roll), roll) == 3:
                cutted_roll = list(filter((more_occurence(roll)).__ne__, roll))
                if count(more_occurence(cutted_roll), cutted_roll) == 2:
                    return 25
            return 0


        elif expected == "smallStraight":
            possible = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
            sortRoll = sorted(roll)
            for i in possible:
                print(i, "  ", sortRoll)
                if all(elem in sortRoll for elem in i):
                    return 30
            return 0


        elif expected == "largeStraight":
            possible = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
            sortRoll = sorted(roll)
            if sortRoll == possible[0] or sortRoll == possible[1]:
                return 40
            else:
                return 0