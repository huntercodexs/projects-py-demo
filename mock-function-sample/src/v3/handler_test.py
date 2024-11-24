from unittest import TestCase
from unittest.mock import Mock

from exception import ServerException
from handler import RequestHandlerAPI
from source import Messages, DataSource


class RequestHandlerAPITest(TestCase):

    @staticmethod
    def __setup(method):
        return RequestHandlerAPI(method)

    def test_lambda_handler_check_http_method(self):
        instance = self.__setup('WRONG-METHOD')
        self.assertEqual(Messages.MSG_405_METHOD.value, instance.check_http_method())

    def test_lambda_handler_encode_body__GET__(self):
        instance = self.__setup('GET')
        result = instance.encode_body(DataSource.request_ok())
        self.assertEqual(None, result)

    def test_lambda_handler_encode_body__POST__(self):
        instance = self.__setup('POST')
        result = instance.encode_body(DataSource.request_ok())
        self.assertEqual(b'{"userName": "user@email.com"}', result)
        self.assertEqual('user@email.com', result.decode('utf-8').split('"')[3])

    def test_lambda_handler_encode_body__POST_400__(self):
        instance = self.__setup('POST')
        result = instance.encode_body(DataSource.request_invalid_json())
        self.assertEqual(400, result['statusCode'])
        self.assertEqual(Messages.MSG_400_JSON.value, result['body'][0]['message'])

    def test_lambda_handler_do_request__GET_OK__(self):
        instance = self.__setup('GET')
        encoded_body = instance.encode_body(DataSource.do_request_ok())
        response  = instance.do_request(DataSource.do_request_ok(), encoded_body)
        response_body = instance.check_response(response)
        result = instance.build_response(response, response_body)
        self.assertEqual(200, result.get('statusCode'))
        self.assertEqual(DataSource.response_body_ok_12070020(), result.get('body'))

    def test_lambda_handler_do_request__FAIL_500__(self):
        instance = self.__setup('GET')
        encoded_body = instance.encode_body(DataSource.do_request_error())
        response  = instance.do_request(DataSource.do_request_error(), encoded_body)
        self.assertEqual(500, response['statusCode'])
        self.assertEqual('500', response['body'][0]['code'])
        self.assertRegex(response['body'][0]['message'], '^Request failed:')

    def test_lambda_handler_check_response(self):
        instance = self.__setup('POST')
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = DataSource.response_ok()
        result = instance.check_response(mock_response)
        self.assertEqual(DataSource.response_ok(), result)

    def test_lambda_handler_check_response__500__(self):
        instance = self.__setup('POST')
        mock_response = Mock()
        mock_response.status_code = 500
        with self.assertRaises(ServerException):
            instance.check_response(mock_response)

    def test_lambda_handler_build_uri__query_params__(self):
        instance = self.__setup('POST')
        result = instance.build_uri(DataSource.request_params('query'))
        self.assertEqual(Messages.MSG_BUILD_URI_QUERY_PARAMS.value, result)

    def test_lambda_handler_build_uri__path_params__(self):
        instance = self.__setup('POST')
        result = instance.build_uri(DataSource.request_params('path'))
        self.assertEqual(Messages.MSG_BUILD_URI_PATH_PARAMS.value, result)

    def test_lambda_handler_build_uri__all__(self):
        instance = self.__setup('POST')
        result = instance.build_uri(DataSource.request_params('all'))
        self.assertEqual(Messages.MSG_BUILD_URI_ALL_PARAMS.value, result)

