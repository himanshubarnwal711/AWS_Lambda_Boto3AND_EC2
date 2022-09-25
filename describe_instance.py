import boto3

client=boto3.client('ec2')
resp=client.describe_instances(
    Filters=[{
        'Name':'tag:Name',
        'Values':['QA']
    }]
)
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID is - {}".format(instance['InstanceId']))
