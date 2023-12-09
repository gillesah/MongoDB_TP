from pymongo import MongoClient

# Lister les 5 réalisateurs les mieux notés
# from module.connexion import movies
client = MongoClient("mongodb://localhost:27017/")
# Base de donnée Cinema
db = client["cinema"]
# Collection movies
movies = db["movies"]

ag_1 = movies.aggregate(
    [
        {
            '$group': {
                '_id': '$Director',
                'sum_rating': {
                    '$avg': '$Rating'
                }
            }
        }, {
            '$sort': {
                'sum_rating': -1
            }
        }, {
            '$limit': 5
        }
    ])

if __name__ == "__main__":
    for t in ag_1:
        print(t)
