import shelve
import time
import uuid
import json

database = "users"
filename = "selected.json"


def get_all_uuids():
    with shelve.open(database) as db:
        all_uuids = list(db.keys())

    return all_uuids


def get_all_users():
    with shelve.open(database) as db:
        all_users = [db[str(uuid)] for uuid in get_all_uuids()]
    return all_users


def get(uuid):
    with shelve.open(database) as db:
        return db.get(str(uuid))


def put(uuid, user_obj):
    user_obj.last_changed = time.time()
    with shelve.open(database) as db:
        db[str(uuid)] = user_obj


def delete(uuid):
    with shelve.open(database) as db:
        if str(uuid) in db:
            del db[str(uuid)]


def modify_diagnosis(uuid, new_diagnosis):
    with shelve.open(database) as db:
        user = db.get(str(uuid))
        if user:
            user.diagnosis = new_diagnosis
            user.last_changed = time.time()
            db[str(uuid)] = user


def reset_chat_history(uuid):
    with shelve.open(database) as db:
        user = db.get(str(uuid))
        if user:
            user.chat_history = ""  # Reset the chat history
            user.last_changed = time.time()
            db[str(uuid)] = user
        else:
            raise ValueError("User not found with the given UUID.")


def modify_chat_history(uuid, new_chat_history):
    with shelve.open("users") as db:
        user = db.get(str(uuid))
        if user:
            user.chat_history = new_chat_history  # Update the chat history
            user.last_changed = time.time()
            db[str(uuid)] = user
        else:
            raise ValueError("User not found with the given UUID.")


def append_chat_history(uuid, new_chat_history):
    with shelve.open("users") as db:
        user = db.get(str(uuid))
        if user:
            string_message = repr(new_chat_history)
            user.chat_history += string_message  # Update the chat history
            user.last_changed = time.time()
            db[str(uuid)] = user
        else:
            raise ValueError("User not found with the given UUID.")


def get_chat_history(uuid):
    with shelve.open("users") as db:
        user = db.get(str(uuid))
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
        self.chat_history = ""


def read_selected_user():
    with open(filename, 'r') as file:
        data = json.load(file)
    return data.get("selected_user")


# Function to write the given data as JSON to the file
def write_selected_user(selected_user_uuid):
    with open(filename, 'r') as file:
        data = json.load(file)
        data["selected_user"] = str(selected_user_uuid)
    with open(filename, 'w') as file:
        json.dump(data, file)
