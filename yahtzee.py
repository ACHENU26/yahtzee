class yahtzee:
    
    def __init__(self, D1, D2, D3, D4, D5):
        self.dice = [0]*5
        self.dice[0] = D1
        self.dice[1] = D2
        self.dice[2] = D3
        self.dice[3] = D4
        self.dice[4] = D5

#### Upper section combinaisons
#ones
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

#twos
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

#threes
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

#fours
    def four(self):
        sum = 0
        i = 0
        for at in range(len(self.dice)):
            if (self.dice[i] == 4): 
                sum += 4
        return sum
    
#fives
    def five(self):
        sum = 0
        i = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                sum = sum + 5
        return sum
    
#sixes
    def sixe(self):
        sum = 0
        i = 0
        for at in range(len(self.dice)): 
            if (self.dice[i] == 6):
                sum = sum + 6
        return sum
 

#### Lower section combinations
# chance
    @staticmethod
    def chance(D1, D2, D3, D4, D5):
        total = 0
        total += d1
        total += d2
        total += d3
        total += d4
        total += d5
        return total
# yahtzee
    @staticmethod
    def yatzee(dice):
        counts = [0]*(len(dice)+1)
        for d in dice:
            counts[d-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
# fullHouse
    @staticmethod
    def fullHouse(D1, D2, D3, D4, D5):
        equivalent = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        equivalent = [0]*6
        equivalent[D1-1] += 1
        equivalent[D2-1] += 1
        equivalent[D3-1] += 1
        equivalent[D4-1] += 1
        equivalent[D5-1] += 1

        for i in range(6):
            if (equivalent[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (equivalent[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0

# three_kind
    @staticmethod
    def three_kind(D1, D2, D3, D4, D5):
        equivalent = [0]*6
        equivalent[D1-1] += 1
        equivalent[D2-1] += 1
        equivalent[D3-1] += 1
        equivalent[D4-1] += 1
        equivalent[D5-1] += 1
        for i in range(6):
            if (equivalent[i] >= 3):
                return (i+1) * 3
        return 0

# four_kind
    @staticmethod
    def four_kind(D1, D2, D3, D4, D5):
        equivalent = [0]*6
        equivalent[D1-1] += 1
        equivalent[D2-1] += 1
        equivalent[D3-1] += 1
        equivalent[D4-1] += 1
        equivalent[D5-1] += 1
        for i in range(6):
            if (equivalent[i] >= 4):
                return (i+1) * 4
        return 0

# small_straight

# large_straight

# one_pair

#two_pairs