import requests
from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_cors import CORS


app = Flask(__name__)
swagger = Swagger(app)
CORS(app)

def fetch_prayer_times(city, country):
    try:
        url = f"http://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method=2"
        response = requests.get(url)
        info = response.json()

        if "data" in info:
            timing = info["data"][0]["timings"]
            return timing
        else:
            return None

    except Exception as e:
        return f"Unexpected error occurred: {e}"

@app.route('/prayer-times', methods=['GET'])
def get_prayer_times():
    """
    Retrieve prayer times for a specific location
    ---
    parameters:
      - name: city
        in: query
        type: string
        required: true
      - name: country
        in: query
        type: string
        required: true
    responses:
      200:
        description: Prayer times successfully retrieved
    """
    city = request.args.get('city')
    country = request.args.get('country')
    prayer_timings = fetch_prayer_times(city, country)