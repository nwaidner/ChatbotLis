import shelve
import time
import uuid
import json
from config import DATABASE_PATH
from config import SELECTED_USER_PATH
from config import BOOLEAN_VALUE_PATH
from config import POSSIBLE_DIAGNOSIS


def get_all_uuids():
    with shelve.open(DATABASE_PATH) as data_base:
        all_uuids = list(data_base.keys())

    return all_uuids


def get_all_users():
    with shelve.open(DATABASE_PATH) as data_base:
        all_users = [data_base[str(uuid)] for uuid in get_all_uuids()]
    return all_users


def get(uuid):
    with shelve.open(DATABASE_PATH) as data_base:
        return data_base.get(str(uuid))


def put(user_obj):
    user_obj.last_changed = time.time()
    with shelve.open(DATABASE_PATH) as data_base:
        data_base[str(user_obj.uuid)] = user_obj


def check(uuid):
    with shelve.open(DATABASE_PATH) as data_base:
        return str(uuid) in data_base


def delete(uuid):
    with shelve.open(DATABASE_PATH) as data_base:
        if str(uuid) in data_base:
            del data_base[str(uuid)]


def modify_diagnosis(uuid, new_diagnosis):
    with shelve.open(DATABASE_PATH) as data_base:
        user = data_base.get(str(uuid))
        if user:
            user.diagnosis = new_diagnosis
            user.last_changed = time.time()
            data_base[str(uuid)] = user


def reset_chat_history(uuid):
    with shelve.open(DATABASE_PATH) as data_base:
        user = data_base.get(str(uuid))
        if user:
            user.chat_history = ""  # Reset the chat history
            user.last_changed = time.time()
            data_base[str(uuid)] = user
        else:
            raise ValueError("User not found with the given UUID.")


def modify_chat_history(uuid, new_chat_history):
    with shelve.open(DATABASE_PATH) as data_base:
        user = data_base.get(str(uuid))
        if user:
            user.chat_history = new_chat_history  # Update the chat history
            user.last_changed = time.time()
            data_base[str(uuid)] = user
        else:
            raise ValueError("User not found with the given UUID.")


def append_chat_history(uuid, new_chat_history):
    with shelve.open(DATABASE_PATH) as data_base:
        user = data_base.get(str(uuid))
        if user:
            string_message = repr(new_chat_history)
            user.chat_history += string_message  # Update the chat history
            user.last_changed = time.time()
            data_base[str(uuid)] = user
        else:
            raise ValueError("User not found with the given UUID.")


def get_chat_history(uuid):
    with shelve.open(DATABASE_PATH) as data_base:
        user = data_base.get(str(uuid))
        if user:
            message_history = custom_eval(user.chat_history)

    return message_history


def add_comma_between_brackets(input_string):
    result = ""
    for i in range(len(input_string)):
        result += input_string[i]
        if input_string[i] == '}' and i < len(input_string) - 1 and input_string[i + 1] == '{':
            result += ','
    return result


def custom_eval(message_history):
    message_history = f"[{message_history}]"
    message_history = add_comma_between_brackets(message_history)
    return eval(message_history)


class User:
    def __init__(self, name, diagnosis):
        self.name = name
        self.uuid = uuid.uuid4()
        self.diagnosis = diagnosis
        self.last_changed = time.time()
        self.chat_history = repr({"role": "user", "content": POSSIBLE_DIAGNOSIS[diagnosis]})


def read_selected_user():
    with open(SELECTED_USER_PATH, 'r') as file:
        data = json.load(file)
    return data.get(SELECTED_USER_PATH)


# Function to write the given data as JSON to the file
def write_selected_user(selected_user_uuid):
    with open(SELECTED_USER_PATH, 'r') as file:
        data = json.load(file)
        data[SELECTED_USER_PATH] = str(selected_user_uuid)
    with open(SELECTED_USER_PATH, 'w') as file:
        json.dump(data, file)


def read_boolean_value():
    with open(BOOLEAN_VALUE_PATH, 'r') as file:
        data = json.load(file)
        # Assuming the JSON file contains a boolean value directly
        return data


def write_boolean_value(boolean_value):
    data = boolean_value
    with open(BOOLEAN_VALUE_PATH, 'w') as file:
        json.dump(data, file)

