import json
import pytest
import boto3
import re
import os
from functions.hello_world import app as app_hello


def test_echo():
    print("pytest start")
    app_hello.lambda_handler("","")

def test_function_sample():
    assert app_hello.function_sample(2,3)==5

