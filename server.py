from flask import Flask, render_template
from dice import dice
from gamecontroller import gamecontroller
from points import points
app = Flask(__name__)
mydice = dice()
gc = gamecontroller(mydice)
names = ["Ones","Twos","Threes","Fours","Fives","Sixes","Three of a Kind","Four of a Kind","Full House",
         "Small Straight","Large Straight","Chance","YAHTZEE"]
combos = []

@app.route('/')
def home():
    return render_template('index.html', mydice=mydice.get_numbers(), names=names, gc=gc)

@app.route('/roll_all_button_action', methods=['POST'])
def roll_all_button_action():
    # This is the function that gets triggered by the roll button.
    gc.roll()
    p = points(gc.dice.get_numbers())
    p.calculate_combinations()
    combos = p.get_combinations()
    gc.set_current_points(combos)
    gc.ey_check()

    return render_template('index.html', mydice=mydice.get_numbers(), names=names, gc=gc, combos=combos)


# Responses to which dice to keep / roll
@app.route('/keep_button_action/<int:button_id>', methods=['POST'])
def keep_button_action(button_id):
    gc.set_keep(button_id)
    return render_template('index.html', mydice=mydice.get_numbers(), names=names, gc=gc, combos=gc.current_points)

@app.route('/roll_button_action/<int:button_id>', methods=['POST'])
def roll_button_action(button_id):
    gc.set_roll(button_id)
    return render_template('index.html', mydice=mydice.get_numbers(), names=names, gc=gc, combos=gc.current_points)

# Responses to which combination to choose
def update_scores(num):
    # Updates the score-card
    combos = gc.current_points
    gc.set_done(num)
    gc.set_score(num, combos[num])

@app.route('/choose_button_action/<int:button_id>', methods=['POST'])
def choose_button_action(button_id):
    update_scores(button_id)
    gc.ey = False
    return render_template('index.html', mydice=mydice.get_numbers(), names=names, gc=gc, combos=combos)

# Run server
if __name__ == '__main__':
    app.run(debug=True)