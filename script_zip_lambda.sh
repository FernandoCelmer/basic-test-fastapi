#!/usr/bin/env bash

root_dir=$PWD
venv_dir="$root_dir/venv/lib/python3.9/site-packages"
cd $venv_dir && zip -r9 "$root_dir/lambda.zip" . \
&& cd "$root_dir/app" && zip -g ../lambda.zip -r .