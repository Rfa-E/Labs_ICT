# Deliverables Session 06 - Rafael Antonio Echevarria Silva
# Exercise 5:
#To add a form that allows us to enter some text and send it to the API
# • Use input elements and submit button.
# • Create new endpoint /showtext that capture the text sent with the form and writes it to the console with a print()
from flask import Flask, render_template, request
import sqlite3
from sense_hat import SenseHat
import random

sense = SenseHat()

def random_colour():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/showtext', methods=['POST'])
def showtext():
    user_input = request.form.get('usertext')
    rand = random_colour()
    print(f"Received text from form: {user_input}")
    print(f"<h1>You sent: {user_input}</h1><p>Check the server console for the printed text.</p>")
# ¿Can we write it to the LED matrix? ¿Can we also add another input to select the color?
    sense.show_message(user_input, text_colour = rand, back_colour = (0,0,0))
    return render_template('main.html')