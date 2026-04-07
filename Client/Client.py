from . import FileReader

import os


class Client():


    def __init__(self) -> None:
        """Manager of finding, copying, and handling Repository data."""
        #there will be other functionality relating to clients needing class vars
        pass


    def copy_repository_data(self, repository_dir:str, new_dir:str) -> None:
        """Converts the given Repositories data chunks back into a single file. The resulting file is placed in the given directory."""

        #creating new directory for the requested file placement
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        
        FileReader.copy_repository_data(repository_dir, new_dir)