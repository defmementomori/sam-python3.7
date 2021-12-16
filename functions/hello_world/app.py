import json
import os

env=os.environ.get("run_local")

def function_sample( num1:int, num2:int) -> int:
    return num1 + num2

def lambda_handler(event, context):
    print("run_local? {0}".format(env))
    return {
        "statusCode": 200
    }
