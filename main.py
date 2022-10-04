from flask import Flask, jsonify
from api import search_api
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/search/<string:search>', methods=['GET'])
def request_search(search):
    data = search_api(search)
    value_data=data['value']
    accp_key = ['title', 'description', 'url']
    structured_data = [{key : val for key, val in sub.items() if key in accp_key} for sub in value_data]
    return jsonify({'search_result': structured_data})

if __name__ == "__main__":
    app.run(debug=True, port=5000)