from flask import Flask, jsonify, request
from flask_cors import CORS
from Database import retrieve_dict, insert
from Animal import Animal
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

@app.route('/api/database/<database_name>/', methods=['POST'])
def set_data(database_name):
    try:
        data = request.json
        response = insert(data, database_name)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error" : str(e)}), 500

@app.route('/api/name/<name>/phone_number/<phone_number>/gender/<gender>/email/<email>/address/<address>/', methods=['GET'])
def create_animal(name, breed, age, weight, gender, owner_name, owner_phone_number, owner_gender, owner_email, owner_address,
                  allergy=None, medication=None, vaccination=None, checkup=None):
    try:
        response = Animal(name, breed, age, weight, gender, allergy, medication, vaccination, checkup)
        owner = Owner(owner_name, owner_phone_number, owner_gender, owner_email, owner_address)
        response.add_owner(owner)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)