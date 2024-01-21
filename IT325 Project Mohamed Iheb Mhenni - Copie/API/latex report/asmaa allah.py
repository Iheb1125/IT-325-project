import requests
from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

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

if __name__ == '__main__':
    app.run(debug=True, port=3000)
