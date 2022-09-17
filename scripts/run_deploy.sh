#!/usr/bin/env bash

root_dir=$PWD
venv_dir="$root_dir/venv/lib/python3.9/site-packages"

# Zip Package
mkdir zip && cp -r app/ zip/app/ \
&& cd $venv_dir && zip -r9 "$root_dir/lambda.zip" . \
&& cd "$root_dir/zip" && zip -g ../lambda.zip -r . \
&& cd "$root_dir" && rm -r zip

# Upload S3
bucket_name="upy-fastapi-lambda-dev"
cd $root_dir
aws s3 cp lambda.zip s3://$bucket_name/lambda.zip --profile upy

# Update Function Lambda
function_name="upy-fastapi-lambda-dev"
bucket="upy-fastapi-lambda-dev"
aws lambda update-function-code --function-name $function_name --s3-bucket $bucket --s3-key lambda.zip --profile upy
