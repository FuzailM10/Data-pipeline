import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch
from src.api_client import fetch_data

class TestAPIClient(unittest.TestCase):
    @patch('src.api_client.requests.get')
    def test_fetch_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'key': 'value'}
        mock_response.status_code = 200

        data = fetch_data('https://api.example.com/data')
        self.assertEqual(data, {'key': 'value'})
        mock_get.assert_called_once_with('https://api.example.com/data')

if __name__ == '__main__':
    unittest.main()
