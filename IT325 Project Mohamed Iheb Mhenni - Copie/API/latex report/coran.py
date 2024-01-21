import requests
from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

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
