import json
from urllib.parse import urlencode

import requests

from exception import ServerException


class RequestHandlerAPI:

    def __init__(self, method):
        self.__method = method.upper()


    @staticmethod
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


    def check_http_method(self):
        print("\nCALL >>> check_http_method")
        if not self.__method or self.__method not in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD']:
            return {
                'statusCode': 405,
                'body': [{'code': '405', 'message': f'Method not allowed: {self.__method}'}]
            }


    def encode_body(self, event):
        print("CALL >>> encode_body")
        encoded_body = None

        if self.__method in ['POST', 'PUT', 'PATCH']:
            try:
                body = event.get('body', {})
                encoded_body = json.dumps(body).encode('utf-8')

            except (TypeError, ValueError):
                return {
                    'statusCode': 400,
                    'body': [{'code': '400', 'message': 'Invalid json body.'}]
                }

        return encoded_body


    def do_request(self, event, encoded_body):
        print("CALL >>> do_request")
        try:
            headers = event.get('headers', {})
            headers = {k: v for k, v in headers.items()}

            response = requests.request(method=self.__method, url=self.build_uri(event), headers=headers, data=encoded_body)

            print("===[response]> ")
            print(response)
            print(response.json())

            return response

        except requests.exceptions.RequestException as e:
            err = [{'code': '500', 'message': f'Request failed: {str(e)}'}]
            return {'statusCode': 500, 'body': err}


    @staticmethod
    def check_response(response):
        print("CALL >>> check_response")
        response_body = None
        if response.content:
            response_body = response.json()

            if 500 <= response.status_code <= 599:
                raise ServerException(response.status_code, response_body)

        return response_body

    @staticmethod
    def build_response(response, response_body):
        print("CALL >>> build_response")
        return {
            'statusCode': response.status_code,
            'body': response_body,
            'headers': dict(response.headers)
        }

