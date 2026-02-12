import mysql.connector
import os


#fonction de connexion à la base de données
def connection_db():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", ""),
            database=os.environ.get("DB_NAME", "")
        )
        return conn

    except Exception as e:
        print("Erreur connexion base de données :", e)
        return None
    
