import text2emotion


def emotion_detection_text2emotion(x):
    if x != "" and x is not None:
        all_emotions_value = text2emotion.get_emotion(x)
        emotion = max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]
    else:
        return "Neutral"

    if emotion is "Surprise":
        return "Neutral"

    return emotion
