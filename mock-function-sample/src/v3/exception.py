class ServerException(Exception):
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body
        error_message = {'statusCode': status_code, 'body': body}
        error_message = str(error_message).replace("\"", "")
        error_message = str(error_message).replace("'", "\"")
        super().__init__(error_message)

