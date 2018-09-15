#!/bin/bash
directory=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) 
echo $directory
$directory/python3-env/bin/python $directory/core.py
