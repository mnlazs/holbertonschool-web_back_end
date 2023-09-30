#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the nested map."),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested map."),
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected_exception_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        
        # Verificando el mensaje de excepción
        actual_exception_message = str(context.exception)
        self.assertEqual(actual_exception_message, expected_exception_message)

    if __name__ == '__main__':
        unittest.main()
    