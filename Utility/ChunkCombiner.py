
import os
import json

from .. import config

def chunks_to_file(chunks_dir:str, new_dir:str) -> None:

    os.makedirs(new_dir, exist_ok=True)
    
    #CHANGE MAGIC STRING
    with open(os.path.join(new_dir, "video.mp4"), "wb") as new_file:
        for chunk_id in os.listdir(chunks_dir):
            with open(os.path.join(chunks_dir, chunk_id), "rb") as chunk:
                new_file.write(chunk.read(config.DEFAULT_READ_SIZE))
            

