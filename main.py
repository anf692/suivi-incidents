#importation des modules nécessaires
import auth
from tickets import creation_ticket, liste_tickets, liste_tickets_admin, Modifier_status

def main_menu():
    while True:
        print("\n===== APPLICATION SUPPORT =====")

        #verifier si un utilisateur est connecté pour afficher les options appropriées
        if not auth.actuelle_user:
            print("1. S'Inscription")
            print("2. Connexion")
            print("0. Quitter")

            choix = input("Entrer votre Choix: ")

            if choix == "1":
                auth.inscription()
            elif choix == "2":
                auth.connexion()
            elif choix == "0":
                break

        else:
            print(f"\nConnecté en tant que {auth.actuelle_user['nom']} ({auth.actuelle_user['role']})")
            print("1. Créer un ticket")
            print("2. Voir mes tickets")

            #afficher les options admin si l'utilisateur est admin
            if auth.actuelle_user['role'] == 'admin':
                print("3. Voir tous les tickets")
                print("4. Modifier statut ticket")
                print("5. Déconnexion")
            else:
                print("3. Déconnexion")

            choix = input("Votre Choix: ")

            if choix == "1":
                creation_ticket()
            elif choix  == "2":
                liste_tickets()
            elif choix == "3" and auth.actuelle_user['role'] == 'admin':
                liste_tickets_admin()
            elif choix == "4" and auth.actuelle_user['role'] == 'admin':
                Modifier_status()
            elif (choix == "5" and auth.actuelle_user['role'] == 'admin') or \
                 (choix == "3" and auth.actuelle_user['role'] != 'admin'):
                auth.deconnexion()

main_menu()
