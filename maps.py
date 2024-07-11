# from flask import Blueprint, render_template_string, request, jsonify

# mapping_bp = Blueprint('mapping', __name__)

# directions_html = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Google Maps Directions</title>
#     <style>
#         #map {
#             height: 80%;
#             width: 100%;
#         }
#         html, body {
#             height: 100%;
#             margin: 0;
#             padding: 0;
#         }
#     </style>
#     <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDqlgjgW4XiLsJM33jY8voBIjGUQswKd_I&callback=initMap" async defer></script>
#     <script>
#         let map;
#         function initMap() {
#             const origin = "{{ origin }}";
#             const destination = "{{ destination }}";
#             const directionsService = new google.maps.DirectionsService();
#             const directionsRenderer = new google.maps.DirectionsRenderer();
#             map = new google.maps.Map(document.getElementById("map"), {
#                 center: { lat: -34.397, lng: 150.644 },
#                 zoom: 6,
#             });
#             directionsRenderer.setMap(map);
#             calculateAndDisplayRoute(directionsService, directionsRenderer, origin, destination);
#         }

#         function calculateAndDisplayRoute(directionsService, directionsRenderer, origin, destination) {
#             directionsService.route(
#                 {
#                     origin: origin,
#                     destination: destination,
#                     travelMode: google.maps.TravelMode.DRIVING,
#                 },
#                 (response, status) => {
#                     if (status === "OK") {
#                         directionsRenderer.setDirections(response);
#                     } else {
#                         window.alert("Directions request failed due to " + status);
#                     }
#                 }
#             );
#         }
#     </script>
# </head>
# <body>
#     <div id="map"></div>
# </body>
# </html>
# """

# @mapping_bp.route('/mapping/directions', methods=['GET'])
# def get_directions():
#     origin = request.args.get('origin')
#     destination = request.args.get('destination')
#     if not origin or not destination:
#         return jsonify({"error": "Origin and destination are required"}), 400
#     return render_template_string(directions_html, origin=origin, destination=destination)
from flask import Flask, render_template, request, jsonify, Blueprint
import requests


mapping_bp = Blueprint('mapping', __name__)

MAPBOX_TOKEN = 'pk.eyJ1Ijoid2lwb2RydmNlIiwiYSI6ImNsdnVzN255YzE5MDYycm55c3hheDhtdTUifQ.lEWdCkssgxZWHlg0eGNkiw'

@mapping_bp.route('/')
def index():
    return render_template('index.html', mapbox_token=MAPBOX_TOKEN)

@mapping_bp.route('/geocode')
def geocode():
    address = request.args.get('address')
    response = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={MAPBOX_TOKEN}')
    data = response.json()
    coordinates = data['features'][0]['geometry']['coordinates']
    print(coordinates)
    return jsonify({'coordinates': coordinates})

@mapping_bp.route('/directions')
def directions():
    start = request.args.get('start')
    end = request.args.get('end')
    response = requests.get(f'https://api.mapbox.com/directions/v5/mapbox/driving/{start};{end}?geometries=geojson&overview=full&steps=true&access_token={MAPBOX_TOKEN}')
    data = response.json()
    route = data['routes'][0]['geometry']
    return jsonify({'route': route})



