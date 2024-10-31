import data
from typing import Optional
from data import Book
# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 1
def selection_sort_books(books: list[Book]) -> None:
    for i in range(len(books)):
        min_index = i
        for j in range(i + 1, len(books)):
            if books[j].title < books[min_index].title:
                min_index = j
        books[i], books[min_index] = books[min_index], books[i]
# Part 2
def swap_case(input_str: str) -> str:
    result = ''
    for char in input_str:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result
# Part 3
def str_translate(input_str: str, old: str, new: str) -> str:
    result = ''
    for char in input_str:
        if char == old:
            result += new
        else:
            result += char
    return result
# Part 4
def histogram(paragraph: str) -> dict[str, int]:
    word_count = {}
    words = paragraph.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
