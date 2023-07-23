import openai
import data_handler as dh
import keys
from config import non_matching_diagnos_error_message
from config import possible_diagnoses

openai.api_key = keys.OPENAI_API_KEY


def open_ai_request(content):
    current_user_uuid = dh.read_selected_user()
    current_user = dh.get(current_user_uuid)

    if content == "":
        content = init_prompt(current_user.diagnosis)

    content = {"role": "user", "content": content}

    print(content)

    dh.append_chat_history(current_user_uuid, content)

    # current_user = dh.get(current_user_uuid)
    current_user_uuid = dh.read_selected_user()

    # print(current_user.message_history)

    #print("get_chat_history: " + str(dh.get_chat_history(current_user_uuid)))

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=dh.get_chat_history(current_user_uuid))
    content_output = chat_completion.choices[0].message.content

    output_for_history = {"role": "system", "content": content_output}
    dh.append_chat_history(current_user_uuid, output_for_history)

    return content_output


'''
def open_ai_request(content):
    if content == "":
        content = init_prompt(diagnosis)
        if content == "":
            key_list = getKeyStringList()
            return non_matching_diagnos_error_message + key_list

    content = {"role": "user", "content": content}
    message_history.append(content)
    print(message_history)
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message_history)
    content_output = chat_completion.choices[0].message.content

    output_for_history = {"role": "system", "content": content_output}
    message_history.append(output_for_history)

    return content_output

'''


def init_prompt(diagnosis):
    if diagnosis not in possible_diagnoses:
        return ""
    prompt = possible_diagnoses[diagnosis]
    print("matching diagnosis for '" + diagnosis + "' found")

    return prompt
