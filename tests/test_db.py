from src.common.db import get_connection


conn = get_connection()

print("DATABASE CONNECTION SUCCESS")

conn.close()