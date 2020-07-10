# How to boto3

## The purpose
Connect to AWS-service using Python.

## How does it work?
...

## Useful commands
Read a text file from S3 (to memory)
```
S3_key = "something/something/log.txt"
bucket_name = "my_bucket_name"
s3 = boto3.resource('s3')
obj = s3.Object(bucket_name, S3_key)
filecontent = obj.get()['Body'].read().decode('utf-8')
````

## Useful links
[Oslo kommune](https://www.oslo.kommune.no/)

