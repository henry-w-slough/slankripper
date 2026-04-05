import hashlib
import json

from . import config


def get_chunk_name(data:bytes, length:int=8) -> str:
    """Returns a hash name based on the data and length provided."""
    return hashlib.sha256(data).hexdigest()[:length]


def chop_file(file_src:str, data_dir:str, manifest_src:str, read_size:int, name_size:int=8) -> None:
    """Reads the file at the given path and creates data chunks based on it."""

    chunks = []

    #opening manifest to read the metadata. We open it here so we can compare the old data to the new reads
    with open(manifest_src, "r") as manifest:
        manifest_data = json.load(manifest)


    with open(file_src, "rb") as to_read:
        #iterating each chunk of data
        while chunk := to_read.read(read_size):
            
            chunk_name = get_chunk_name(chunk, name_size)

            #creating file for chunk
            with open(f"{data_dir}/{chunk_name}", "wb") as to_write:
                to_write.write(chunk)

            #adding chunk to chunk list for later manifest addition
            chunks.append(chunk_name)


    #updating metadata chunk order
    manifest_data[config.CHUNK_ORDER_KEY] = chunks

    #opening manifest to write the updated metadata
    with open(manifest_src, "w") as manifest:
        json.dump(manifest_data, manifest, indent=config.MANIFEST_INDENT)

    



    

    

        









            



