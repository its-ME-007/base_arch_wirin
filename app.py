# app.py

from threading import Thread
from flask import Flask, jsonify
from lighting_ac import lighting_bp
from maps import mapping_bp

def create_main_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the Modular Request Resolver API",
            "endpoints": [
                "/lighting/set",
                "/lighting/get", 
                "/mapping/directions?origin=<origin>&destination=<destination>", 
                "/lighting/get"
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


def run_service(app, port):
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main_app = create_main_app()
    lighting_app = create_lighting_app()
    mapping_app = create_mapping_app()

    main_thread = Thread(target=run_service, args=(main_app, 5000))
    lighting_thread = Thread(target=run_service, args=(lighting_app, 5001))
    mapping_thread = Thread(target=run_service, args=(mapping_app, 5002))

    main_thread.start()
    lighting_thread.start()
    mapping_thread.start()


    main_thread.join()
    lighting_thread.join()
    mapping_thread.join()
