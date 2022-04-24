def count(expected, roll):
    return roll.count(expected)


def more_occurence(roll):
    return max(roll, key=roll.count)


class Yahtzee:
    @classmethod
    def turn(cls, roll, expected):
        if isinstance(expected, int):
            return count(expected, roll) * expected
        elif expected == "chance":
                return sum(roll)

        elif expected == "yahtzee":
            maxNumber = more_occurence(roll)
            if count(maxNumber, roll) == 5:
                return 50
            else:
                return 0