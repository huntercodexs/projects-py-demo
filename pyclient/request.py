import http.client
import json

conn = http.client.HTTPSConnection('viacep.com.br')

headers = {'Content-type': 'application/json'}

conn.request('GET', '/ws/12090002/json/', 'null', headers)

response = conn.getresponse()
print(response.read().decode())

# -----

import http.client
import json

def lambda_handler(event, context):
    

    code = event['postalcode'];
    conn = http.client.HTTPSConnection('viacep.com.br')
    headers = {'Content-type': 'application/json'}


    conn.request('GET', '/ws/'+code+'/json/', 'null', headers)
    response = json.loads(conn.getresponse().read().decode())


    return response

