import os

from aws_lambda_powertools import Logger

region = os.environ.get("AWS_REGION")
logger = Logger(service="payment")


def function_sample(num1: int, num2: int) -> int:
    res = num1 + num2
    print(res)
    return res


def lambda_handler(event, context):

    logger.append_keys(region=region)
    logger.info("sample log")

    return {
        "statusCode": 200
    }
