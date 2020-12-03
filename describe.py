import boto3
import botocore
from botocore.exceptions import ClientError
import json

'''try:
    ec2 = boto3.resource('ec2')
    vpc = ec2.Vpc('vpc-06d96b9aa0b485ac8')
    print(vpc)
    client=boto3.client('ec2')

    response = client.describe_vpcs()
   # VpcIds=[
    #    'vpc-06d96b9aa0b485ac8',
    #],


    print(response)
except ClientError as error:
    print(error.response['Error']['Message'])
    #raise error

#except botocore.exceptions.ParamValidationError as error:
 #   raise ValueError('The parameters you provided are incorrect: {}'.format(error))

'''
client=boto3.client('ec2')
response = client.describe_vpcs()
print(response)
json_object = json.dumps(response, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 
