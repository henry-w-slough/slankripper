from ..Video import FileReader
from .. import config

import os
import json
import uuid


class Video():


    def __init__(self, root_dir:str) -> None:
        """Manager of all information and data relating to the organization of files. This includes the data itself, it's location, and how data is handled in operations."""

        self.id = uuid.uuid4()

        self.root_dir = root_dir

        #the size of which chunks are created (default 32MB)
        self.read_size = (1024*1024*32)

        os.makedirs(self.root_dir, exist_ok=True)
        os.makedirs(os.path.join(self.root_dir, config.DATA_DIR), exist_ok=True)

        with open(os.path.join(self.root_dir, config.MANIFEST_SRC), "w") as manifest:
            #writing default manifest values
            json.dump(config.MANIFEST_DEFAULTS, manifest)

        
    def set_read_size(self, size:int) -> None:
        """Sets the size in megabytes at which file chunks will be created."""
        #NOTE: May want to change this for more versatility of chunk data size
        self.read_size = (1024*1024*size)


    def add_file(self, src:str) -> None:
        """Takes a given file and converts it into seperate data files within the Repositories data directory."""
        FileReader.file_to_chunks(self.root_dir, src, self.read_size)

    
