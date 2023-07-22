import openai

import keys
from conifg import non_matching_diagnos_error_message
from conifg import possible_diagnoses

openai.api_key = keys.OPENAI_API_KEY

message_history = []


def open_ai_request(content, diagnosis):
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


def init_prompt(diagnosis):

    if diagnosis not in possible_diagnoses:
        return ""
    prompt = possible_diagnoses[diagnosis]
    print("matching diagnosis for '" + diagnosis + "' found")

    return prompt


def getKeyStringList():
    keylist = ""

    for dia in possible_diagnoses:
        keylist += dia + ", "

    return keylist
