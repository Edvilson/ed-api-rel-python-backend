import sqlite3

DB_PATH = "relatorio.db"

def populate_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS RELATORIO")
    cursor.execute("""
    CREATE TABLE RELATORIO (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT NOT NULL,
        DATA_EVENTO TEXT NOT NULL,
        VALOR REAL NOT NULL
    )""")
    dados = [
        ("João Silva", "2025-07-01", 1500.75),
        ("Maria Souza", "2025-07-10", 3200.00),
        ("Carlos Pereira", "2025-07-15", 2750.50),
        ("Ana Lima", "2025-07-20", 1800.00),
        ("Roberto Costa", "2025-07-25", 1950.00),
        ("Luciana Dias", "2025-07-28", 2200.00)
    ]
    cursor.executemany("INSERT INTO RELATORIO (NOME, DATA_EVENTO, VALOR) VALUES (?, ?, ?)", dados)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_db()
    print("Banco de dados populado com sucesso!")
