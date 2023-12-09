from pymongo import MongoClient

# la liste et le nombre
# de films des 15 acteurs les plus présents
# from module.connexion import movies
client = MongoClient("mongodb://localhost:27017/")
# Base de donnée Cinema
db = client["cinema"]
# Collection movies
movies = db["movies"]

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

if __name__ == "__main__":
    for t in ag_4:
        print(t)
