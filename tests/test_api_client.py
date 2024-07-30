import unittest
from src.api_client import fetch_data

class TestAPIClient(unittest.TestCase):
    def test_fetch_data(self):
        data = fetch_data('https://api.example.com/data')
        self.assertIsInstance(data, dict)

if __name__ == '__main__':
    unittest.main()
