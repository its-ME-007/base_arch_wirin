# mapping.py

from flask import Blueprint, jsonify, request

mapping_bp = Blueprint('mapping', __name__)

@mapping_bp.route('/mapping/directions', methods=['GET'])
def get_directions():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    if not origin or not destination:
        return jsonify({"error": "Origin and destination are required"}), 400
    directions = f"Directions from {origin} to {destination}"
    return jsonify({"directions": directions})
