from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

def fetch_prayer_times_by_city(year, month, city, country):
    try:
        url = f"http://api.aladhan.com/v1/calendarByCity/{year}/{month}"
        params = {
            'city': city,
            'country': country,
            
        }

        response = requests.get(url, params=params)
        prayer_times_data = response.json()

        if "data" in prayer_times_data:
            return prayer_times_data["data"]
        else:
            return None

    except Exception as e:
        return f"Unexpected error occurred: {e}"

@app.route('/calendar-by-city', methods=['GET'])
def get_prayer_times_by_city():
    """
    Retrieve prayer times for a specific calendar month by city
    ---
    parameters:
      - name: year
        in: query
        type: integer
        required: true
      - name: month
        in: query
        type: integer
        required: true
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
    try:
        year = int(request.args.get('year'))
        month = int(request.args.get('month'))
        city = request.args.get('city')
        country = request.args.get('country')

        prayer_times = fetch_prayer_times_by_city(year, month, city, country)
        return jsonify(prayer_times)

    except Exception as e:
        return jsonify({"error": f"Unexpected error occurred: {e}"}), 500
    
if __name__ == "__main__":
    app.run(debug=True, port=3000)
