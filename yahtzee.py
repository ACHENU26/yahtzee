def count(expected, roll):
    return roll.count(expected)


def more_occurence(roll):
    return max(roll, key=roll.count)


def sum_if_valid(roll, required):
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
        else:
            if expected == "chance":
                return sum(roll)