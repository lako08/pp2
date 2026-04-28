import psycopg2
from config import params

def connect():
    try:
        conn = psycopg2.connect(**params)
        return conn
    except Exception as e:
        print("Connection error:", e)
        return None