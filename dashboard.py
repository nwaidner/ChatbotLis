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
        "Disgusted": "./resources/emotion_pics/disgusted.png",
        "Fearful": "./resources/emotion_pics/fearful.png",
        "Surprised": "./resources/emotion_pics/surprised.png"
    }

    # Display the Emotion
    st.image(emotions["Neutral"], width=600)
    st.subheader("User Input:")

    # init_prompt()

    user_input = st.text_input("")

    st.header(emotion_detection_text2emotion(user_input))

    st.subheader("Lis:")

    output = open_ai_request(user_input)

    st.write(output)


if __name__ == "__main__":
    main()
