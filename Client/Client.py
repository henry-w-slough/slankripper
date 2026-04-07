from . import FileReader

import os


class Client():


    def __init__(self) -> None:
        
        #the size of which chunks are created (default 32MB)
        self.read_size = (1024*1024*32)


    def set_read_size(self, size:int) -> None:
        """Sets the size in megabytes at which file chunks will be created."""
        #NOTE: May want to change this for more versatility of chunk data size
        self.read_size = (1024*1024*size)


    def copy_repository_data(self, repository_dir:str, new_dir:str) -> None:
        """Converts the given Repositories data chunks back into a single file. The resulting file is placed in the given directory."""

        #creating new directory for the requested file placement
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        
        FileReader.copy_repository_data(repository_dir, new_dir, self.read_size)