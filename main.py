# from module.connexion import movies_dict
from module.director import Director
from module.movie import Movie

# for row in movies_dict:
#     print(row["Title"])


def main():
    while True:
        souhait = input(
            "souhaitez vous ajouter un film (M) ou rechercher un réalisateur (D) [Q pour quitter] ?")
        if souhait.lower() == "d":
            director_search = input(
                "Merci d'entrer le nom d'un réalisateur : ")
            print(Director(director_search).movies_by_director())
            print(Director(director_search).avg_rate_director())
        elif souhait.lower() == "m":
            film_title = input("Titre : ")
            film_annee = input("Année : ")
            film_resume = input("Résumé long : ")
            film_shortresume = input("Résumé court : ")
            film_director = input("Réalisateur: ")
            new_movie = Movie(film_title, int(film_annee),
                              film_resume, film_shortresume, film_director)
            new_movie.create_movie()
        elif souhait.lower() == "q":
            print("Au revoir !")
            break

        else:
            print("Merci d'entrer M, D ou Q.")


main()
