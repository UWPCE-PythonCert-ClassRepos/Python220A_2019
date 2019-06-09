"""
File Recursion Homework for Lesson09
"""
import os


def jpeg_discovery(parent_directory):
    """
    Returns a list containing file directory and
    .jpgs stored within aforementioned directory given
    parent file directory
    :param parent_directory: String containing parent
    file directory
    :return: Structured list w/ directory file path
    and images contained witin them
    """

    for file in os.listdir(parent_directory):
        file_path = os.path.join(parent_directory,file)

        # Check to determine if the file path is a directory
        if os.path.isdir(file_path):
            jpeg_discovery(file_path)
        # Check if file is a .png file and handle file
        elif file.endswith(".png"):
            # Handle file if already in dictionary
            if parent_directory in file_dict.keys():
                file_dict[parent_directory] = [file]
            # Handle File if not already in dictionary
            else:
                file_dict[parent_directory] = [file]

    return [[file, file_dict[file]] for file in file_dict]


if __name__ == "__main__":
    # Create Parent Dictionary to Hold Data
    file_dict = {}
    # Establish file path
    file_path = "C:\\Python220A_2019\\students\\KyleCreek\\lesson09\\assignment\\data"
    # Return List
    test = jpeg_discovery(file_path)
    # Print Results
    print(test)
