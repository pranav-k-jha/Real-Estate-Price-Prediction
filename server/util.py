import json
import pickle
import numpy as np

# Global variables
__locations = None
__data_columns = None
__model = None

def load_saved_artifacts(artifacts_path):
    """Loads saved artifacts from the specified path."""
    global __locations, __data_columns, __model

    try:
        with open(f"{artifacts_path}/columns.json", "r") as f:
            data = json.load(f)
            __data_columns = data['data_columns']
            __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

        with open(f"{artifacts_path}/banglore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)

        print("Artifacts loaded successfully.")
    except Exception as e:
        print(f"Error loading artifacts: {e}")

def get_estimated_price(location, sqft, bhk, bath):
    """Predicts the estimated home price."""
    global __data_columns, __model

    if __data_columns is None or __model is None:
        return "Model or data columns not loaded properly."

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        # Handle invalid location
        return "Location not found."

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    try:
        return round(__model.predict([x])[0], 2)
    except Exception as e:
        # Handle prediction errors
        return f"Prediction error: {e}"

def get_location_names():
    """Returns a list of location names."""
    return __locations

if __name__ == '__main__':
    # Replace with the actual path to your artifacts
    artifacts_path = "./artifacts"
    load_saved_artifacts(artifacts_path)
    
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
