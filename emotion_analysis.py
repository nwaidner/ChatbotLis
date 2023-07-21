import text2emotion


def emotion_detection_text2emotion(x):
    all_emotions_value = text2emotion.get_emotion(x)
    return max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]


input_text = "I am sad for you but i am happy"
result_emotion = emotion_detection_text2emotion(input_text)
print(f"Emotion: {result_emotion}")