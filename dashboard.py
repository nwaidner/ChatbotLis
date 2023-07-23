import streamlit as st
from openAI import open_ai_request, init_prompt
from emotion_analysis import emotion_detection_text2emotion
from conifg import emotions
from conifg import default_emotion
from conifg import default_output


def main():
    st.set_page_config(page_title="Lis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("User Input:")

        user_input = st.text_input("")

    with col2:
        if user_input != "":
            output = open_ai_request(content=user_input)
            emotion = (emotion_detection_text2emotion(output))
        else:
            emotion = default_emotion
            output = default_output
        st.image(emotions[emotion], width=600)

    with col1:
        st.subheader("Lis:")

        st.write(output)


if __name__ == "__main__":
    main()
