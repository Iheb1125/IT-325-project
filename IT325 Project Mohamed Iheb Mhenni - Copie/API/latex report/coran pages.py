import requests
from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

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

if __name__ == '__main__':
    app.run(debug=True, port=3000)
