from threading import Thread
from flask import Flask, jsonify
from lighting_ac import lighting_bp
from maps import mapping_bp
from ac import ac_bp
from door import door_bp
from sound import sound_bp


def create_main_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the Modular Request Resolver API",
            "endpoints": [
                "5001/lighting/set",
                "5001/lighting/get",
                "5002/mapping/directions?origin=<origin>&destination=<destination>",
                "5003/ac/set",
                "5003/ac/get",
                "5004/sound/set",
                "5004/sound/get"
            ]
        })

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"error": "Page not found"}), 404

    return app

def create_lighting_app():
    app = Flask(__name__)
    app.register_blueprint(lighting_bp, url_prefix='/api')
    return app

def create_mapping_app():
    app = Flask(__name__)
    app.register_blueprint(mapping_bp, url_prefix='/api')
    return app

def create_ac_app():
    app = Flask(__name__)
    app.register_blueprint(ac_bp, url_prefix='/api')
    return app

def create_door_app():
    app = Flask(__name__)
    app.register_blueprint(door_bp, url_prefix='/api')
    return app

def create_sound_app():
    app = Flask(__name__)
    app.register_blueprint(sound_bp, url_prefix='/api')
    return app

def run_service(app, port):
    try:
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        print(f"Error running service on port {port}: {e}")

if __name__ == '__main__':
    main_app = create_main_app()
    lighting_app = create_lighting_app()
    mapping_app = create_mapping_app()
    ac_app = create_ac_app()
    door_app = create_door_app()
    sound_app = create_sound_app()

    main_thread = Thread(target=run_service, args=(main_app, 5000))
    lighting_thread = Thread(target=run_service, args=(lighting_app, 5001))
    mapping_thread = Thread(target=run_service, args=(mapping_app, 5002))
    ac_thread = Thread(target=run_service, args=(ac_app, 5003))
    door_thread = Thread(target=run_service, args=(door_app, 500))
    sound_thread = Thread(target=run_service, args=(sound_app, 5004))

    main_thread.start()
    lighting_thread.start()
    mapping_thread.start()
    ac_thread.start()
    door_thread.start()
    sound_thread.start()

    main_thread.join()
    lighting_thread.join()
    mapping_thread.join()
    ac_thread.join()
    door_thread.join()
    sound_thread.join()


