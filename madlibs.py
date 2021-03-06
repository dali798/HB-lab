"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """ """

    answer = request.args.get("want_play")
    # if answer == "Yes":
    #     return render_template("game.html")
    # else:
    #     return render_template("goodbye.html")

    webpage_name = "game.html" if answer == "yes" else "goodbye.html"
    return render_template(webpage_name)
    
@app.route("/madlib")
def show_madlib():
    color = request.args.get("color")
    character = request.args.get("char")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")  
    adjectives = request.args.getlist("adjective1")
    adjective1 = choice(adjectives)
    
    print("***********************************************")
    print(f"adjectives = {adjectives}")
    print(f"adjective1 {adjective1}")
    # print(f"\n request.args = {request.args} \n")
    # print(f"adjectives = {adjectives}")
    webpage_name = choice(["madlib.html", "madlib1.html", "madlib2.html"])

    return render_template(webpage_name, color = color, character = character, noun = noun, adjective = adjective, adjective1 = adjective1)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
