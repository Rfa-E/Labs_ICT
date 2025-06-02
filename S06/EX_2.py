# Deliverables Session 06 - Rafael Antonio Echevarria Silva
# Exercise 2: Write a home web page using templates with Flask in the “/” resource
# • It should include the same information as in exercise 1.
# • It should accept a parameter in the url called “group” and it will be shown on the page as Heading and title.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('group')
    return render_template('hello.html', name = name)