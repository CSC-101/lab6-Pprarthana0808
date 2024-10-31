import data
import lab6
import unittest
from lab6 import selection_sort_books, swap_case, str_translate, histogram
from data import Book
# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_empty(self):
        books = []
        selection_sort_books(books)
        expected = []
        self.assertEqual(expected, books)

    def test_selection_sort_books(self):
        books = [Book(["F. Scott Fitzgerald"], "The Great Gatsby"), Book(["Herman Melville"], "Moby Dick"),Book(["Harper Lee"], "To Kill a Mockingbird")]
        selection_sort_books(books)
        expected_titles = ["Moby Dick", "The Great Gatsby", "To Kill a Mockingbird"]
        self.assertEqual([book.title for book in books], expected_titles)
    # Part 2
    def test_swap_case_one(self):
        input = "Hello World"
        expected_output = "hELLO wORLD"
        self.assertEqual(swap_case(input), expected_output)
    def test_swap_case_two(self):
        input = "Computer Science"
        expected_output = "cOMPUTER sCIENCE"
        self.assertEqual(swap_case(input), expected_output)

    # Part 3
    def test_str_translate_one(self):
        input_str = 'abcdcba'
        old_char = 'a'
        new_char = 'x'
        expected_output = 'xbcdcbx'
        self.assertEqual(str_translate(input_str, old_char, new_char), expected_output)

    def test_str_translate_two(self):
        input_str = 'hello'
        old_char = 'h'
        new_char = 'm'
        expected_output = 'mello'
        self.assertEqual(str_translate(input_str, old_char, new_char), expected_output)
    # Part 4
    def test_histogram_one(self):
        paragraph = "apple banana apple orange banana apple"
        histogram_result = histogram(paragraph)
        self.assertEqual(histogram_result.get('grape'), None)

    def test_histogram_basic(self):
        paragraph = "apple banana apple orange banana apple"
        histogram_result = histogram(paragraph)
        self.assertEqual(histogram_result.get("apple"),3)

    def test_histogram_empty(self):
        paragraph = ""
        histogram_result = histogram(paragraph)
        self.assertEqual(histogram_result, {})


if __name__ == '__main__':
    unittest.main()
