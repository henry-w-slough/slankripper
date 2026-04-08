from . import FileReader

import os
import uuid


class Assembler():


    def __init__(self) -> None:
        """Manager of finding, copying, and handling Repository data."""

        self.id = uuid.uuid4()


    def copy_repository_data(self, repository_dir:str, new_dir:str) -> None:
        """Converts the given Repositories data chunks back into a single file. The resulting file is placed in the given directory."""

        #creating new directory for the requested file placement
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        
        FileReader.copy_repository_data(repository_dir, new_dir)