from urllib import response
import boto3

# Launching an EC2 instance
client=boto3.client('ec2')
resp=client.run_instances(
    ImageId='ami-01216e7612243e0ef',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
)
for instance in resp['Instances']:
    print(instance['InstanceId'])


# Stopping an ec2 instance
# ec2=boto3.resource('ec2')
# instance=ec2.Instance('i-02d581095aafc36a9')
# response=instance.stop(
#     Hibernate=False,
#     DryRun=False,
#     Force=True,
# )
# print(response['StoppingInstances'][0]['CurrentState']['Name'])

# Starting again the same ec2 Instance
# ec2=boto3.resource('ec2')
# instance=ec2.Instance('i-0bb4831dee782207a')
# response=instance.start(
#     DryRun=False,
# )
# print(response['StartingInstances'][0]['CurrentState']['Name'])

# Terminate the instance
# ec2=boto3.resource('ec2')
# instance=ec2.Instance('i-00d2692a3d75de2ed')
# response = instance.terminate(
#     DryRun=False,
# )
# print(response)