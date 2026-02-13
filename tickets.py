from db import connection_db
import auth

#fonction de création de ticket
def creation_ticket():
    
    #vérifier si l'utilisateur est connecté
    if not auth.actuelle_user:
        print("Veuillez vous connecter.")
        return

    connexion = connection_db()
    curseur = connexion.cursor()

    try:

        #donne de saisir les informations du ticket avec validation
        while True:
            try:
                titre = str(input("Entrer la Titre: ").strip())
                if not titre.isalpha() or not titre:
                    print("Le titre invalide.")
                    continue
                break
            except ValueError:
                print("Titre invalide. Veuillez réessayer.")

        #validation de la description pour éviter les entrées vides
        while True:
            try:
                description = input("Entrer la Description: ").strip()
                if not description:
                    print("La description ne peut pas être vide.")
                    continue
                break
            except ValueError:
                print("Description invalide. Veuillez réessayer.")

        #validation de l'urgence pour n'accepter que les valeurs valides
        while True:
            urgence = input("Urgence (Faible/Moyenne/Haute): ").strip().capitalize()

            if urgence not in ["Faible", "Moyenne", "Haute"]:
                print("Urgence invalide.")
                continue
            break

        curseur.execute("""
            INSERT INTO tickets (titre, description, urgence, id_user, id_statut)
            VALUES (%s, %s, %s, %s, 1)
        """, (titre, description, urgence, auth.actuelle_user['id_user']))

        #prendre l'id du ticket créé pour l'historique
        ticket_id = curseur.lastrowid

        curseur.execute("""
            INSERT INTO historiques (action, id_user, id_ticket)
            VALUES (%s, %s, %s)
        """, ("Création du ticket", auth.actuelle_user['id_user'], ticket_id))

        connexion.commit()
        print("Ticket créé avec succès.")

    except Exception as e:
        print("Erreur :", e)

    finally:
        connexion.close()


#fonction de liste des tickets pour utilisateur connecté
def liste_tickets():
    if not auth.actuelle_user:
        print("Veuillez vous connecter.")
        return

    connexion = connection_db()
    curseur = connexion.cursor(dictionary=True)

    try:
        curseur.execute("""
            SELECT t.id_ticket, t.titre, t.urgence, s.libelle
            FROM tickets t
            JOIN statuts s ON t.id_statut = s.id_statut
            WHERE t.id_user = %s
        """, (auth.actuelle_user['id_user'],))

        tickets = curseur.fetchall()

        if not tickets:
            print("Aucun ticket.")
        else:
            for t in tickets:
                print(f"{t['id_ticket']} | {t['titre']} | {t['urgence']} | {t['libelle']}")

    except Exception as e:
        print("Erreur :", e)

    finally:
        connexion.close()


#fonrction de liste des tickets pour admin
def liste_tickets_admin():
    if not auth.actuelle_user or auth.actuelle_user['role'] != 'admin':
        print("Accès refusé.")
        return

    connexion = connection_db()
    curseur = connexion.cursor(dictionary=True)

    try:
        curseur.execute("""
            SELECT t.id_ticket, t.titre, u.nom, s.libelle
            FROM tickets t
            JOIN utilisateurs u ON t.id_user = u.id_user
            JOIN statuts s ON t.id_statut = s.id_statut
        """)

        tickets = curseur.fetchall()

        for t in tickets:
            print(f"{t['id_ticket']} | {t['titre']} | {t['nom']} | {t['libelle']}")

    except Exception as e:
        print("Erreur :", e)

    finally:
        connexion.close()


#fonction de modification du status par admin
def Modifier_status():
    if not auth.actuelle_user or auth.actuelle_user['role'] != 'admin':
        print("Seul l'admin peut modifier le statut.")
        return

    connexion = connection_db()
    curseur = connexion.cursor()

    try:
        #validation de l'id du ticket et du nouveau statut pour éviter les entrées invalides
        while True:
            try:
                ticket_id = input("ID du ticket: ").strip()
                if not ticket_id.isdigit():
                    print("ID invalide.")
                    continue
                break
            except ValueError:
                print("Entrée invalide reessayer.")

        #validation du nouveau statut pour n'accepter que les valeurs valides
        while True:
            try:
                new_status_id = input("Nouveau statut (1=En attente, 2=En cours, 3=Résolu): ").strip()
                if new_status_id not in ["1", "2", "3"]:
                    print("Statut invalide.")
                    continue
                break
            except ValueError:
                print("Entrée invalide reessayer.")
            return

        curseur.execute("SELECT id_ticket FROM tickets WHERE id_ticket = %s", (ticket_id,))
        if not curseur.fetchone():
            print("Ticket introuvable.")
            return

        curseur.execute("""
            UPDATE tickets
            SET id_statut = %s
            WHERE id_ticket = %s
        """, (new_status_id, ticket_id))

        curseur.execute("""
            INSERT INTO historiques (action, id_user, id_ticket)
            VALUES (%s, %s, %s)
        """, ("Changement de statut", auth.actuelle_user['id_user'], ticket_id))
        connexion.commit()
        print("Statut mis à jour.")

    except Exception as e:
        print("Erreur :", e)

    finally:
        connexion.close()


