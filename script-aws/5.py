import boto3
region = 'us-east-2'
instances = ['i-0600b5889ba3288c1',]
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
lambda_handler("1","2")