# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    rev_lst =  []
    for i in range(len(lst)-1, -1, -1):
        rev_lst.append(lst[i])
    return rev_lst

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    count = 0
    for num in lst:
        if num == element:
            count += 1
    return count

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    new_lst = []
    for key, value1 in dct.items():
        if value == value1:
            new_lst.append(key)
    return new_lst

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    new_lst = []
    for number in lst1:
        new_lst.append(number)
    for num in lst2:
        new_lst.append(num)
    sorted_list = sorted(new_lst)
    return sorted_list
    
def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    highest = max(numbers)
    empty = []
    for num in numbers:
        if num < highest:
            empty.append(num)
    if empty != []:
        second_largest = max(empty)
    else: 
        second_largest = None
    
    return second_largest

find_second_largest([42, 42, 42])

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    if sorted(list(str1)) == sorted(list(str2)):
        return True
    else:
        return False

def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    new_lst = []
    for lists in nested_list:
        new_lst.extend(lists)

    return new_lst

def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    return list(sorted(set(lst)))

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    ab = set(lst1)
    bc = set(lst2)
    cd = list(ab.intersection(bc))
    return cd