import json


def read_json_file_path():
    """Reads from the settings json file"""
    try:
        with open('User_Interface/Frontend/Settings/app_settings.json', 'r') as file:
            data = json.load(file)
            file_path = data['file_path']
            return file_path
    except Exception as e:
        print(e)


def update_json_file_path(file_path):
    """Updates data in the settings json file"""
    # Read the JSON file
    try:
        with open('User_Interface/Frontend/Settings/app_settings.json', 'r') as file:
            data = json.load(file)
    except Exception as e:
        print(e)

    # Update the values (for example, increment the download counter)
    data['file_path'] = file_path

    # Write the updated data back to the JSON file
    try:
        with open('User_Interface/Frontend/Settings/app_settings.json', 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as z:
        print(z)

def read_json_status():
    try:
        with open('User_Interface/Frontend/Settings/app_settings.json', 'r') as file:
           data = json.load(file)
           status = data['user_status']
           return status
    except Exception as e:
        print(e)

def update_json_status(new_status: str):
    try:
        with open('User_Interface/Frontend/Settings/app_settings.json', 'r') as file:
            data = json.load(file)

        data['user_status'] = new_status

        with open('User_Interface/Frontend/Settings/app_settings.json', 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(e)
