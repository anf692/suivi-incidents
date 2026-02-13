# Support Tickets - Application de gestion d'incidents

## Contexte

Dans un centre de formation comme **Simplon** ou **UNCHK**, le flux de demandes techniques est constant : "mon chargeur ne marche plus", "je n'ai pas accès à la plateforme", etc.  
Actuellement, ces demandes arrivent par téléphone, email ou WhatsApp, se perdent et ne sont pas suivies.

Cette application console centralisée permet à chaque utilisateur (apprenant ou staff) de créer, suivre et gérer ses tickets d’assistance de manière sécurisée.

---

## Fonctionnalités

### Pour tous les utilisateurs :

- **Inscription** : Création de compte avec nom, email (unique) et mot de passe (haché avec bcrypt).  
- **Connexion / Déconnexion** : Vérification sécurisée des identifiants.  
- **Création de ticket** : Saisie de titre, description et niveau d’urgence (Faible / Moyenne / Haute).  
- **Liste de mes tickets** : Visualisation des tickets créés par l’utilisateur.  

### Pour les administrateurs :

- **Voir tous les tickets** : Accès à tous les tickets de tous les utilisateurs.  
- **Changer le statut d’un ticket** : Mettre à jour le statut (En attente / En cours / Résolu).  
- **Historique automatique** : Chaque action (création ou changement de statut) est tracée.  

---

## Base de données

- **SGBD** : MySQL
- **Nom de la base** : `suivi_incident`  
- **Entités principales** :

1. **utilisateurs** : stocke les utilisateurs, rôle, email unique et mot de passe haché.  
2. **tickets** : stocke les tickets avec titre, description, urgence, auteur et statut.  
3. **statut** : liste normalisée des statuts (`En attente`, `En cours`, `Résolu`).  
4. **historique** : trace toutes les actions sur les tickets (création, changement de statut).  

- **Intégrité référentielle** :  
  - Suppression d’un utilisateur supprime ses tickets
  - Impossible de supprimer un statut utilisé
  - Suppression d’un ticket supprime automatiquement son historique

---

## Sécurité et bonnes pratiques

- **Mots de passe hachés** avec `bcrypt` → pas de texte clair dans la BDD.  
- **Isolement des tickets** → un utilisateur ne peut accéder qu’à ses propres tickets.  
- **Gestion des rôles** → l’admin peut voir et modifier tous les tickets.  
- **Validation des entrées** → urgence, statut et identifiants vérifiés avant insertion.  
- **Historique automatique** → traçabilité complète des actions.

---

## Installation et lancement

1. Cloner le dépôt :

git clone <URL_DU_DEPOT>
cd suivi_incidents


2. Installer les dépendances :

pip install -r requirements.txt


3. Créer la base de données et les tables (script schema_support.sql) :

mysql -u root -p < schema_support.sql


4. Lancer l’application :

python main.py
