import streamlit as st

import data_handler as dh
from config import possible_diagnoses
from config import non_matching_diagnos_error_message
from config import getKeyStringList

# CURRENT USER

current_user_uuid = dh.read_selected_user()
current_user = dh.get(current_user_uuid)
st.header("Settings")
st.subheader("Change Current User")

st.write(f"Current User: {current_user.name}")



# SELECT EXISTING USERS ##################################
all_users = dh.get_all_users()

selected_user = st.selectbox("Choose an existing user", all_users,
                             format_func=lambda user: f"{user.uuid} - {user.name}")

if st.button("Select Current User"):
    if selected_user:
        dh.write_selected_user(selected_user.uuid)

if st.button("View User Details"):
    if selected_user:
        st.write("User Details:")
        st.write("Name:", selected_user.name)
        st.write("UUID:", selected_user.uuid)
        st.write("Diagnosis:", selected_user.diagnosis)
        st.write("Last Changed:", selected_user.last_changed)
        st.write("Chat History:", selected_user.chat_history)

# MODIFY DIAGNOSIS #######################################
st.subheader("Modify Diagnosis")

new_diagnosis = st.text_input("New Diagnosis")
if st.button("Confirm Diagnosis Change"):
    if new_diagnosis in possible_diagnoses:
        dh.modify_diagnosis(selected_user.uuid, new_diagnosis)
    else:
        st.write(non_matching_diagnos_error_message + getKeyStringList())


# CREATE NEW USER #######################################
st.subheader("Create New User")

_name = st.text_input("Name")
_diagnosis = st.text_input("Diagnosis")
if st.button("Confirm Creation"):
    if _name is not "" and _name is not None and _diagnosis is not "" and _diagnosis is not None:
        if _diagnosis in possible_diagnoses:
            new_user = dh.User(
                name=_name,
                diagnosis=_diagnosis,
            )

            dh.put(new_user)
        else:
            st.write(non_matching_diagnos_error_message + getKeyStringList())
    else:
        st.write("please provide correct details for the new User")

st.subheader("Deletion & Reset")

# RESET CHAT HISTORY #######################################

if st.button("Reset Chat History"):
    dh.reset_chat_history(selected_user.uuid)


# DELETE USER #######################################

if st.button("Delete User"):
    dh.delete(selected_user.uuid)
