from enum import Enum

URL = "viacep.com.br"

class DataSource:

    @staticmethod
    def request_invalid_json():
        return {
            "uri": f":https//{URL}",
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "queryParams": {
                "clientId": "5a33ec690adaeda2cb8d3001"
            },
            "body":  {'invalid-json'}
        }

    @staticmethod
    def request_fail():
        # This request it will cause an exception
        return {
            "uri": f"tcp://{URL}",
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "queryParams": {
                "clientId": "5a33ec690adaeda2cb8d3001"
            },
            "body": {'userName': 'user@email.com'}
        }

    @staticmethod
    def request_ok():
        return {
            "uri": f"https://{URL}",
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "queryParams": {
                "clientId": "5a33ec690adaeda2cb8d3001"
            },
            "body": {'userName': 'user@email.com'}
        }

    @staticmethod
    def do_request_ok():
        return {
            "uri": f"https://{URL}/ws/12070020/json/",
            "method": "GET",
            "headers": {
                "Content-Type": "application/json"
            }
        }

    @staticmethod
    def do_request_error():
        return {
            "uri": f"tcp://{URL}/ws/12070020/json/",
            "method": "GET",
            "headers": {
                "Content-Type": "application/json"
            }
        }

    @staticmethod
    def headers_sample():
        return  {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, compress, deflate, br",
            "Content-Type": "application/json",
            "Host": "huntercodexs",
            "request-start-time": "1731094362195",
            "User-Agent": "bruno-runtime/1.32.0",
            "x-amzn-cipher-suite": "ECDHE-RSA-AES128-GCM-SHA256",
            "x-amzn-tls-version": "TLSv1.2",
            "x-amzn-vpc-id": "vpc-041816fbca4943a91",
            "x-amzn-vpce-config": "1",
            "x-amzn-vpce-id": "vpce-02f7b507a10c065a7",
            "X-Forwarded-For": "10.97.246.149"
        }

    @staticmethod
    def response_ok():
        return {
            "statusCode": "200",
            "body": {
                "userId": "12345",
                "businessId": "67890",
                "username": "teste.testesSF4@mailinator.com"
            }
        }

    @staticmethod
    def response_body_ok_12070020():
        return {
            'cep': '12070-020',
            'logradouro': 'Travessa João Dias Cardoso Sobrinho',
            'complemento': '',
            'unidade': '',
            'bairro': 'Jardim Maria Augusta',
            'localidade': 'Taubaté',
            'uf': 'SP',
            'estado': 'São Paulo',
            'regiao': 'Sudeste',
            'ibge': '3554102',
            'gia': '6889',
            'ddd': '12',
            'siafi': '7183'}


    @staticmethod
    def response_headers_ok():
        return {
            "statusCode":200,
            "body": {
                "statusCode":"200",
                "body":{
                    "userId":"1234599999",
                    "businessId":"67890",
                    "username":"teste.testesSF4@mailinator.com"
                }
            },
            "headers":{
                "Accept":"application/json, text/plain, */*",
                "Accept-Encoding":"gzip, compress, deflate, br",
                "Content-Type":"application/json",
                "Host":"huntercodexs",
                "request-start-time":"1731094362195",
                "User-Agent":"bruno-runtime/1.32.0",
                "x-amzn-cipher-suite":"ECDHE-RSA-AES128-GCM-SHA256",
                "x-amzn-tls-version":"TLSv1.2",
                "x-amzn-vpc-id":"vpc-041816fbca4943a91",
                "x-amzn-vpce-config":"1",
                "x-amzn-vpce-id":"vpce-02f7b507a10c065a7",
                "X-Forwarded-For":"10.97.246.149"
            }
        }

    @staticmethod
    def request_method_not_allowed():
        return {
            "uri": f"https://{URL}",
            "method": "METHOD",
            "headers": {
                "Content-Type": "application/json"
            },
            "queryParams": {
                "clientId": "5a33ec690adaeda2cb8d3001"
            },
            "body": {'userName': 'user@email.com'}
        }

    @staticmethod
    def request_params(goal:str):

        if goal == 'all':
            return {
                "uri": f"https://{URL}/uri/test/v1/endpoint/{{fieldName1}}/path/{{fieldName2}}",
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                },
                "queryParams": {
                    "clientId": "5a33ec690adaeda2cb8d3001",
                    "appId": "5b391ec6f18f4f00082d59b1",
                    "principalId": "5a33ec690adaeda2cb8d3001",
                    "integrationLatency": 82,
                    "serviceId": "5b2d6db58b9a2900088176d9",
                    "isUser": "false"
                },
                "pathParams": {
                    "fieldName1": "pathParams1",
                    "fieldName2": "pathParams2"
                },
                "body": {}
            }

        elif goal == 'query':
            return {
                "uri": f"https://{URL}/uri/test/v1/endpoint",
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                },
                "queryParams": {
                    "clientId": "5a33ec690adaeda2cb8d3001",
                    "appId": "5b391ec6f18f4f00082d59b1",
                    "principalId": "5a33ec690adaeda2cb8d3001",
                    "integrationLatency": 82,
                    "serviceId": "5b2d6db58b9a2900088176d9",
                    "isUser": "false"
                },
                "body": {}
            }

        elif goal == 'path':
            return {
                "uri": f"https://{URL}/uri/test/v1/endpoint/{{fieldName1}}/path/{{fieldName2}}",
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                },
                "pathParams": {
                    "fieldName1": "pathParams1",
                    "fieldName2": "pathParams2"
                },
                "body": {}
            }


class Messages(Enum):
    MSG_BUILD_URI_QUERY_PARAMS = f"https://{URL}/uri/test/v1/endpoint?clientId=5a33ec690adaeda2cb8d3001&appId=5b391ec6f18f4f00082d59b1&principalId=5a33ec690adaeda2cb8d3001&integrationLatency=82&serviceId=5b2d6db58b9a2900088176d9&isUser=false"
    MSG_BUILD_URI_PATH_PARAMS = f"https://{URL}/uri/test/v1/endpoint/pathParams1/path/pathParams2"
    MSG_BUILD_URI_ALL_PARAMS = f"https://{URL}/uri/test/v1/endpoint/pathParams1/path/pathParams2?clientId=5a33ec690adaeda2cb8d3001&appId=5b391ec6f18f4f00082d59b1&principalId=5a33ec690adaeda2cb8d3001&integrationLatency=82&serviceId=5b2d6db58b9a2900088176d9&isUser=false"
    MSG_400_JSON = "Invalid json body."
    MSG_405_REQ = "Method not allowed: METHOD"
    MSG_500_INT = "Request failed: 'int' object has no attribute 'upper'"
    MSG_500_NONE = "Request failed: 'NoneType' object has no attribute 'upper'"
    MSG_500_CON = f"Request failed: No connection adapters were found for 'tcp://{URL}?clientId=5a33ec690adaeda2cb8d3001'"
    MSG_EXCEPTION_LINUX = "local variable 'response' referenced before assignment"
    MSG_EXCEPTION_WINDOWS = "cannot access local variable 'response' where it is not associated with a value"
    MSG_405_METHOD = {'body': [{'code': '405', 'message': 'Method not allowed: WRONG-METHOD'}], 'statusCode': 405}
