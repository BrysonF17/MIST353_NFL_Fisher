import streamlit as st
from fetch_data import get_data
from datetime import date, time
import pandas as pd

def schedule_game_ui():
    st.header("Schedule a New Game")

    nfl_admin_id = st.session_state.get("app_user_id")
    user_role = st.session_state.get("app_user_role")

    if not nfl_admin_id:
        st.warning("Please validate as an admin before scheduling games.")
        return
    if user_role and user_role.lower() != "admin":
        st.warning("Only administrators can schedule games.")
        return

    teams_df = get_data("get_all_teams", {})
    stadiums_df = get_data("get_all_stadiums", {})

    if isinstance(teams_df, pd.DataFrame) and teams_df.empty:
        st.error("Unable to load teams. Please try again.")
        return
    if not isinstance(teams_df, pd.DataFrame):
        st.error("Failed to fetch teams from the API.")
        return

    if isinstance(stadiums_df, pd.DataFrame) and stadiums_df.empty:
        st.error("Unable to load stadiums. Please try again.")
        return
    if not isinstance(stadiums_df, pd.DataFrame):
        st.error("Failed to fetch stadiums from the API.")
        return

    GAME_ROUNDS = ["Wildcard", "Divisional", "Conference", "Super Bowl"]

    team_options = dict(zip(teams_df["TeamName"], teams_df["TeamID"]))
    stadium_options = dict(zip(stadiums_df["StadiumName"], stadiums_df["StadiumID"]))

    col1, col2 = st.columns(2)
    with col1:
        home_team_name = st.selectbox("Select Home Team", options=team_options.keys())
    with col2:
        away_team_name = st.selectbox("Select Away Team", options=team_options.keys())

    stadium_name = st.selectbox("Select Stadium", options=stadium_options.keys())
    game_round = st.selectbox("Select Game Round", options=GAME_ROUNDS)

    game_date = st.date_input("Select Game Date", min_value=date.today())
    game_start_time = st.time_input("Select Game Start Time", value=time(13, 0))

    if st.button("Schedule Game"):
        if home_team_name == away_team_name:
            st.error("Home team and away team cannot be the same. Please select different teams.")
            return

        input_params = {
            "home_team_id": team_options[home_team_name],
            "away_team_id": team_options[away_team_name],
            "stadium_id": stadium_options[stadium_name],
            "game_round": game_round,
            "game_date": game_date.isoformat(),
            "game_start_time": game_start_time.isoformat(),
            "nfl_admin_id": nfl_admin_id
        }

        result = get_data("schedule_game", input_params, method="POST")
        if result is None:
            st.error("Unable to schedule game; no response from the API.")
            return

        st.info(result.get("status_message", "No response message received."))

