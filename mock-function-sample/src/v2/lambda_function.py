import json
from urllib.parse import urlencode

import requests


def lambda_handler(event, context):

    try:

        method = event.get('method', '').upper()
        if not method or method not in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD']:
            return {
                'statusCode': 405,
                'body': [{'code': '405', 'message': f'Method not allowed: {method}'}]
            }

        encoded_body = None
        if method in ['POST', 'PUT', 'PATCH']:
            try:
                body = event.get('body', {})
                encoded_body = json.dumps(body).encode('utf-8')
            except (TypeError, ValueError):
                return {
                    'statusCode': 400,
                    'body': [{'code': '400', 'message': 'Invalid json body.'}]
                }

        headers = event.get('headers', {})
        headers = {k: v for k, v in headers.items()}

        response = requests.request(method=method, url=build_uri(event), headers=headers, data=encoded_body)

        response_body = None
        if response.content:
            response_body = response.json()

        if 500 <= response.status_code <= 599:
            raise ServerException(response.status_code, response_body)

        return {'statusCode': response.status_code, 'body': response_body, 'headers': dict(response.headers)}

    except requests.exceptions.RequestException as e:
        err = [{'code': '500', 'message': f'Request failed: {str(e)}'}]
        return {'statusCode': response.status_code, 'body': err}


def build_uri(event):
    value_uri = event.get('uri')
    path_params = event.get('pathParams', {})
    query_params = event.get('queryParams', {})

    if path_params:
        for key, value in path_params.items():
            value_uri = value_uri.replace(f"{{{key}}}", str(value))

    uri = f"{value_uri}"
    if query_params:
        uri += f"?{urlencode(query_params)}"

    return uri


class ServerException(Exception):
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body
        error_message = {'statusCode': status_code, 'body': body}
        error_message = str(error_message).replace("\"", "")
        error_message = str(error_message).replace("'", "\"")
        super().__init__(error_message)
