#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test a list with ordered positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_unordered_list(self):
        """Test a list with unordered positive integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
    
    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers"""
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)
    
    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)
    
    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)
    
    def test_identical_elements(self):
        """Test a list with identical elements"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
    
    def test_large_numbers(self):
        """Test a list with very large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
    
if __name__ == "__main__":
    unittest.main()
