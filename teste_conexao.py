import pyodbc 

try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=CA-C-004UQ\SQLEXPRESS;DATABASE=GS-PT;UID=sa;PWD=isateste123')
    print("Conexao feita...")

    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM dbo.dremel") 
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
except pyodbc.Error as e:
    print(f"Erro na conexão: {e}")
finally:
    if conn:
        conn.close()
