import boto3
import botocore
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
'''response = s3.list_buckets()
text_file = open("Output.txt", "w", encoding='UTF-8')
    
# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    text_file.write(str(bucket["Name"]))
    print(f'  {bucket["Name"]}')'''

response = s3.create_bucket(
    ACL="public-read-write",
    bucketname="jdmnewawsbucket",
    CreateBucketConfiguration={
        'LocationConstraint': "us-west-2",
    },
    )
bucket = s3.Bucket('name')
try:
    response = s3.upload_file('KT.png','bucket','KT.png')
except ClientError as e:
    logging.error(e)
   



