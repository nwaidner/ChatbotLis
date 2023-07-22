import streamlit as st
from openAI import open_ai_request, init_prompt
from emotion_analysis import emotion_detection_text2emotion


def main():
    st.set_page_config(page_title="Lis")

    emotions = {
        "Neutral": "./resources/emotion_pics/neutral.png",
        "Happy": "./resources/emotion_pics/happy.png",
        "Sad": "./resources/emotion_pics/sad.png",
        "Angry": "./resources/emotion_pics/angry.png",
        "Fear": "./resources/emotion_pics/fearful.png",
        "Surprise": "./resources/emotion_pics/surprised.png"
    }

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Diagnosis:")

        diagnosis = st.text_input(placeholder="Please enter a diagnosis", label="")

        st.subheader("User Input:")

        user_input = st.text_input("")

    with col2:
        if diagnosis != "":
            output = open_ai_request(content=user_input, diagnosis=diagnosis)
            emotion = (emotion_detection_text2emotion(output))
        else:
            emotion = "Neutral"
            output = "Hi, I'm Lis. Please enter a diagnosis in the corresponding Textfield :)"
        st.image(emotions[emotion], width=600)

    with col1:
        st.subheader("Lis:")

        st.write(output)


if __name__ == "__main__":
    main()
