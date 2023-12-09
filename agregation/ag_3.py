from pymongo import MongoClient
from module.connexion import movies
# Les 5 réalisateurs ayant le plus de films
client = MongoClient("mongodb://localhost:27017/")
# Base de donnée Cinema
db = client["cinema"]
# Collection movies
movies = db["movies"]


def ag3():
    ag_3 = movies.aggregate(
        [
            {
                '$group': {
                    '_id': '$Director',
                    'movies_number': {
                        '$sum': 1
                    }
                }
            }, {
                '$sort': {
                    'movies_number': -1
                }
            }, {
                '$limit': 5
            }
        ]
    )
    return ag_3


if __name__ == "__main__":
    for t in ag3():
        print(t)
