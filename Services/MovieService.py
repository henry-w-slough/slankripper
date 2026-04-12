from ..Repositories import MovieRepository
from ..Models import Movie
from ..Exceptions import movie_exceptions
from ..Utility import ChunkCombiner 
from .. import config
import os


class MovieService:


    def __init__(self) -> None:
        """Handles all logic for creating and configuring Movies."""
        self.movie_repository = MovieRepository.MovieRepository()


    def add_movie(self, id:str, name:str, src:str) -> None:
        """Adds a movie to the Service's repository with the given characteristics."""
        new_movie = Movie.Movie(id, name)
        self.movie_repository.add_movie(new_movie, src)   

   
    def get_movie_by_id(self, id:str) -> Movie.Movie:
        movie = self.movie_repository.get_movie_by_id(id)

        if not movie:
            raise movie_exceptions.MovieNotFoundException(f"ERROR: Movie not found by Id: {id}")
        return movie


    def get_movie_by_name(self, name:str) -> Movie.Movie:
        movie = self.movie_repository.get_movie_by_name(name)

        if not movie:
            raise movie_exceptions.MovieNotFoundException(f"ERROR: Movie not found by name: {name}")
        return movie


    def copy_movie(self, movie:Movie.Movie, new_dir:str) -> None:
        """Copies the given Movie's data into another directory."""
        movie_dir = self.movie_repository.get_movie_directory(movie)
        if movie_dir:
            chunks_dir = os.path.join(movie_dir, config.MOVIE_DATA_DIR)
            ChunkCombiner.chunks_to_file(movie, chunks_dir, new_dir)





