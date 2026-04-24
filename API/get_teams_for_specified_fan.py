from get_db_connection import get_db_connection
import pymssql
def get_teams_for_specified_fan(nfl_fan_id: int):
    """
    Retrieve teams for a specified NFL fan.
    
    Args:
        nfl_fan_id (int): The ID of the NFL fan
    
    Returns:
        list: A list containing team information
    """
    conn = get_db_connection()
    cursor = conn.cursor(as_dict=True)
    
    # Call the stored procedure
    cursor.callproc("proGetTeamsForSpecifiedFan", (nfl_fan_id,))
    
    # Fetch all results
    rows = cursor.fetchall()
    
    # Convert rows to list of dictionaries
    teams = []
    for row in rows:
        teams.append({
            "team_name": row[0],
            "conference": row[1],
            "division": row[2],
            "team_colors": row[3]
        })
    
    cursor.close()
    conn.close()
    
    return {"teams": teams, "status": "success"}
