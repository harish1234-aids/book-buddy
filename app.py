from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/word-search')
def word_search():
    return render_template('word_game.html')

@app.route('/logic-riddle')
def logic_riddle():
    return render_template('riddle_game.html')

@app.route('/unscrubble')
def jumbled_words():
    return render_template('jumble_game.html')

@app.route('/need-vs-want')
def need_challenge():
    return render_template('need_game.html')

@app.route('/money-magic')
def money_challenge():
    return render_template('money_game.html')

if __name__ == '__main__':
    app.run(debug=True)