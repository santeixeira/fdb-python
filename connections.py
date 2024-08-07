from psycopg2 import connect

DB_NAME = "name"
DB_USER = "user"
DB_PASS = "password"
DB_HOST = "ip@host"
DB_PORT = "port"

def conectar():
    return connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
