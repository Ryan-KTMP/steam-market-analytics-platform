import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    dbname="steam_dw",
    user="steam_admin",
    password="SteamDW_2026!Data"
)

print("SUCCESS")

conn.close()