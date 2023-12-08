from module import connexion

for row in connexion.movies_dict:
    print(row["Title"])
