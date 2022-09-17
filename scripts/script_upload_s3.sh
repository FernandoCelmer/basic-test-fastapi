#!/usr/bin/env bash

root_dir=$PWD
bucket_name="upy-fastapi-lambda-dev"
cd $root_dir
aws s3 cp lambda.zip s3://$bucket_name/lambda.zip --profile upy