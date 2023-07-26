import streamlit as st
import data_handler as dh
from config import POSSIBLE_DIAGNOSIS
from config import DIAGNOSIS_NOT_MATCHING_ERROR
from config import get_key_string_list
from datetime import datetime

# CURRENT USER

current_user_uuid = dh.read_selected_user()
current_user = dh.get(current_user_uuid)
st.header("Settings")

# Change Audio Settings ##################################
st.subheader("Audio Settings")

if dh.read_boolean_value():
    audio_setting = "activated"
else:
    audio_setting = "deactivated"


st.write(f"Current Audio Setting: {audio_setting}")

if st.button("activate Audio Output"):
    dh.write_boolean_value(True)

if st.button("deactivate Audio Output"):
    dh.write_boolean_value(False)

st.subheader("Change Current User")

st.write(f"Current User: {current_user.name}")

# SELECT EXISTING USERS ##################################
all_users = dh.get_all_users()

selected_user = st.selectbox("Choose an existing user", all_users,
                             format_func=lambda user: f"{user.uuid} - {user.name}")

if st.button("Select Current User"):
    if selected_user:
        dh.write_selected_user(selected_user.uuid)
        message = {"role": "user", "content": "Lis, introduce yourself again"}
        dh.append_chat_history(selected_user.uuid, message)
        dh.write_boolean_value(True)

if st.button("View User Details"):
    if selected_user:
        st.write("User Details:")
        st.write("Name:", selected_user.name)
        st.write("UUID:", selected_user.uuid)
        st.write("Diagnosis:", selected_user.diagnosis)
        st.write("Last Changed:", datetime.fromtimestamp(selected_user.last_changed).strftime('%Y-%m-%d %H:%M:%S'))
        st.write("Chat History:", selected_user.chat_history)

# MODIFY DIAGNOSIS #######################################
st.subheader("Modify Diagnosis")

new_diagnosis = st.text_input("New Diagnosis")
if st.button("Confirm Diagnosis Change"):
    user_uuid = selected_user.uuid
    if new_diagnosis in POSSIBLE_DIAGNOSIS:
        dh.modify_diagnosis(user_uuid, new_diagnosis)
        init_prompt = {"role": "user", "content": POSSIBLE_DIAGNOSIS[new_diagnosis]}
        dh.append_chat_history(user_uuid, init_prompt)
    else:
        st.write(DIAGNOSIS_NOT_MATCHING_ERROR + get_key_string_list())

# CREATE NEW USER #######################################
st.subheader("Create New User")

_name = st.text_input("Name")
_diagnosis = st.text_input("Diagnosis")
if st.button("Confirm Creation"):
    if _name != "" and _name is not None and _diagnosis != "" and _diagnosis is not None:
        if _diagnosis in POSSIBLE_DIAGNOSIS:
            new_user = dh.User(
                name=_name,
                diagnosis=_diagnosis,
            )
            dh.put(new_user)
        else:
            st.write(DIAGNOSIS_NOT_MATCHING_ERROR + get_key_string_list())
    else:
        st.write("please provide correct details for the new User")

st.subheader("Deletion & Reset")

# RESET CHAT HISTORY #######################################

if st.button("Reset Chat History"):
    dh.reset_chat_history(selected_user.uuid)
    diagnosis_prompt = POSSIBLE_DIAGNOSIS[selected_user.diagnosis]
    init_prompt = {"role": "user", "content": diagnosis_prompt}
    dh.append_chat_history(selected_user.uuid, init_prompt)

# DELETE USER #######################################

if st.button("Delete User"):
    dh.delete(selected_user.uuid)
