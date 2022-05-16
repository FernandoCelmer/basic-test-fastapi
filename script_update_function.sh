#!/usr/bin/env bash

function_name="upy-fastapi-lambda-dev"
bucket="upy-fastapi-lambda-dev"
aws lambda update-function-code --function-name $function_name --s3-bucket $bucket --s3-key lambda.zip --profile upy
