import sys 
import os
import pytest
import json
import boto3

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../functions/"))

def set_environment_variable(json_filepath):
    """Jsonを読み込み環境変数にセットする."""
    with open(f"./{json_filepath}") as filedata:
        for key, value in json.load(filedata).items():
            os.environ[key] = value

#環境変数をセット
set_environment_variable('./tests/variable.local.json')

