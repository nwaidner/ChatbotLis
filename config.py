# Database
DATABASE_PATH = "users"
SELECTED_USER_PATH = "resources/selected.json"
AUDIO_PATH = "resources/tts_audiofile.mp3"

# Emotions that can be shown
emotions = {
    "Neutral": "./resources/emotion_pics/neutral.png",
    "Happy": "./resources/emotion_pics/happy.png",
    "Sad": "./resources/emotion_pics/sad.png",
    "Angry": "./resources/emotion_pics/angry.png",
    "Fear": "./resources/emotion_pics/fearful.png",
    "Surprise": "./resources/emotion_pics/surprised.png"
}

# Default Emotion
DEFAULT_EMOTION = "Neutral"

# Default Output
DEFAULT_OUTPUT = "Hi, I'm Lis. Please enter a diagnosis in the corresponding Textfield :)"

# supported diagnoses types
possible_diagnoses = {
    "dementia": "Task:  Act like a friend of an old lonely human with dementia. "
                "He has no one to talk to. \n"
                "Your name is Lis and introduce yourself \n"
                "Language: simple \n"
                "Output:  very short answers\n"
                "Handling text errors: Correcting typing errors\n",
    "lonely": "Task:  Act like a friend of an old lonely human. "
              "He has no one to talk to. \n"
              "Your name is Lis and introduce yourself \n"
              "Language: simple \n"
              "Output:  very short answers\n"
              "Handling text errors: Correcting typing errors\n",
    "depression": "Task:  Act like a friend of an old lonely human who is depressed. "
                  "He has no one to talk to. \n"
                  "Your name is Lis and introduce yourself \n"
                  "Language: simple \n"
                  "Output:  very short answers\n"
                  "Handling text errors: Correcting typing errors\n",
    "dementia and depression": "Task:  Act like a friend of an old lonely "
                               "human who has dementia and depression. He has no one to talk "
                               "to. \n "
                               "Your name is Lis and introduce yourself \n"
                               "Language: simple \n"
                               "Output:  very short answers\n"
                               "Handling text errors: Correcting typing errors\n",
}

# Output that is shown, when a diagnosis is not supported
DIAGNOSIS_NOT_MATCHING_ERROR = "Please enter a a valid diagnosis. You have the following options: "


def get_key_string_list():
    keys = ""

    for dia in possible_diagnoses:
        keys += dia + ", "

    return keys
