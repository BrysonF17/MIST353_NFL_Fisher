import streamlit as st
from validate_user_ui import validate_user_ui
from get_teams_conference_division_ui import get_teams_by_conference_division_ui
from get_teams_in_same_conference_division_as_specified_team_ui import get_teams_in_same_conference_division_as_specified_team_ui
from get_teams_for_specified_fan_ui import get_teams_for_specified_fan_ui
from schedule_game_ui import schedule_game_ui
from get_all_changes_by_admin_ui import get_all_changes_by_admin_ui

st.title("NFL Playoffs App")
st.write("Welcome to the NFL Playoffs App! Use the sidebar to navigate through different features.")

st.sidebar.title("NFL Playoff Functionalities")
api_endpoint = st.sidebar.selectbox(
    "Select a functionality:",
    [
        "Validate User",
        "Get Teams by Conference and Division",
        "Get Teams in Same Conference and Division as Specified Team",
        "Get Teams for Specified Fan",
        "Schedule a Game",
        "View My Admin Change History"
    ]
)

if st.session_state.get("app_user_id"):
    st.sidebar.markdown(f"**Current User ID:** {st.session_state.get('app_user_id')}")
    if st.session_state.get("app_user_role"):
        st.sidebar.markdown(f"**Role:** {st.session_state.get('app_user_role')}")

if api_endpoint == "Validate User":
    validate_user_ui()
elif api_endpoint == "Get Teams by Conference and Division":
    get_teams_by_conference_division_ui()
elif api_endpoint == "Get Teams in Same Conference and Division as Specified Team":
    get_teams_in_same_conference_division_as_specified_team_ui()
elif api_endpoint == "Get Teams for Specified Fan":
    get_teams_for_specified_fan_ui()
elif api_endpoint == "Schedule a Game":
    schedule_game_ui()
elif api_endpoint == "View My Admin Change History":
    get_all_changes_by_admin_ui()
