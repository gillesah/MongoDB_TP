db.createCollection("movies", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            #seul le titre est obligatoire
            required: ["Title"],
            properties: {
                Title: {
                    bsonType: "string",
                    description: "Le titre est obligatoire et doit être une chaîne de caractères."
                },
                Year: {
                    bsonType: "int",
                    description: "L'année doit être un entier."
                },
                Summary: {
                    bsonType: "string",
                    description: "Un résumé du film."
                },
                Short_Summary: {
                    bsonType: "string",
                    description: "Un court résumé du film."
                },
                IMDB_ID: {
                    bsonType: "string",
                    description: "L'ID IMDB du film."
                },
                Runtime: {
                    bsonType: "int",
                    description: "La durée du film en minutes."
                },
                YouTube_Trailer: {
                    bsonType: "string",
                    description: "L'ID de la bande-annonce YouTube."
                },
                Rating: {
                    bsonType: "double",
                    description: "La note du film."
                },
                Movie_Poster: {
                    bsonType: "string",
                    description: "L'URL de l'image du film."
                },
                Director: {
                    bsonType: "string",
                    description: "Le réalisateur du film."
                },
                Writers: {
                    bsonType: "string",
                    description: "Les scénaristes du film."
                },
                Cast: {
                    bsonType: "string",
                    description: "La distribution du film."
                }
            }
        }
    }
})
