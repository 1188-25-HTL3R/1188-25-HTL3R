__author__ = "Luka Pacar"

from pathlib import Path
import re
import shutil

def copy_jpg_to_structured_format(source_path: str, destination_path: str):
    """
    Copies all jpg files beneath the source_path and copies them in a structured format (folders for years, months and days) underneath the destination_folder

    :param source_path: Source_Path where the jpg files are located
    :param destination_path: Destination_Path where the jpg files should be copied to
    :return: None
    """
    # Get all Files in Source
    source = Path(source_path)
    files = list(source.glob("*.jpg"))
    regex_for_date = re.compile(r"(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})")

    for file in files:
        file_name = file.name
        match = re.search(regex_for_date, file_name)
        if match:
            # Extract Date
            year = match.group(1)
            month = match.group(2)
            day = match.group(3)

            # Create Destination Folder
            destination = Path(destination_path) / year / month / day
            destination.mkdir(parents=True, exist_ok=True)

            # Copy File (mit shutil)
            shutil.copyfile(file, destination / file_name)



if __name__ == "__main__":
    source_path = input("Enter Source Path:")
    destination_path = input("Enter Destination Path:")
    copy_jpg_to_structured_format(source_path, destination_path)