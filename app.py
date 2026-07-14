from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "my_secret_key"


def initialize_game(difficulty):
    """Initialize a new game."""

    ranges = {
        "easy": 10,
        "medium": 50,
        "hard": 100
    }

    session["difficulty"] = difficulty
    session["max_number"] = ranges[difficulty]
    session["secret_number"] = random.randint(1, ranges[difficulty])
    session["attempts"] = 0
    session["score"] = 100
    session["game_started"] = True
    session["game_over"] = False
    session["message"] = "Welcome! Start Guessing."


@app.route("/")
def home():

    if "game_started" not in session:
        session["game_started"] = False

    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():

    difficulty = request.form["difficulty"]

    initialize_game(difficulty)

    return redirect(url_for("home"))


@app.route("/guess", methods=["POST"])
def guess():

    if not session.get("game_started"):
        return redirect(url_for("home"))

    guess = int(request.form["guess"])

    session["attempts"] += 1

    if guess < session["secret_number"]:
        session["message"] = "⬇ Too Low!"
        session["score"] = max(0, session["score"] - 10)

    elif guess > session["secret_number"]:
        session["message"] = "⬆ Too High!"
        session["score"] = max(0, session["score"] - 10)

    else:
        # session["message"] = "🎉 Congratulations! You guessed correctly!"
        # session["game_over"] = True
        session["game_over"] = True

        session["message"] = (
            f"🎉 Congratulations! "
            f"You guessed {session['secret_number']} "
            f"in {session['attempts']} attempts. "
            f"Final Score: {session['score']}"
        )

    return redirect(url_for("home"))


@app.route("/play-again", methods=["POST"])
def play_again():

    difficulty = session["difficulty"]

    initialize_game(difficulty)

    return redirect(url_for("home"))


@app.route("/change-difficulty", methods=["POST"])
def change_difficulty():

    session.clear()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)