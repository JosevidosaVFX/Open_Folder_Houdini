import os
import platform

# Gets the path of the current folder.
directory_path = hou.hipFile.path()

# Get the path without the file.
real_path = os.path.dirname(directory_path)

def open_folder(real_path):
    """Performs a check of the operating system"""
    if platform.system() == "Windows":
        os.startfile(real_path)
                
# Open the folder with the given route.
open_folder(real_path)