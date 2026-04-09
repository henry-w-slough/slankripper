from ..Services import MovieService

class MovieController:


    def __init__(self) -> None:
        """Handles all user-directed Movie actions."""
        self.movie_service = MovieService.MovieService()


    def add_movie(self, id:str, name:str, src:str) -> None:
        self.movie_service.add_movie(id, name, src)




