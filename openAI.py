import openai
import keys


openai.api_key = keys.OPENAI_API_KEY


def open_ai_request(content):
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                   messages=[{"role": "user", "content": content}])

    return chat_completion.choices[0].message.content


def init_prompt():
    prompt = "Task:  Act like a friend of an old lonely human with dementia. He has no one to talk to. \n" \
                "Language: simple \n" \
                "Output:  very short answers\n" \
                "Handling text errors: Correcting typing errors\n"

    return open_ai_request(prompt)
