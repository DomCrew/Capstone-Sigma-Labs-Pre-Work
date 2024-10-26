class gamecontroller:
    def __init__(self, dice):
        self.dice = dice
        self.turn = 0
        self.rolls = 3
        self.scores = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.current_points = []
        self.done = [False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.keeping = [False, False, False, False, False]
        self.buttons_available = [True,True,True]
        self.ey = False

    def get_total_score(self):
        upper_section = self.scores[:6]
        total = sum(self.scores)
        if sum(upper_section) >= 63:
            total += 35
        return total

    def ey_check(self):
        numbers = self.dice.get_numbers()
        if numbers.count(numbers[0]) == len(numbers) and self.done[12] and self.scores[12] !=0:
            self.scores[12] += 100
            self.rolls = 0
            if not self.done[numbers[0] - 1]:
                self.done[numbers[0] - 1] = True
                self.scores[numbers[0] - 1] = numbers[0] * 5
                self.turn_function()
            elif (not self.done[6] or not self.done[7] or not self.done[11]):
                if self.done[6]:
                    self.buttons_available[0] = False
                if self.done[7]:
                    self.buttons_available[1] = False
                if self.done[11]:
                    self.buttons_available[2] = False
                self.ey = True


    def turn_function(self):
        self.rolls = 3
        self.turn += 1
        self.keeping = [False, False, False, False, False]

    def roll(self):
        self.ey = False
        self.rolls -= 1
        for i,keep in enumerate(self.keeping):
            if not keep:
                self.dice.roll_one(i)

    def set_current_points(self, points):
        self.current_points = points

    def set_keep(self, num):
        self.keeping[num] = True

    def set_roll(self, num):
        self.keeping[num] = False

    def set_done(self, num):
        self.done[num] = True
        self.current_points = []
        self.turn_function()
        self.keeping = [False, False, False, False, False]

    def set_score(self, num, score):
        self.scores[num] = score

    # Getters

    def get_turn(self):
        return self.turn

    def get_rolls(self):
        return self.rolls

    def get_scores(self):
        return self.scores

    def get_done(self):
        return self.done

