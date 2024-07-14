from flask import render_template
from flask import current_app as app
from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='static')

    from blackjack import BlackjackGame
    game = BlackjackGame()

    @app.route("/")
    def home_route():
        game.start_game()
        return render_template("home.html", game_state=game.get_game_state())

    @app.route("/hit")
    def hit():
        game.hit()
        return render_template("home.html", game_state=game.get_game_state())

    @app.route("/stand")
    def stand():
        game.stand()
        return render_template("home.html", game_state=game.get_game_state())

    @app.route("/new_game")
    def new_game():
        game.start_game()
        return render_template("home.html", game_state=game.get_game_state())

    return app