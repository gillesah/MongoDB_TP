from pymongo import MongoClient
from module.connexion import movies
# la liste et le nombre
# de films des 15 acteurs les plus présents

# client = MongoClient("mongodb://localhost:27017/")
# # Base de donnée Cinema
# db = client["cinema"]
# # Collection movies
# movies = db["movies"]


def ag4():
    ag_4 = movies.aggregate(
        [
            {
                '$addFields': {
                    'new_actor': {
                        '$split': [
                            '$Cast', '|'
                        ]
                    }
                }
            }, {
                '$unwind': {
                    'path': '$new_actor'
                }
            }, {
                '$group': {
                    '_id': '$new_actor',
                    'count': {
                        '$sum': 1
                    },
                    'films': {
                        '$push': '$Title'
                    }
                }
            }, {
                '$sort': {
                    'count': -1
                }
            },
            {
                '$limit': 15
            }
        ]
    )
    return ag_4


if __name__ == "__main__":
    for t in ag4():
        print(t)
