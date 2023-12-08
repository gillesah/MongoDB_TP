from pymongo import MongoClient
import csv

client = MongoClient("mongodb://localhost:27017/")
# Base de donnée Cinema
db = client["cinema"]
# Collection movies
movies = db["movies"]

# avoir movies en format dictionnaire
movies_dict = movies.find({})


def clean_data(row):
    # nettoyage de la base de donnée
    # au niveau année : on transforme en entier
    try:
        row['Year'] = int(row['Year'])
    except ValueError:
        row['Year'] = None

    # au niveau Runtime : temps de film en minute et donc entier
    try:
        row['Runtime'] = int(row['Runtime'])
    except ValueError:
        row['Runtime'] = None
    # Rating est un float
    try:
        row['Rating'] = float(row['Rating'])
    except ValueError:
        row['Rating'] = None
    return row
# ouverture de movies.csv pour le lire en dictionnaire
with open("./data/movies.csv", newline='', encoding="utf-8") as f:
    movies_list = csv.DictReader(f, delimiter=',')
    for row in movies_list:
        clean_row = clean_data(row)
        # importation dans MongoDB dans la collection Movies
        # movies.insert_one(clean_row) # à décommenter pour importer
