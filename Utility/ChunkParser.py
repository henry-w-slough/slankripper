import hashlib
import json
import os
import pathlib

from .. import config
from ..Models import Movie


def get_chunk_id(data:bytes, length:int=8) -> str:
    """Returns a hash id based on the data and length provided."""
    return hashlib.sha256(data).hexdigest()[:length]


def file_to_chunks(movie:Movie.Movie, file_src:str, read_size:int, id_length:int=8) -> None:
    """Takes a file and breaks it into data chunks which are placed in a given directory. Chunks are named with hash convention."""

    #making the root file for the movie
    movie_dir = os.path.join(config.MOVIES_DIR, movie.name)
    os.makedirs(movie_dir, exist_ok=True)
    #creating the data folder for chunks
    os.makedirs(os.path.join(movie_dir, config.MOVIE_DATA_DIR), exist_ok=True)

    with open(file_src, "rb") as file:

        while chunk := file.read(read_size):

            chunk_id = get_chunk_id(chunk, id_length)
            #adding id to the order of chunks in Movie object
            movie.chunk_order.append(chunk_id)

            #writing chunk data to the movie's data dir
            with open(os.path.join(movie_dir, config.MOVIE_DATA_DIR, chunk_id), "wb") as chunk_src:
                chunk_src.write(chunk)

            







            

    


        

    



    

    

        









            



