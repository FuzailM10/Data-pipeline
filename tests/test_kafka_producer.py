import unittest
from unittest.mock import patch
from src.kafka_producer import produce_messages

class TestKafkaProducer(unittest.TestCase):
    @patch('src.kafka_producer.Producer')
    def test_produce_messages(self, MockProducer):
        mock_producer = MockProducer.return_value
        produce_messages('test_topic', 'test_message')
        mock_producer.produce.assert_called_once_with('test_topic', value='test_message')
        mock_producer.flush.assert_called_once()

if __name__ == '__main__':
    unittest.main()
