#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    
    @patch('utils.request.get')
    def test_get_json(self, mock_get):
        #definiendo los casos de prueba
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
        # Iterar a través de los casos de prueba
        for test_url, test_payload in test_cases:
            # Crear un objeto Mock para la respuesta
            mock_response = Mock()
            # Configurar el método json del objeto Mock para que devuelva el test_payload
            mock_response.json.return_value = test_payload
            # Configurar el valor de retorno del método get del objeto Mock
            mock_get.return_value = mock_response

            # Llamar a la función get_json con el test_url
            resultado = get_json(test_url)

            # Asegurar que el método get simulado se llamó exactamente una vez con test_url como argumento
            mock_get.assert_called_once_with(test_url)

            # Asegurar que el resultado de get_json es igual a test_payload
            self.assertEqual(resultado, test_payload)

    
    
    
    

    if __name__ == '__main__':
        unittest.main()
    