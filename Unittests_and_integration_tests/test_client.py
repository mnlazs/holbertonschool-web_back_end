#!/usr/bin/env python3
""" Casos de Prueba"""

import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
import utils
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Test that json can be got """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """ Test the org of the client """
        get_patch.return_value = expected
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/"+org)

    def test_public_repos_url(self):
        """ test that _public_repos_url works """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """Haciendo pruebas de repositorios publicos"""
        maria = {"name": "maria", "license": {"key": "a"}}
        pedro = {"name": "pedro", "license": {"key": "b"}}
        juan = {"name": "juan"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [maria, pedro, juan]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ["maria", "pedro", "juan"])
            self.assertEqual(x.public_repos("a"), ["maria"])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos("45"), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()
