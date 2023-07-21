import text2emotion


def emotion_detection_text2emotion(x):
    all_emotions_value = text2emotion.get_emotion(x)
    return max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]