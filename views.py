import random

from flask import Flask
from flask import request

app = Flask(__name__)


MAGIC_8_BALL = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

@app.route('/', methods=['POST'])
def bot():
    data = request.json

    matin_text = data.get('text', '')
    bot_text = random.choice(MAGIC_8_BALL)

    final_text = "you said " + matin_text + ". " + bot_text

    return {'text': final_text}
