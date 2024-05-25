import os


def search_files(directory, pattern):
    """
    Search for files that match a given pattern within a directory and its subdirectories.

    :param directory: The directory to search in.
    :param pattern: The pattern to match the file names against.
    :return: A list of paths to files that match the pattern.
    """
    matches = []
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        print(files)
        for file in files:
            # If the file matches the pattern, add it to the list
            if pattern in file:
                matches.append(os.path.join(root, file))
    return matches


directory_to_search = '/home/drghodrat/Desktop/mlphysics'
pattern = 'NB19_CXVII-Keras'
found_files = search_files(directory_to_search, pattern)
print(found_files)
