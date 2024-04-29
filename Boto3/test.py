## WORK IN PROGRESS! ##

import boto3

# Get everything from official boto3 documentation located at: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

# Create an instance of s3
client = boto3.client('s3')

# Create S3 bucket
response = client.create_bucket(
    Bucket='shivani-demo-boto3',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1',
    },
)

# Get Access Control List of the s3 bucket
response = client.get_bucket_acl(
    Bucket='shivani-demo-boto3',
)
# Print the owner of the bucket
print(response['Owner']['DisplayName'])

