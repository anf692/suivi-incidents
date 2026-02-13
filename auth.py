import bcrypt
from db import connection_db

#variable globale pour stocker l'utilisateur connecté
actuelle_user = None


#fonction d'inscription
def inscription():
    connexion = connection_db()
    if not connexion:
        return

    curseur = connexion.cursor()

    try:
        #validation des entrées pour éviter les données invalides
        while True:
            try:
                nom = input("Entrer votre Nom: ").strip()
                if not nom.isalpha():
                    print("Nom invalide.")
                    continue
                break
            except ValueError:
                print("Nom invalide. Veuillez réessayer.")

        #validation de l'email pour s'assurer qu'il contient un '@' et n'est pas vide
        while True:
            try:
                email = input("Entrer votre Email: ").strip()
                if not email or "@" not in email:
                    print("Email invalide.")
                    continue
                break
            except ValueError:
                print("Email invalide. Veuillez réessayer.")

        #validation du mot de passe pour s'assurer qu'il n'est pas vide et a une longueur minimale
        while True:
            try:
                password = input("Entrer votre Mot de passe: ").strip()
                if not password or len(password) < 8:
                    print("Mot de passe invalide (minimum 8 caractères).")
                    continue
                break
            except ValueError:
                print("Mot de passe invalide. Veuillez réessayer.")

        #vérifier que tous les champs sont remplis
        if not nom or not email or not password:
            print("Tous les champs sont obligatoires.")
            return

        #hasher le mot de passe avant de le stocker
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

#fonction de connexion
def connexion():
    global actuelle_user

    connnexion = connection_db()
    if not connnexion:
        return

    #utiliser un curseur avec dictionnaire pour accéder aux champs par nom
    curseur = connnexion.cursor(dictionary=True)

    try:
        #validation des entrées pour éviter les données invalides
        while True:
            try:
                email = input("Entrer votre Email: ").strip()
                if not email or "@" not in email:
                    print("Email invalide.")
                    continue
                break
            except ValueError:
                print("Email invalide. Veuillez réessayer.")

        #validation du mot de passe pour s'assurer qu'il n'est pas vide
        while True:
            try:
                password = input("Entrer votre Mot de passe: ").strip()
                if not password:
                    print("Mot de passe invalide.")
                    continue
                break
            except ValueError:
                print("Mot de passe invalide. Veuillez réessayer.")

        curseur.execute("SELECT * FROM utilisateurs WHERE email = %s", (email,))
        user = curseur.fetchone()
        #vérifier que l'utilisateur existe et que le mot de passe correspond
        if user and bcrypt.checkpw(password.encode(), user['mot_de_passe'].encode()):
            actuelle_user = user
            print("Connexion réussie.")
        else:
            print("Identifiants incorrects.")

    except Exception as e:
        print("Erreur :", e)

    finally:
        connnexion.close()

#fonction de déconnexion
def deconnexion():
    global actuelle_user
    actuelle_user = None
    print("Déconnexion réussie.")
