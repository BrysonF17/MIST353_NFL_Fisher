import streamlit as st
import requests
import pandas as pd

def get_teams_for_specified_fan_ui():
    """
    Streamlit UI for retrieving teams for a specified NFL fan.
    """
    st.header("Get Teams for Specified Fan")
    
    # Input for NFL Fan ID
    nfl_fan_id = st.number_input(
        "Enter NFL Fan ID",
        min_value=1,
        step=1,
        help="Enter the ID of the NFL fan"
    )
    
    # Button to retrieve teams
    if st.button("Get Teams"):
        # Call the API endpoint
        response = requests.get(
            f"http://127.0.0.1:8000/get_teams_for_specified_fan",
            params={"nfl_fan_id": nfl_fan_id}
        )
        
        data = response.json()
        teams = data["teams"]
        
        # Display teams in a table
        df = pd.DataFrame(teams)
        st.dataframe(df, use_container_width=True)
        
        # Display individual team details
        for i, team in enumerate(teams, 1):
            st.write(f"**Team {i}:** {team['team_name']} - {team['conference']} {team['division']}")


if __name__ == "__main__":
    get_teams_for_specified_fan_ui()
