class yahtzee:
    @staticmethod
    def chance(D1, D2, D3, D4, D5):
        total = 0
        total += d1
        total += d2
        total += d3
        total += d4
        total += d5
        return total


    @staticmethod
    def ones(D1, D2, D3, D4, D5):
        sum = 0
        if (D1 == 1):
            sum += 1
        if (D2 == 1):
            sum += 1
        if (D3 == 1):
            sum += 1
        if (D4 == 1):
            sum += 1
        if (D5 == 1): 
            sum += 1
        return sum

    @staticmethod
    def two (D1, D2, D3, D4, D5):
        sum = 0
        if (D1 == 2):
            sum += 2
        if (D2 == 2):
            sum += 2
        if (D3 == 2):
            sum += 2
        if (D4 == 2):
            sum += 2
        if (D5 == 2): 
            sum += 2
        return sum

    @staticmethod
    def three (D1, D2, D3, D4, D5):
        sum = 0
        if (D1 == 3):
            sum += 3
        if (D2 == 3):
            sum += 3
        if (D3 == 3):
            sum += 3
        if (D4 == 3):
            sum += 3
        if (D5 == 3): 
            sum += 3
        return sum