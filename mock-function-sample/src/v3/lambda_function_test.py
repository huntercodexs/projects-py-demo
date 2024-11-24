from unittest import TestCase
from unittest.mock import patch, Mock

from lambda_function import lambda_handler
from source import DataSource


class LambdaFunctionTest(TestCase):

    def test_lambda_handler_no_mocking(self):
        result = lambda_handler(DataSource.do_request_ok(), None)
        self.assertEqual(DataSource.response_body_ok_12070020(), result["body"])


    @patch('handler.requests.request')
    @patch('handler.RequestHandlerAPI.build_response')
    def test_lambda_handler_mocking_parts(self, mock_build_response, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'{"key": "value"}'
        mock_response.headers = {}
        mock_response.json.return_value = DataSource.response_ok()
        mock_requests.return_value = mock_response

        mock_build_response.return_value = {'statusCode': 200, 'body': 'mocked_response_body'}

        result = lambda_handler(event=DataSource.do_request_ok(), context=None)
        self.assertEqual({'statusCode': 200, 'body': 'mocked_response_body'}, result)


    @patch('handler.RequestHandlerAPI.check_http_method')
    @patch('handler.RequestHandlerAPI.encode_body')
    @patch('handler.RequestHandlerAPI.do_request')
    @patch('handler.RequestHandlerAPI.check_response')
    @patch('handler.RequestHandlerAPI.build_response')
    def test_lambda_handler_mocking(self, mock_build_response, mock_check_response, mock_do_request, mock_encode_body, mock_check_method):
        mock_check_method.return_value = {}
        mock_encode_body.return_value = {}
        mock_do_request.return_value = {}
        mock_check_response.return_value = {}
        mock_build_response.return_value = {}

        result = lambda_handler(event=DataSource.do_request_ok(), context=None)
        self.assertEqual({}, result)

