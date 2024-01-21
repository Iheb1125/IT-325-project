import requests
from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

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

if __name__ == '__main__':
    app.run(debug=True, port=3000)
