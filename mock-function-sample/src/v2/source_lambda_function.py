from enum import Enum

class DataSource:

    @staticmethod
    def request_invalid_json():
        return {
            "uri": ":https//huntercodexs.com.br/security/iam/v1/user-identities/retrieve-identity",
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
            "uri": "tcp://huntercodexs.com.br/security/iam/v1/user-identities/retrieve-identity",
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
            "uri": "https://huntercodexs.com.br/security/iam/v1/user-identities/retrieve-identity",
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
            "statusCode": "201",
            "body": {
                "userId": "12345",
                "businessId": "67890",
                "username": "teste.testesSF4@mailinator.com"
            }
        }

    @staticmethod
    def response_headers_ok():
        return {
            "statusCode":200,
            "body": {
                "statusCode":"201",
                "body":{
                    "userId":"12345",
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
            "uri": "https://huntercodexs.com.br/security/iam/v1/user-identities/retrieve-identity",
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
                "uri": "https://test.huntercodexs.com.br/uri/test/v1/endpoint/{fieldName1}/path/{fieldName2}",
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
                "uri": "https://test.huntercodexs.com.br/uri/test/v1/endpoint",
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
                "uri": "https://test.huntercodexs.com.br/uri/test/v1/endpoint/{fieldName1}/path/{fieldName2}",
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
    MSG_BUILD_URI_QUERY_PARAMS = "https://test.huntercodexs.com.br/uri/test/v1/endpoint?clientId=5a33ec690adaeda2cb8d3001&appId=5b391ec6f18f4f00082d59b1&principalId=5a33ec690adaeda2cb8d3001&integrationLatency=82&serviceId=5b2d6db58b9a2900088176d9&isUser=false"
    MSG_BUILD_URI_PATH_PARAMS = "https://test.huntercodexs.com.br/uri/test/v1/endpoint/pathParams1/path/pathParams2"
    MSG_BUILD_URI_ALL_PARAMS = "https://test.huntercodexs.com.br/uri/test/v1/endpoint/pathParams1/path/pathParams2?clientId=5a33ec690adaeda2cb8d3001&appId=5b391ec6f18f4f00082d59b1&principalId=5a33ec690adaeda2cb8d3001&integrationLatency=82&serviceId=5b2d6db58b9a2900088176d9&isUser=false"
    MSG_400_JSON = "Invalid json body."
    MSG_405_REQ = "Method not allowed: METHOD"
    MSG_500_INT = "Request failed: 'int' object has no attribute 'upper'"
    MSG_500_NONE = "Request failed: 'NoneType' object has no attribute 'upper'"
    MSG_500_CON = "Request failed: No connection adapters were found for 'tcp://huntercodexs.com.br/security/iam/v1/user-identities/retrieve-identity?clientId=5a33ec690adaeda2cb8d3001'"
    MSG_EXCEPTION_LINUX = "local variable 'response' referenced before assignment"
    MSG_EXCEPTION_WINDOWS = "cannot access local variable 'response' where it is not associated with a value"
