class Movie:
#definir el constructor
    def __init__(self, code, name, image_url = None, year = None) -> None:
        self._code = code
        self._name = name
        self.image_url = image_url
        self.year = year
class Review:
#definir el constructor
    def __init__(self, name, email, description, rating, movie_code, id = None) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.description = description
        self.rating = rating
        self.code = movie_code