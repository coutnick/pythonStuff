from flask import Flask, abort, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    phrases: list[str] = ['Welcome to this page!', 'You are looking good today!', 'The wheather is great!']
    return {'phrase': choice(phrases),
            'date': datetime.now()}

@app.route('/api/random')
def random():
    number_input = request.args.get('number', type=int)
    text_input = request.args.get('text', type=str, default='default_text')

    if isinstance(number_input, int):
        return{
            'input': number_input,
            'random': randint(0, number_input),
            'text': text_input,
            'date': datetime.now()
        }
    else:
        abort(400,"Error: please enter a valid number")

if __name__ == '__main__':
    app.run()