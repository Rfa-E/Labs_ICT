# Deliverables Session 06 - Rafael Antonio Echevarria Silva
# Exercise 1: HTML With Flask
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def main():
   return render_template('main.html')
