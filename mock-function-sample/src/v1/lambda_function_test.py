from unittest import TestCase
from unittest.mock import patch, Mock

from lambda_function import some_function, some_function_requests


class LambdaFunctionTest(TestCase):

    def test_some_function_not_mocking(self):
        result = some_function(event={}, context=None)
        self.assertEqual({'body': 'message body'}, result)


    def test_some_function_requests_not_mocking(self):
        result = some_function_requests(event={}, context=None)
        self.assertEqual({'body': 200, 'method': {'body': 'message body'}}, result)


    def test_some_function_mocking(self):
        with patch('module.Foo') as mock_foo:
            instance = mock_foo.return_value
            instance.method.return_value = 'result'
            result = some_function(event={}, context=None)
            self.assertEqual('result', result)


    def test_some_function_requests_mocking(self):
        with patch('lambda_function.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 202
            mock_response.content = b'{"key": "value"}'
            mock_response.headers = {}
            mock_response.json.return_value = {'body': 202, 'method': {'body': 'message body'}}
            mock_get.return_value = mock_response
            result = some_function_requests(event={}, context=None)
            self.assertEqual({'body': 202, 'method': {'body': 'message body'}}, result)
