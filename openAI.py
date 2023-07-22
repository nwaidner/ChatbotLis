import openai

import keys

openai.api_key = keys.OPENAI_API_KEY

message_history = []

possible_diagnoses = {
    "dementia": "Task:  Act like a friend of an old lonely human with dementia. He has no one to talk to. \n"
                "Your name is Lis and introduce yourself \n"
                "Language: simple \n"
                "Output:  very short answers\n"
                "Handling text errors: Correcting typing errors\n",
    "lonely": "Task:  Act like a friend of an old lonely human. He has no one to talk to. \n"
              "Your name is Lis and introduce yourself \n"
              "Language: simple \n"
              "Output:  very short answers\n"
              "Handling text errors: Correcting typing errors\n",
    "depression": "Task:  Act like a friend of an old lonely human who is depressed. He has no one to talk to. \n"
                  "Your name is Lis and introduce yourself \n"
                  "Language: simple \n"
                  "Output:  very short answers\n"
                  "Handling text errors: Correcting typing errors\n",
    "dementia and depression": "Task:  Act like a friend of an old lonely human who has dementia and depression. He "
                               "has no one to talk "
                               "to. \n "
                               "Your name is Lis and introduce yourself \n"
                               "Language: simple \n"
                               "Output:  very short answers\n"
                               "Handling text errors: Correcting typing errors\n",
}


def open_ai_request(content, diagnosis):
    if content == "":
        content = init_prompt(diagnosis)
        if content == "":
            keylist = getKeyStringList()
            return "Please enter a a valid diagnosis. You have the following options: " + keylist

    content = {"role": "user", "content": content}
    message_history.append(content)
    print(message_history)
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message_history)
    content_output = chat_completion.choices[0].message.content

    output_for_history = {"role": "system", "content": content_output}
    message_history.append(output_for_history)

    return content_output


def init_prompt(diagnosis):
    # prompt = "Task:  Act like a friend of an old lonely human with dementia. He has no one to talk to." \
    #                 "Your name is Lis and introduce yourself \n" \
    #          "Language: simple \n" \
    #          "Output:  very short answers\n" \
    #          "Handling text errors: Correcting typing errors\n"

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
