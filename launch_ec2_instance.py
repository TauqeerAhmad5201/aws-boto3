import boto3

session = boto3.Session()
ec2 = session.resource('ec2')

def launch_instance():
    instances = ec2.create_instances(
        ImageId='ami-03f4878755434977f',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='boto3',
        SecurityGroupIds=['sg-04f2cfd7cb63e928e'],
        UserData='#!/bin/bash\n'
                 '# Your userdata script here\n'
                 'echo "Hello from userdata"'
    )
    instance = instances[0]
    instance.wait_until_running()
    instance.reload()
    print("Instance ID:", instance.id)
    print("Public IP:", instance.public_ip_address)

launch_instance()