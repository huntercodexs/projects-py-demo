
# role
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Sid": "VirtualEditor0",
#       "Effect": "Allow",
#       "Action": "states:StartExecution",
#       "Principal": {
#         "AWS": "905418367021"
#         },
#       "Resource": [
#         {
#           "*"
#         }
#       ]
#     }
#   ]
# }

# policy
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": "sts:AssumeRole",
#             "Principal": {
#                 "AWS": "905418367021"
#             },
#             "Condition": {}
#         }
#     ]
# }

# definition
# {
#   "Comment": "Step Function From Lambda Test",
#   "StartAt": "Pass",
#   "States": {
#     "Pass": {
#       "Type": "Pass",
#       "Parameters": {
#         "MessageBody": {
#           "TransactionId.$": "$.TransactionId",
#           "Type.$": "$.Type"
#         }
#       },
#       "End": true
#     }
#   }
# }

# input
# {
#   "MessageBody": {
#     "TransactionId.$": "$.TransactionId",
#     "Type.$": "$.Type"
#   }
# }


import json
import boto3
import uuid

client = boto3.client('stepfunctions')

def lambda_handler(event, context):
  transactionId = str(uuid.uuid1())

  input = {'TransactionId': transactionId, 'Type': 'PURCHASE'}

  response = client.start_execution(
    stateMachineArn='YOUR ARN HERE!',
    name=transactionId,
    input=json.dumps(input) 
    )