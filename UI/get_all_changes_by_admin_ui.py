import streamlit as st
from fetch_data import get_data


def get_all_changes_by_admin_ui():
    st.header("Get All Changes Made By This Admin")

    nfl_admin_id = st.session_state.get("app_user_id")
    user_role = st.session_state.get("app_user_role")

    if not nfl_admin_id:
        st.warning("Please validate as an admin before viewing change history.")
        return
    if user_role and user_role.lower() != "admin":
        st.warning("Only administrators can view admin change history.")
        return

    st.markdown(f"**Current Admin ID:** {nfl_admin_id}")

    if st.button("Load My Changes"):
        df = get_data("get_all_changes_by_admin", {"nfl_admin_id": nfl_admin_id})
        if df is None:
            st.error("Unable to load changes. The API did not return a valid response.")
            return

        if df.empty:
            st.info("No change records were found for this admin.")
            return

        st.dataframe(df, use_container_width=True, hide_index=True)
