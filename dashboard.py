import streamlit as st


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
    st.image(emotions["Happy"], width=600)
    st.subheader("User Input:")
    user_input = st.text_input("")

    st.subheader("Lis:")

    st.text(user_input)


if __name__ == "__main__":
    main()
