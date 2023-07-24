import openai
import data_handler as dh
import keys
from config import possible_diagnoses

openai.api_key = keys.OPENAI_API_KEY


def open_ai_request(content):
    current_user_uuid = dh.read_selected_user()
    current_user = dh.get(current_user_uuid)

    # if content == "":
    #     content = init_prompt(current_user.diagnosis)
    #     print("content empty")

    if content != "":
        content = {"role": "user", "content": content}
        dh.append_chat_history(current_user_uuid, content)

    current_user_uuid = dh.read_selected_user()

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=dh.get_chat_history(current_user_uuid)
    )
    content_output = chat_completion.choices[0].message.content

    output_for_history = {"role": "system", "content": content_output}
    dh.append_chat_history(current_user_uuid, output_for_history)

    return content_output


def init_prompt(diagnosis):
    if diagnosis not in possible_diagnoses:
        return ""
    prompt = possible_diagnoses[diagnosis]

    return prompt
