import platform
import sys
from unittest import TestCase
from unittest.mock import patch, Mock

import requests

from lambda_function import lambda_handler, build_uri, ServerException
from source_lambda_function import DataSource, Messages


class LambdaFunctionTest(TestCase):

    def test_lambda_handler_405(self):
        result = lambda_handler(DataSource.request_method_not_allowed(), None)
        self.assertEqual(405, result['statusCode'])
        self.assertEqual('405', result['body'][0]['code'])
        self.assertEqual(Messages.MSG_405_REQ.value, result['body'][0]['message'])


    def test_lambda_handler_400(self):
        result = lambda_handler(DataSource.request_invalid_json(), None)
        self.assertEqual(400, result['statusCode'])
        self.assertEqual('400', result['body'][0]['code'])
        self.assertEqual(Messages.MSG_400_JSON.value, result['body'][0]['message'])


    @patch('lambda_function.requests.request')
    def test_lambda_handler_500(self, mock_request):
        try:
            mock_request.side_effect = requests.exceptions.RequestException("Network error")
            lambda_handler(event=DataSource.request_ok(), context=None)

        except UnboundLocalError as e:

            version = sys.version
            os_name = platform.system()

            if version.startswith("3.8") and os_name == 'Linux':
                # 3.8 - Linux
                self.assertEqual(Messages.MSG_EXCEPTION_LINUX.value, str(e))

            elif version.startswith("3.12") and os_name == 'Windows':
                # 3.12 - Windows
                self.assertEqual(Messages.MSG_EXCEPTION_WINDOWS.value, str(e))

            else:
                print(os_name)
                print(version)
                assert 1 == 2


    @patch('lambda_function.requests.request')
    def test_lambda_handler_success(self, mock_request):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'{"key": "value"}'
        mock_response.headers = DataSource.headers_sample()
        mock_response.json.return_value = DataSource.response_ok()
        mock_request.return_value = mock_response
        result = lambda_handler(event=DataSource.request_ok(), context=None)
        self.assertEqual(DataSource.response_headers_ok(), result)


    def test_build_uri_query_params(self):
        result = build_uri(DataSource.request_params('query'))
        self.assertEqual(Messages.MSG_BUILD_URI_QUERY_PARAMS.value, result)


    def test_build_uri_path_params(self):
        result = build_uri(DataSource.request_params('path'))
        self.assertEqual(Messages.MSG_BUILD_URI_PATH_PARAMS.value, result)


    def test_build_uri_all(self):
        result = build_uri(DataSource.request_params('all'))
        self.assertEqual(Messages.MSG_BUILD_URI_ALL_PARAMS.value, result)


    def test_server_exception(self):
        server_exception = ServerException(500, {"error": "Message error testing"})
        self.assertEqual(500, server_exception.status_code)
        self.assertEqual({"error": "Message error testing"}, server_exception.body)
