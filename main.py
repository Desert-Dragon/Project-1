"""
    Searches deep inside a directory structure, looking for duplicate file.
    Duplicates aka copies have the same content, but not necessarily the same name.
"""
__author__ = "Dustin Edward Deleon Johnson"
__email__ = "squirttle123@gmail.com"
__version__ = "1.0"

# noinspection PyUnresolvedReferences
from os.path import getsize, join

# noinspection PyUnresolvedReferences
from p1utils import all_files, compare


def search(file_list):
    """Looking for duplicate files in the provided list of files
    :returns a list of lists, where each list contains files with the same content

    Basic search strategy goes like this:
    - until the provided list is empty.
    - remove the 1st item from the provided file_list
    - search for its duplicates in the remaining list and put the item and all its duplicates into a new list
    - if that new list has more than one item (i.e. we did find duplicates) save the list in the list of lists
    As a result we have a list, each item of that list is a list,
    each of those lists contains files that have the same content
    """
    lol = []
    current_files = []
    F_list = []
    T_list = []
    while len(file_list) > 2:
        if len(current_files) < 1:
            z = file_list.pop(0)
            current_files.append(z)
            if len(current_files) < 3:
                u = file_list.pop(0)
                current_files.append(u)
        if len(file_list) > 1:
            if getsize(z) == getsize(u):
                T_list.append(u)
                current_files.pop(-1)
            else:
                F_list.append(u)
                current_files.pop(-1)
                if len(T_list) == 0:
                    current_files.pop(0)
    lol.append(T_list)
    if len(F_list) > 1:
        T_list = []
        search(F_list)
    return lol


def faster_search(file_list):
    """Looking for duplicate files in the provided list of files
    :returns a list of lists, where each list contains files with the same content

    Here's an idea: executing the compare() function seems to take a lot of time.
    Therefore, let's optimize and try to call it a little less often.
    """
    lol = []
    #
    # ...
    #
    return lol


def report(lol):
    """ Prints a report
    :param lol: list of lists (each containing files with equal content)
    :return: None
    Prints a report:
    - longest list, i.e. the files with the most duplicates
    - list where the items require the largest amount or disk-space
    """
    maximum = max(lol)
    i = []
    for e in lol:
        i.append(e)
    space = i  # I was stuck on this piece of the code for a decent amount of time, for the moment it will have to stay so i can get this in on time,
    print("== == Duplicate File Finder Report == ==")

    if len(lol) > 0:
        print(f"The file with the most duplicates is {maximum}")
        print(f"and the files that are taking up the most space are: {space}")
    else:
        print("No duplicates found")


if __name__ == '__main__':
    path = join(".", "images")

# measure how long the search and reporting takes:
# t0 = time()
# report(search(all_files(path)))
# print(f"Runtime: {time() - t0:.2f} seconds")
# #
# print("\n\n .. and now w/ a faster search implementation:")

# measure how long the search and reporting takes:
# t0 = time()
# report(faster_search(all_files(path)))
# print(f"Runtime: {time() - t0:.2f} seconds")

report(search(all_files(path)))
