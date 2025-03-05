import requests
import csv


# 🚀 Fonction pour récupérer et afficher les titres des posts
def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        data = response.json()  # Convertir la réponse en JSON

        print("Status Code:", response.status_code)

        # Boucle pour afficher les titres proprement
        for index, post in enumerate(data):
            print("Titre:", post["title"])

            # Afficher les tirets sauf pour le dernier titre
            if index < len(data) - 1:
                print("-" * 50)
    else:
        print("Erreur:", response.status_code)


# Fonction pour récupérer et sauvegarder les posts dans un fichier CSV
def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        data = response.json()  # Convertir la réponse en JSON

        # On crée une liste de dictionnaires avec seulement id, title, body
        posts_list = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in data
        ]

        # Écriture dans un fichier CSV
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()  # Écrire la première ligne
            writer.writerows(posts_list)  # Écrire toutes les lignes

        print(" Données enregistrées dans 'posts.csv'")
    else:
        print("Erreur:", response.status_code)


# Exécuter les fonctions
fetch_and_print_posts()
fetch_and_save_posts()
