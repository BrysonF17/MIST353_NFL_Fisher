import streamlit as st
from get_teams_conference_division_ui import get_teams_by_conference_division_ui


def nfl_playoffs_ui():
    st.title("NFL Playoffs")
    st.write("Welcome to the NFL Playoffs UI! Here you can find information about the teams, matchups, and schedule for the NFL playoffs.")
    
    #Creating a sidebar for navigation
    #Dropdown for nfl playoff functionalities
    with st.sidebar:
        st.title("NFL Playoff Functionalities")

        st.selectbox(
            "Select a functionality", ["Get Teams by Conference and Division", "Get Teams in Same Conference and Division as Specified Team"]
        )
        if api_endpoint == "Get Teams by Conference and Division":
            get_teams_by_conference_division_ui()

        elif api_endpoint == "Get Teams in Same Conference and Division as Specified Team":
            get_teams_in_same_conference_division_as_specified_team_ui()
