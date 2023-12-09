from pymongo import MongoClient

# Les 5 réalisateurs ayant le plus de films
# from module.connexion import movies
client = MongoClient("mongodb://localhost:27017/")
# Base de donnée Cinema
db = client["cinema"]
# Collection movies
movies = db["movies"]

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

if __name__ == "__main__":
    for t in ag_3:
        print(t)
