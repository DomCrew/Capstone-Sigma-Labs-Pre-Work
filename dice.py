import random

def roll_all():
    dice = []
    for i in range(1, 6):
        dice.append(random.randint(1, 6))
    return dice
class dice():
    def __init__(self):
        self.dice = roll_all()

    def roll_one(self,num):
        self.dice[num] = random.randint(1, 6)

    def get_numbers(self):
        return self.dice