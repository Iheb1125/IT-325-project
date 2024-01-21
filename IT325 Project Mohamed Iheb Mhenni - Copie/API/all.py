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
    return jsonify(prayer_timings)
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

def fetch_quran_page(page, edition, offset=None, limit=None):
    try:
        url = f"http://api.alquran.cloud/v1/page/{page}/{edition}"
        params = {'offset': offset, 'limit': limit}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            page_data = response.json()
            return page_data
        else:
            return f"Error: Unable to fetch Quran page data. Status code: {response.status_code}"

    except Exception as e:
        return f"Unexpected error occurred: {e}"

def fetch_sajda_ayahs(edition):
    try:
        url = f"http://api.alquran.cloud/v1/sajda/{edition}"
        response = requests.get(url)
        
        if response.status_code == 200:
            sajda_data = response.json()
            return sajda_data
        else:
            return f"Error: Unable to fetch sajda ayahs data. Status code: {response.status_code}"

    except Exception as e:
        return f"Unexpected error occurred: {e}"

def fetch_asma_al_husna(names):
    try:
        url = f"http://api.aladhan.com/v1/asmaAlHusna/{names}"
        response = requests.get(url)
        
        if response.status_code == 200:
            asma_al_husna_data = response.json()
            return asma_al_husna_data
        else:
            return f"Error: Unable to fetch Asma Al Husna data. Status code: {response.status_code}"

    except Exception as e:
        return f"Unexpected error occurred: {e}"

def get_quran_edition(edition):
    try:
        url = f"http://api.alquran.cloud/v1/quran/{edition}"
        response = requests.get(url)
        if response.status_code == 200:
            quran_data = response.json()
            return quran_data
        else:
            return f"Error: Unable to fetch Quran data. Status code: {response.status_code}"

    except Exception as e:
        return f"Unexpected error occurred: {e}"

@app.route('/quran-page', methods=['GET'])
def quran_page():
    """
    Retrieve a page from a particular Quran edition
    ---
    parameters:
      - name: page
        in: query
        type: integer
        required: true
        description: The page number.
        example: 1
      - name: edition
        in: query
        type: string
        required: true
        description: A Quran edition identifier.
        example: en.asad
      - name: offset
        in: query
        type: integer
        required: false
        description: Offset ayahs in a page by the given number.
      - name: limit
        in: query
        type: integer
        required: false
        description: The number of ayahs that the response will be limited to.
    
    responses:
      200:
        description: Quran page successfully retrieved
    """
    try:
        page = int(request.args.get('page'))
        edition = request.args.get('edition')
        offset = request.args.get('offset', default=None, type=int)
        limit = request.args.get('limit', default=None, type=int)

        page_data = fetch_quran_page(page, edition, offset, limit)
        return jsonify(page_data) 

    except Exception as e:
        return jsonify({"error": f"Unexpected error occurred: {e}"}), 500

@app.route('/sajda-ayahs', methods=['GET'])
def sajda_ayahs():
    """
    Retrieve sajda ayahs from a particular Quran edition
    ---
    parameters:
      - name: edition
        in: query
        type: string
        required: true
        description: A Quran edition identifier.
        example: en.asad
    
    responses:
      200:
        description: Sajda ayahs successfully retrieved
    """
    try:
        edition = request.args.get('edition')

        sajda_data = fetch_sajda_ayahs(edition)
        return jsonify(sajda_data)

    except Exception as e:
        return jsonify({"error": f"Unexpected error occurred: {e}"}), 500

@app.route('/asma-al-husna', methods=['GET'])
def asma_al_husna():
    """
    Retrieve Asma Al Husna (Names of Allah) with Arabic text, transliteration, and meaning
    ---
    parameters:
      - name: numbers
        in: query
        type: string
        required: false
        description: Names are numbered from 1 to 99. If not specified, all names will be returned.
        example: "1,2,3"
    
    responses:
      200:
        description: Asma Al Husna successfully retrieved
    """
    try:
        numbers = request.args.get('numbers')

        asma_al_husna_data = fetch_asma_al_husna(numbers)
        return jsonify(asma_al_husna_data)

    except Exception as e:
        return jsonify({"error": f"Unexpected error occurred: {e}"}), 500

@app.route('/quran-edition', methods=['GET'])
def quran_edition():
    """
    Retrieve Quran edition in text format
    ---
    parameters:
      - name: edition
        in: query
        type: string
        required: true
        description: A Quran edition identifier.
        example: en.asad
    
    responses:
      200:
        description: Quran edition successfully retrieved
    """
    try:
        edition_identifier = request.args.get('edition')
        quran_edition_data = get_quran_edition(edition_identifier)
        return jsonify(quran_edition_data)

    except Exception as e:
        return jsonify({"error": f"Unexpected error occurred: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=3000)
