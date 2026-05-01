import streamlit as st
from fetch_data import get_data


def validate_user_ui():
    st.header("Validate User")

    email = st.text_input("Enter Email")
    password_hash = st.text_input("Enter Password", type="password")

    if st.button("Validate User"):
        if not email.strip():
            st.error("Email is required.")
            return

        if not password_hash.strip():
            st.error("Password is required.")
            return

        input_params = {
            "email": email.strip(),
            "password_hash": password_hash.strip()
        }

        df = get_data("validate_user", input_params)

        if df is not None and not df.empty:
            st.subheader(f"User {email} is valid:")
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.session_state.app_user_id = int(df["AppUserID"].values[0])
            st.session_state.app_user_role = df["UserRole"].values[0]
        else:
            st.info(f"User {email} is invalid. Please try again.")
