import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    path_list = list()

    def file_traverse(path):
        # check to see if the path is a file and if it ends with
        # the given suffix, if it is , append to the path_list
        if os.path.isfile(path):
            if path.endswith(suffix):
                path_list.append(path)
            return
        # if the current path is a directory, if it is a direcotyr,
        # store all its subpath in a list, go over the list check
        # the path recursively
        elif os.path.isdir(path):
            temp_path_list = os.listdir(path)
            for sub_path in temp_path_list:
                joined_path = os.path.join(path, sub_path)
                file_traverse(joined_path)
        else:
            return

    file_traverse(path)

    return path_list


# Test Case 1
print(find_files(".c", "testdir"))
print(find_files(".h", "testdir"))
print(find_files(".gitkeep", "testdir"))

# Test Case 2, None input
try:
    print(find_files(None, "testdir"))
except Exception:
    print("End of file arg cannot be None")

try:
    print(find_files(1, "testdir"))
except Exception:
    print("End of file arg cannot be number")

try:
    print(find_files(".c", None))
except Exception:
    print("File path cannot be None")


# Test Case 3
try:
    print(find_files(' ', "testdir"))
except Exception:
    print("End of file arg is invalid")
try:
    print(find_files('', "testdir"))
except Exception:
    print("End of file arg is invalid")
