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
        st.subheader("User Input:")

        user_input = st.text_input("")

    with col2:
        output = open_ai_request(user_input)
        emotion = (emotion_detection_text2emotion(output))
        st.image(emotions[emotion], width=600)

    with col1:
        st.subheader("Lis:")


        st.write(output)


if __name__ == "__main__":
    main()
