from pymongo import MongoClient
import connexion
from connexion import movies_dict, db

directors = db["directors"]

# Créer un dictionnaire pour regrouper les films par réalisateur
movies_by_director = {}

for movie in movies_dict:
    director = movie.get("Director")
    title = movie.get("Title")

    if director in movies_by_director:
        movies_by_director[director].add(title)
    else:
        movies_by_director[director] = {title}
## pour insérer dans la collection, merci de décommenter ces lignes :
# for director, movies in movies_by_director.items():
#     directors.insert_one({"director": director, "movies": list(movies)})
