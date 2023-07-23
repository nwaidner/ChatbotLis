import streamlit as st
import data_handler as dh
from conifg import possible_diagnoses



# CURRENT USER

current_user_uuid = dh.read_selected_user()
current_user = dh.get(current_user_uuid)
st.header("Change Current User")

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

# CREATE NEW USER #######################################
st.subheader("Create New User")

_name = st.text_input("Name")
_diagnosis = st.text_input("Diagnosis")
if st.button("Confirm Creation"):
    if _name is not "" and _name is not None and _diagnosis is not "" and _diagnosis is not None:
        new_user = dh.User(
            name=_name,
            diagnosis=_diagnosis,
        )

        dh.put(new_user.uuid, new_user)

    else:
        st.write("please provide correct details for the new User")

# DELETE USER #######################################
st.subheader("Delete User")

uuid_to_delete = st.text_input("UUID of the user to delete")
if st.button("Confirm Deletion"):
    dh.delete(uuid_to_delete)

# MODIFY DIAGNOSIS #######################################
st.subheader("Modify Diagnosis")

uuid_to_change_diagnosis = st.text_input("UUID of the user to change diagnosis")
new_diagnosis = st.text_input("New Diagnosis")
if st.button("Confirm Diagnosis Change"):
    dh.modify_diagnosis(uuid_to_change_diagnosis, new_diagnosis)

# RESET CHAT HISTORY #######################################
st.subheader("Reset Chat History")

uuid_to_reset_chat_history = st.text_input("UUID of the user to reset chat history")
if st.button("Confirm Reset Chat History"):
    dh.reset_chat_history(uuid_to_reset_chat_history)


