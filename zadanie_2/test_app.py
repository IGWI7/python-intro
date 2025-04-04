import unittest
from app import *

class TestAppFunctions(unittest.TestCase):

    def setUp(self):
        self.valid_email = "test@example.com"
        self.invalid_email = "wrong@com"
        self.date_input = "2024-04-04"
        self.date_format_input = "%Y-%m-%d"
        self.date_format_output = "%d/%m/%Y"

    # Testy dla is_valid_email
    def test_valid_email(self):
        self.assertTrue(is_valid_email(self.valid_email))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email(self.invalid_email))

    def test_empty_email(self):
        self.assertFalse(is_valid_email(""))

    # Testy dla calculate_rectangle_area
    def test_area_regular(self):
        self.assertEqual(calculate_rectangle_area(5, 3), 15)

    def test_area_zero(self):
        self.assertEqual(calculate_rectangle_area(0, 10), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-1, 5)

    # Testy dla filter_and_sort_numbers
    def test_filter_and_sort_normal(self):
        self.assertEqual(filter_and_sort_numbers([5, 2, 9, 1], 4), [5, 9])

    def test_filter_and_sort_empty_result(self):
        self.assertEqual(filter_and_sort_numbers([1, 2], 5), [])

    def test_filter_and_sort_duplicates(self):
        self.assertEqual(filter_and_sort_numbers([5, 5, 5], 4), [5, 5, 5])

    # Testy dla convert_date_format
    def test_date_conversion_valid(self):
        self.assertEqual(convert_date_format(self.date_input, self.date_format_input, self.date_format_output), "04/04/2024")

    def test_date_conversion_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format("04-04-2024", self.date_format_input, self.date_format_output)

    def test_date_conversion_different_format(self):
        self.assertEqual(convert_date_format("01.01.2020", "%d.%m.%Y", "%Y/%m/%d"), "2020/01/01")

    # Testy dla is_palindrome
    def test_palindrome_simple(self):
        self.assertTrue(is_palindrome("kajak"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("Kobyła ma mały bok"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("palindrom"))

if __name__ == '__main__':
    unittest.main()
