from db import connection_db
from auth import actuelle_user

#fonction de création de ticket
def creation_ticket():

    if not actuelle_user:
        print("Veuillez vous connecter.")
        return

    connexion = connection_db()
    curseur = connexion.cursor()

    try:
        titre = input("Entrer la Titre: ").strip()
        description = input("Entrer le Description: ").strip()
        urgence = input("Urgence (Faible/Moyenne/Haute): ").strip().capitalize()

        if urgence not in ["Faible", "Moyenne", "Haute"]:
            print("Urgence invalide.")
            return

        curseur.execute("""
            INSERT INTO tickets (titre, description, urgence, id_user, id_statut)
            VALUES (%s, %s, %s, %s, 1)
        """, (titre, description, urgence, actuelle_user['id_user']))

        ticket_id = curseur.lastrowid

        curseur.execute("""
            INSERT INTO historiques (action, id_user, id_ticket)
            VALUES (%s, %s, %s)
        """, ("Création du ticket", actuelle_user['id_user'], ticket_id))

        connexion.commit()
        print("Ticket créé avec succès.")

    except Exception as e:
        print("Erreur :", e)

    finally:
        connexion.close()


#fonction de liste des tickets pour utilisateur connecté
def liste_tickets():
    if not actuelle_user:
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
        """, (actuelle_user['id_user'],))

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
    if not actuelle_user or actuelle_user['role'] != 'admin':
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
    if not actuelle_user or actuelle_user['role'] != 'admin':
        print("Seul l'admin peut modifier le statut.")
        return

    connexion = connection_db()
    curseur = connexion.cursor()

    try:
        ticket_id = input("ID du ticket: ").strip()
        new_status_id = input("Nouveau statut (1=En attente, 2=En cours, 3=Résolu): ").strip()

        if new_status_id not in ["1", "2", "3"]:
            print("Statut invalide.")
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
        """, ("Changement de statut", actuelle_user['id_user'], ticket_id))
        connexion.commit()
        print("Statut mis à jour.")

    except Exception as e:
        print("Erreur :", e)

    finally:
        connexion.close()


