from .get_db_connection import get_db_connection
import pymssql

def get_all_changes_by_admin(nfl_admin_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(as_dict=True)

    try:
        cursor.execute("exec procGetAllChangesMadeBySpecifiedAdmin %s", (nfl_admin_id,))
        rows = cursor.fetchall()
    finally:
        conn.close()

    results = [dict(row) for row in rows] if rows else []
    return {"data": results}
