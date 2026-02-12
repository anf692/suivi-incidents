import bcrypt
from db import connection_db

actuelle_user = None


def inscription():
    connexion = connection_db()
    if not connexion:
        return

    curseur = connexion.cursor()
    try:
        nom = input("Entrer votre Nom: ").strip()
        email = input("Entrer votre Email: ").strip()
        password = input("Entrer votre Mot de passe: ").strip()

        if not nom or not email or not password:
            print("Tous les champs sont obligatoires.")
            return

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        curseur.execute("""
            INSERT INTO utilisateurs (nom, email, mot_de_passe)
            VALUES (%s, %s, %s)
        """, (nom, email, hashed_password.decode()))

        connexion.commit()
        print("Compte créé avec succès.")

    except Exception as e:
        print("Erreur :", e)

    finally:
        connexion.close()


def connexion():
    global actuelle_user

    connnexion = connection_db()
    if not connnexion:
        return

    curseur = connnexion.cursor(dictionary=True)

    try:
        email = input("Entrer votre Email: ").strip()
        password = input("Entrer votre Mot de passe: ").strip()

        curseur.execute("SELECT * FROM utilisateurs WHERE email = %s", (email,))
        user = curseur.fetchone()

        if user and bcrypt.checkpw(password.encode(), user['mot_de_passe'].encode()):
            actuelle_user = user
            print("Connexion réussie.")
        else:
            print("Identifiants incorrects.")

    except Exception as e:
        print("Erreur :", e)

    finally:
        connnexion.close()


def logout():
    global actuelle_user
    actuelle_user = None
    print("Déconnexion réussie.")
