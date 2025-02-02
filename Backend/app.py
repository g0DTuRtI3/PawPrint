from flask import Flask, jsonify
from flask_cors import CORS
from Database import retrieve_dict, insert
from Owner import Owner

app = Flask(__name__)
CORS(app)  # Enable CORS for the frontend to fetch data

@app.route('/api/database/<database_name>/ID/<ID>', methods=['GET'])
def get_data(database_name, ID):
    try:
        response = retrieve_dict(database_name, ID)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@app.route('/api/database/<database_name>/obj/<data>/', methods=['GET'])
def set_data(database_name, data):
    try:
        response = insert(data, database_name)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error" : str(e)}), 500

@app.route('/api/name/<name>/phone_number/<phone_number>/gender/<gender>/email/<email>/address/<address>/', methods=['GET'])
def create_owner(name, phone_number,gender, email, address):
    try:
        response = Owner(name, phone_number, gender, email, address).to_dict()
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)