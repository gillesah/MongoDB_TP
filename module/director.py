import connexion
from connexion import db
from director_collection import directors


class Director:
    def __init__(self, name) -> None:
        self.name = name

    # Implémenter la méthode permettant de lister les films d'un réalisateur


for director in directors.find():
    print(f"** {director['director']}** \n {director['movies']}")
