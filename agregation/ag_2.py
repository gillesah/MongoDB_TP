from pymongo import MongoClient

#Les 5 réalisateurs dont les films ont la durée moyenne la plus importante
# from module.connexion import movies
client = MongoClient("mongodb://localhost:27017/")
# Base de donnée Cinema
db = client["cinema"]
# Collection movies
movies = db["movies"]

ag_2 = movies.aggregate(
    [
        {
            '$group': {
                '_id': '$Director',
                'avg_runtime': {
                    '$avg': '$Runtime'
                }
            }
        }, {
            '$sort': {
                'avg_runtime': -1
            }
        }, {
            '$limit': 5
        }
    ])

if __name__ == "__main__":
    for t in ag_2:
        print(t)
