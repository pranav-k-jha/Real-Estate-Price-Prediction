from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)  # Automatically handles CORS for all routes

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        locations = util.get_location_names()
        return jsonify({'locations': locations})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.json  # Expecting JSON payload
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])
        
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        return jsonify({'estimated_price': estimated_price})
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid value: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
