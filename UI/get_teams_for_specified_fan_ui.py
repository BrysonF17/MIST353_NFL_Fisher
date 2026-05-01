import streamlit as st
from fetch_data import get_data
import pandas as pd

def get_teams_for_specified_fan_ui():
    """
    Streamlit UI for retrieving teams for a specified NFL fan.
    """
    st.header("Get Teams for Specified Fan")

    nfl_fan_id = st.number_input(
        "Enter NFL Fan ID",
        min_value=1,
        step=1,
        help="Enter the ID of the NFL fan"
    )

    if st.button("Get Teams"):
        df = get_data("get_teams_for_specified_fan", {"nfl_fan_id": nfl_fan_id})

        if df is None or df.empty:
            st.info(f"No teams found for fan ID {nfl_fan_id}.")
            return

        st.subheader(f"Teams for Fan {nfl_fan_id}:")
        st.dataframe(df, use_container_width=True, hide_index=True)
