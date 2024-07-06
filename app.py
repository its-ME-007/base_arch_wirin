from flask import Flask, jsonify
from maps import mapping
from song_player import song_player
from lighting_ac import lighting_ac

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(mapping)
app.register_blueprint(song_player)
app.register_blueprint(lighting_ac)

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Modular Request Resolver API",
        "endpoints": [
            "/mapping/directions?origin=<origin>&destination=<destination>",
            "/song/play",
            "/song/stop",
            "/lighting/set",
            "/ac/set",
            "/lighting/get",
            "/ac/get"
        ]
    })

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
