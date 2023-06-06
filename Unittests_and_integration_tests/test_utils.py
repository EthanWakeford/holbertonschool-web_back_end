#!/usr/bin/env python3
"""testing for util.py"""
import unittest
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """testing for access_nest_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nest_map, path, expected):
        """testing method"""
        self.assertEqual(utils.access_nested_map(nest_map, path), expected)
