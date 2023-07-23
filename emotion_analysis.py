import text2emotion


def emotion_detection_text2emotion(text_to_analyse):
    if text_to_analyse != "" and text_to_analyse is not None:
        all_emotions_value = text2emotion.get_emotion(text_to_analyse)
        emotion = max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]
    else:
        return "Neutral"

    if emotion == "Surprise":
        return "Neutral"

    return emotion
