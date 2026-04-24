from fastapi import FastAPI
from validate_user import validate_user
from get_teams_by_conference_division import get_teams_by_conference_division
from get_teams_in_same_conference_division_as_specified_team import get_teams_in_same_conference_division_as_specified_team
from get_teams_for_specified_fan import get_teams_for_specified_fan
import pymssql



app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "API is running"}


@app.get("/get_teams_by_conference_division")
def get_teams_by_conference_division_endpoint(conference: str = None, division: str = None):
    return get_teams_by_conference_division(conference=conference, division=division)

@app.get("/get_teams_in_same_conference_division_as_specified_team")
def get_teams_in_same_conference_division_as_specified_team_endpoint(team_name: str):
    return get_teams_in_same_conference_division_as_specified_team(team_name=team_name)

@app.get("/validate_user")
def validate_user_endpoint(email: str, password_hash: str):
    return validate_user(email=email, password_hash=password_hash)

@app.get("/get_teams_for_specified_fan")
def get_teams_for_specified_fan_endpoint(nfl_fan_id: int):
    return get_teams_for_specified_fan(nfl_fan_id=nfl_fan_id)