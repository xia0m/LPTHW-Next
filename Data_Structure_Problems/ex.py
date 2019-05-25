## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
# print(os.listdir("."))
# dir_list = os.listdir("./testdir")
# print(dir_list)
# for path in dir_list:
#     # if os.path.isdir(path):
#     the_path = os.path.join("testdir", path)
#     print(the_path)
#     print(os.path.isdir(the_path))


# def find_files(suffix, path):
#     path_list = list()

#     def file_traverse(path):
#         if not os.path.isdir(path):
#             return
#         temp_path_list = os.listdir(path)
#         for a_path in temp_path_list:
#             joined_path = os.path.join(path, a_path)
#             if os.path.isdir(joined_path):
#                 file_traverse(joined_path)
#             else:
#                 if os.path.isfile(joined_path) and joined_path.endswith(suffix):
#                     path_list.append(joined_path)
#     if os.path.isdir(path):
#         temp_path_list = os.listdir(path)
#         for a_path in temp_path_list:
#             joined_path = os.path.join(path, a_path)
#             if os.path.isdir(joined_path):
#                 file_traverse(joined_path)
#                 # print(joined_path)
#             elif os.path.isfile(joined_path):
#                 if joined_path.endswith(suffix):
#                     path_list.append(joined_path)
#     return path_list

def find_files(suffix, path):
    path_list = list()

    def file_traverse(path):
        if os.path.isfile(path):
            if path.endswith(suffix):
                path_list.append(path)
            return
        elif os.path.isdir(path):
            temp_path_list = os.listdir(path)
            for sub_path in temp_path_list:
                joined_path = os.path.join(path, sub_path)
                file_traverse(joined_path)
        else:
            return
    file_traverse(path)

    return path_list


print(find_files(".c", "testdir"))

# Let us check if this file is indeed a file!
print(os.path.isfile("./ex.py"))

# Does the file end with .py?
print("./ex.py".endswith(".py"))
