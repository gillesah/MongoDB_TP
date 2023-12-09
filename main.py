# from module.connexion import movies_dict
from module.director import Director
from module.movie import Movie
from agregation.ag_1 import ag1
from agregation.ag_2 import ag2
from agregation.ag_3 import ag3
from agregation.ag_4 import ag4


def main():
    while True:
        souhait = input(
            """Souhaitez-vous: 
            - ajouter un film (A) 
            - rechercher un réalisateur (B) 
            - lister les 5 réalisateurs les mieux notés (C)
            - les 5 réalisateurs dont les films ont la durée moyenne la plus importante (D)
            - les 5 réalisateurs ayant le plus de films (E)
            - les 15 acteurs les plus présents (F)
            [Q pour quitter] ?""")

        if souhait.lower() == "a":
            film_title = input("Titre : ")
            film_annee = input("Année : ")
            film_resume = input("Résumé long : ")
            film_shortresume = input("Résumé court : ")
            film_director = input("Réalisateur: ")
            new_movie = Movie(film_title, int(film_annee),
                              film_resume, film_shortresume, film_director)
            new_movie.create_movie()

        elif souhait.lower() == "b":
            director_search = input(
                "Merci d'entrer le nom d'un réalisateur : ")
            print(Director(director_search).movies_by_director())
            print(Director(director_search).avg_rate_director())
        elif souhait.lower() == "c":
            for t in ag1():
                print(t)
        elif souhait.lower() == "d":
            for t in ag2():
                print(t)
        elif souhait.lower() == "e":
            for t in ag3():
                print(t)
        elif souhait.lower() == "f":
            for t in ag4():
                print(t)
        elif souhait.lower() == "q":
            print("Au revoir !")
            break

        else:
            print("Merci d'entrer A, B, C, D, E, F ou Q.")


main()
