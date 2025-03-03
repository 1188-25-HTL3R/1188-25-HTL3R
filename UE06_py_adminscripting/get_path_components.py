__author__ = "Luka Pacar"

from pathlib import Path


def get_path_components(path: str):
    """
    This function takes a path as input and returns the following components of the path:
    - Filename
    - Filename without extension
    - File-extension
    - Part before folders
    - Parent
    - Parent's parent

    :param path: The path to be analyzed
    :return: A string containing the components of the path
    """
    path = Path(path)
    parent_directory = path.parent

    if parent_directory.is_dir():
        parent_directory = parent_directory.parent

    if not parent_directory.exists():
        parent_directory = "Parent directory does not exist!"

    path_components = (
        f'Filename: {path}\n'
        f'Filename without extension: {path.stem}\n'
        f'File-extension: {path.suffix}\n'
        f'Part before folders: {path.anchor}\n'
        f'Parent: {path.parent}\n'
        f'Parent\'s parent: {parent_directory}\n'
    )
    return path_components


if __name__ == "__main__":
    path_input = input("Enter a path: ")
    print(get_path_components(path_input))
