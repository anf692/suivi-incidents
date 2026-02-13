import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # charge les variables depuis .env

#fonction de connexion à la base de données
def connection_db():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn

    except Exception as e:
        print("Erreur connexion base de données :", e)
        return None
    
