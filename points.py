class points():
    def __init__(self, dice):
        self.dice = dice
        self.counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.combinations = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    # Setters
    def set_dice(self, dice):
        self.dice = dice

    # Supporting functions
    def dice_sum(self):
        return sum(self.dice)

    def count_dice(self):
        for i in range(0,5):
            self.counts[self.dice[i]] += 1

    def get_max(self):
        values = list(self.counts.values())
        return max(values)

    # Getting scores for combinations
    def upper_section(self):
        for x in range(6):
            self.combinations[x] = self.counts[x+1] * (x + 1)

    def three_of_a_kind(self):
        if self.get_max() >= 3:
            self.combinations[6] = self.dice_sum()

    def four_of_a_kind(self):
        if self.get_max() >= 4:
            self.combinations[7] = self.dice_sum()

    def full_house(self):
        if 3 in self.counts.values() and 2 in self.counts.values():
            self.combinations[8] = 25

    def small_straight(self):
        values = list(self.counts.values())
        if values[1] >= 1 and values[2] >= 1 and values[3] >= 1 and values[4] >= 1:
            self.combinations[9] = 30
        elif values[2] >= 1 and values[3] >= 1 and values[4] >= 1 and values[5] >= 1:
            self.combinations[9] = 30
        elif values[0] >= 1 and values[1] >= 1 and values[2] >= 1 and values[3] >= 1:
            self.combinations[9] = 30

    def large_straight(self):
        values = list(self.counts.values())
        if values[1] >= 1 and values[2] >= 1 and values[3] >= 1 and values[4] >= 1 and values[5] >= 1:
            self.combinations[10] = 40
        elif values[0] >= 1 and values[1] >= 1 and values[2] >= 1 and values[3] >= 1 and values[4] >= 1:
            self.combinations[10] = 40

    def chance(self):
        self.combinations[11] = self.dice_sum()

    def yahtzee(self):
        if 5 in self.counts.values():
            self.combinations[12] = 50

    # Calculate scores for each combination
    def calculate_combinations(self):
        self.count_dice()
        self.upper_section()
        self.three_of_a_kind()
        self.four_of_a_kind()
        self.full_house()
        self.small_straight()
        self.large_straight()
        self.chance()
        self.yahtzee()

    # Getters
    def get_combinations(self):
        return self.combinations

    def get_counts(self):
        return self.counts