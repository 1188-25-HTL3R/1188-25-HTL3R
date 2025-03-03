__author__ = "Luka Pacar"

from pathlib import Path

def find_files_by_ext(path: str, ext: str):
    """
    Takes a path and a file-extension as input and returns a list of all files with the given extension
    found below the given path.

    :param path: The path to be analyzed
    :param ext: The file-extension to be searched for
    :return: A list of all files with the given extension in the given path
    """
    path = Path(path)
    files = list(path.glob(f"*.{ext}"))
    return files

if __name__ == "__main__":
    path_input = input("Enter a path: ")
    ext_input = input("Enter a file-extension: ")
    print("Files found with the given extension:")
    for file in find_files_by_ext(path_input, ext_input):
        print(file)
