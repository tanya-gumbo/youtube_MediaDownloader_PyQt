import json


def read_json_file():
    """Reads from the settings json file"""

def update_json_file_path(file_path):
    """Updates data in the settings json file"""
    # Read the JSON file
    try:
        with open('User_Interface/Frontend/SettingsWindow/app_settings.json', 'r') as file:
            data = json.load(file)
    except Exception as e:
        print(e)

    # Update the values (for example, increment the download counter)
    data['file_path'] = file_path

    # Write the updated data back to the JSON file
    try:
        with open('User_Interface/Frontend/SettingsWindow/app_settings.json', 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as z:
        print(z)

