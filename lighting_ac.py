from flask import Blueprint, jsonify, request

lighting_ac = Blueprint('lighting_ac', __name__)

# Assuming you have a way to store the current lighting intensity and AC temperature
current_lighting_intensity = 0
current_ac_temperature = 0

@lighting_ac.route('/lighting/set', methods=['POST'])
def set_lighting():
    global current_lighting_intensity
    data = request.json
    intensity = data.get('intensity')
    if intensity is None:
        return jsonify({"error": "Lighting intensity is required"}), 400
    current_lighting_intensity = intensity
    result = f"Setting lighting intensity to {intensity}"
    return jsonify({"result": result})

@lighting_ac.route('/lighting/get', methods=['GET'])
def get_lighting():
    global current_lighting_intensity
    result = f"Current lighting intensity is {current_lighting_intensity}"
    return jsonify({"result": result})

@lighting_ac.route('/ac/set', methods=['POST'])
def set_ac():
    global current_ac_temperature
    data = request.json
    temperature = data.get('temperature')
    if temperature is None:
        return jsonify({"error": "AC temperature is required"}), 400
    current_ac_temperature = temperature
    result = f"Setting AC temperature to {temperature}°C"
    return jsonify({"result": result})

@lighting_ac.route('/ac/get', methods=['GET'])
def get_ac():
    global current_ac_temperature
    result = f"Current AC temperature is {current_ac_temperature}°C"
    return jsonify({"result": result})