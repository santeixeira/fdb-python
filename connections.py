from psycopg2 import connect

DB_NAME = "547873"
DB_USER = "547873"
DB_PASS = "547873@fbd"
DB_HOST = "200.129.44.249"
DB_PORT = "5432"

def conectar():
    return connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
