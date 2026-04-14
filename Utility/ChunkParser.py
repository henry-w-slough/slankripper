import hashlib
import ffmpeg
import os
import tempfile

from .. import config
from ..Models import Movie


def get_chunk_id(data:bytes, length:int=8) -> str:
    """Returns a hash id based on the data and length provided."""
    return hashlib.sha256(data).hexdigest()[:length]


def file_to_chunks(movie:Movie.Movie, file_src:str, id_length:int=8) -> None:
    """Takes a file and breaks it into data chunks which are placed in a given directory. Chunks are named with hash convention."""

    #making the root file for the movie
    movie_dir = os.path.join(config.MOVIES_DIR, movie.name)
    os.makedirs(movie_dir, exist_ok=True)
    #creating the data folder for chunks
    os.makedirs(os.path.join(movie_dir, config.MOVIE_DATA_DIR), exist_ok=True)


    #temporary src for
    with tempfile.TemporaryDirectory() as tmp_file_dir:

        transcoded_file_src = os.path.join(tmp_file_dir, f"transcoded.{config.DEFAULT_MOVIE_EXTENSION}")
        ffmpeg.input(file_src).output(transcoded_file_src, vcodec=config.TRANSCODE_DEFAULT_VCODEC, acodec=config.TRANSCODE_DEFAULT_ACODEC).run()

        with open(file_src, "rb") as file:
            
            while chunk := file.read(config.DEFAULT_READ_SIZE):
                
                chunk_id = get_chunk_id(chunk, id_length)
                #adding id to the order of chunks in Movie object
                movie.chunk_order.append(chunk_id)

                #writing chunk data to the movie's data dir
                with open(os.path.join(movie_dir, config.MOVIE_DATA_DIR, chunk_id), "wb") as chunk_src:
                    chunk_src.write(chunk)

            







            

    


        

    



    

    

        









            



