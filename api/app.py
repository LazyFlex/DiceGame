from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dictionary to store player information and scores
players = {
    'player1': {'name': '', 'score': 0},
    'player2': {'name': '', 'score': 0},
}

# Variable to keep track of the current player
current_player = 'player1'


def roll_dice():
    import random
    return random.randint(1, 6)


@app.route('/')
def index():
    dice_value = str(roll_dice())

    return render_template('index.html', player1=players['player1'], player2=players['player2'],
                           current_player=current_player, dice_value=dice_value)


@app.route('/play', methods=['POST'])
def play():
    global current_player
    choice = request.form.get('choice')
    dice_value = 0

    if choice == 'roll':
        dice_value = roll_dice()
        if dice_value == 1:
            players[current_player]['score'] = 0
            current_player = 'player2' if current_player == 'player1' else 'player1'
        else:
            players[current_player]['score'] += dice_value
    elif choice == 'hold':
        current_player = 'player2' if current_player == 'player1' else 'player1'

    # Check for a winner
    if any(player['score'] >= 20 for player in players.values()):
        winner = max(players, key=lambda k: players[k]['score'])
        return render_template('winner.html', winner=players[winner]['name'])

    return render_template('index.html', player1=players['player1'], player2=players['player2'],
                           current_player=current_player, dice_value=dice_value)

@app.route('/new_game', methods=['POST'])
def new_game():
    global current_player
    players['player1']['name'] = request.form.get('player1')
    players['player2']['name'] = request.form.get('player2')
    players['player1']['score'] = 0
    players['player2']['score'] = 0
    current_player = 'player1'
    return redirect('/')

if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=8080)
     app.run(debug=True)
