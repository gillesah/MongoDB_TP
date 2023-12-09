from pymongo import MongoClient
from module.connexion import movies_dict, movies


class Movie:
    def __init__(self, Title, Year, Summary, Short_summary, Director) -> None:
        self.Title = Title
        self.Year = Year
        self.Summary = Summary
        self.Short_summary = Short_summary
        self.Director = Director

    def create_movie(self):
        super().__init__
        movies.insert_one({"Title": self.Title, "Year": self.Year, "Summary": self.Summary,
                          "Short_summary": self.Short_summary, "Director": self.Director})
