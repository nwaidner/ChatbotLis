import streamlit as st

from config import emotions
from emotion_analysis import emotion_detection_text2emotion
from openAI import open_ai_request


def main():
    st.set_page_config(page_title="Lis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("User Input:")

        user_input = st.text_input(label="")

    with col2:
        output = open_ai_request(content=user_input)
        emotion = (emotion_detection_text2emotion(output))

        st.image(emotions[emotion], width=600)

    with col1:
        st.subheader("Lis:")

        st.write(output)


if __name__ == "__main__":
    main()
