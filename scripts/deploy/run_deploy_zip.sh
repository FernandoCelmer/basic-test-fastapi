#!/usr/bin/env bash

root_dir=$PWD
venv_dir="$root_dir/venv/lib/python3.9/site-packages"
function_name="upy-fastapi-lambda-dev"
bucket_name="upy-fastapi-lambda-dev"
file_name="upy-0.0.1.zip"


# Zip Package
mkdir zip && cp -r app/ zip/app/ && cp -r config.py zip/config.py && cp -r sql_app.db zip/sql_app.db \
&& cd $venv_dir && zip -r9 "$root_dir/$file_name" . \
&& cd "$root_dir/zip" && zip -g ../$file_name -r . \
&& cd "$root_dir" && rm -r zip

# Upload S3
cd $root_dir
aws s3 cp $file_name s3://$bucket_name/$file_name --profile upy

# Update Lambda Function 
aws lambda update-function-code --function-name $function_name --s3-bucket $bucket_name --s3-key $file_name --profile upy