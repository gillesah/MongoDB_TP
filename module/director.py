from module.director_collection import directors
from module.connexion import movies_dict, movies


class Director:
    def __init__(self, name) -> None:
        self.name = name

    # Implémenter la méthode permettant de lister les films d'un réalisateur

    def movies_by_director(self):
        for director in directors.find():
            if self.name.lower() in director['director'].lower():
                return f"** {director['director']}** \n Liste de ses films : {director['movies']}"

    def avg_rate_director(self):
        rate_list = []

        for movie in movies.find():
            if 'Director' in movie and 'Rating' in movie and self.name.lower() in movie["Director"].lower():
                try:
                    rate_list.append(float(movie["Rating"]))
                except ValueError:
                    pass
            if self.name.lower() in movie["Director"].lower():
                rate_list.append(movie["Rating"])
        if rate_list:
            avg_rate = round((sum(rate_list) / len(rate_list)), 2)
            return f"La moyenne des notes de {self.name} est de {avg_rate}"
        else:
            return f"Aucune note disponible pour {self.name}"


if __name__ == '__main__':

    print(Director("honoré").avg_rate_director())

    print(Director("Grashaw").movies_by_director())


# for director in directors.find():
#     print(f"** {director['director']}** \n {director['movies']}")
