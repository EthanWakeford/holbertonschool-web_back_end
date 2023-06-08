#!/usr/bin/env python3
"""testing for util.py"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nest_map, path, expected):
        """testing task 2"""
        with self.assertRaises(expected):
            utils.access_nested_map(nest_map, path)


class TestGetJson(unittest.TestCase):
    """tests get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, payload, expected):
        """tests get_json"""
        mock_response = Mock()
        mock_response.json.return_value = payload
        with patch('requests.get', return_value=mock_response) as mock_get:
            response = utils.get_json(url)
            mock_get.assert_called_once_with(url)
            self.assertEqual(response, payload)
