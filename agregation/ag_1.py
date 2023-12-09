#from pymongo import MongoClient
from module.connexion import movies

# Lister les 5 réalisateurs les mieux notés
# client = MongoClient("mongodb://localhost:27017/")
# # Base de donnée Cinema
# db = client["cinema"]
# # Collection movies
# movies = db["movies"]
def ag1():
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
    return ag_1
if __name__ == "__main__":
    for t in ag1():
        print(t)
