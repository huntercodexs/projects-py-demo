from unittest import TestCase
from unittest.mock import patch

from exception import ServerException


class ServerExceptionTest(TestCase):

    @patch('exception.ServerException.__init__', return_value=None)
    def test_exception(self, mock_init):
        status_code = 500
        body = {'message': 'Internal Error'}
        mock_init.error_message = {'statusCode': 500, 'body': {'message': 'Internal Error'}}

        exception = ServerException(status_code, body)

        mock_init.assert_called_once_with(status_code, body)
        self.assertEqual("(500, {'message': 'Internal Error'})", str(exception))

