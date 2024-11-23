import requests

import module


def some_function(event, context):
    instance = module.Foo()
    return instance.method()

def some_function_requests(event, context):
    instance = module.Foo()
    response = requests.get('https://huntercodexs.com')
    print(f'>>>>+{response}')
    method_call = instance.method()
    return {
        "method": method_call,
        "body": response.status_code
    }

