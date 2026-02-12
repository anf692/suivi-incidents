import mysql.connector
import os


#fonction de connexion à la base de données
def connection_db():
    try:
        return mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME")
        )
    except Exception as e:
        print("Erreur connexion base de données :", e)
        return None
