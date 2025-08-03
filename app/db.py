import sqlite3
from app.config import Config

def get_connection():
    conn = sqlite3.connect(Config.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def query_report(data_inicial=None, data_final=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT ID, NOME, DATA_EVENTO, VALOR FROM RELATORIO
    WHERE (? IS NULL OR DATA_EVENTO >= ?)
    AND (? IS NULL OR DATA_EVENTO <= ?)
    ORDER BY DATA_EVENTO DESC
    """
    params = [data_inicial, data_inicial, data_final, data_final]
    cursor.execute(query, params)
    rows = cursor.fetchall()
    columns = rows[0].keys() if rows else ["ID", "NOME", "DATA_EVENTO", "VALOR"]
    result_rows = [tuple(row) for row in rows]
    cursor.close()
    conn.close()
    return columns, result_rows
