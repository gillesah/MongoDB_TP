# from module.connexion import movies_dict
from module.director import Director


# for row in movies_dict:
#     print(row["Title"])


def main():
    director_search = input("Merci d'entrer le nom d'un réalisateur : ")
    print(Director(director_search).movies_by_director())  
    print(Director(director_search).avg_rate_director())  



main()
