from get_db_connection import get_db_connection
import pymssql

def get_teams_by_conference_division(
    conference: str = None,
    division: str = None):
    conn = get_db_connection()
    cursor = conn.cursor(as_dict=True)
    #cursor.execute("{call procGetTeamsByConferenceDivision(?, ?)}", (conference, division))
    cursor.callproc("procGetTeamsByConferenceDivision", (conference, division))
    rows = cursor.fetchall()
    conn.close()

    results = [
        {
            "TeamName": row["TeamName"],
            "Conference": row["Conference"],
            "Division": row["Division"],
            "TeamColors": row["TeamColors"]
        }
        for row in rows
    ]

    return {"data": results}