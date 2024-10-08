import json
import os

# Change working directory to the script's directory
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    # __file__ is not available in some environments (e.g., interactive shells)
    pass

# User can add name and favorite sport in response.json
# Default sport "Cricket" will be added if the user does not provide a favorite sport
def load_json():
    try:
        with open('../response.json') as json_obj:
            response = json.load(json_obj)
    except FileNotFoundError:
        # Handle case where response.json does not exist
        print("response.json not found, creating a new one.")
        response = {}
    except json.JSONDecodeError:
        # Handle invalid JSON
        print("Error reading JSON, creating a new response.")
        response = {}
    return response


def write_json(data, filename='../response.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=0)
    except Exception as e:
        print(f"Failed to write to {filename}: {e}")


def call_sport():
    name = input("Please add your name: ").strip()
    sport = input("Please add your favorite sport: ").strip()


if __name__ == "__main__":
    response = load_json()  # Load once and reuse
    call_sport()
