from flask import Flask, render_template
from flask_ask import Ask, question, statement
from calendar_scraper import CalendarParser

app = Flask(__name__)

ask = Ask(app, route='/')

print("In main module")

@ask.launch
def starting_point():
    print("Launch function invoked")
    welcome_msg = render_template('welcome', firstname='you')
    return question(welcome_msg)

@ask.intent('YesIntent')
def yes_intent():
    cp = CalendarParser()
    events = cp.get_events()
    # stmt = ", ".join(event.get('title') for event in events)
    stmt = ", ".join(render_template('event', title=event.get('title'), date=event.get('date_and_place')) for event in events)
    print(stmt)
    return statement(stmt)

@ask.intent('NoIntent')
def no_intent():
    return statement("This is the No Intent")


if __name__ == '__main__':
    app.run(debug=True)

