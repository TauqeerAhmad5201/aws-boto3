import boto3

session = boto3.Session()
ec2 = session.resource('ec2')

def delete_instance(instance_id):
    ec2.instances.filter(InstanceIds=[instance_id]).terminate()
    print(f"Instance {instance_id} has been terminated.")

# Call the function with the instance ID of the instance you want to delete
delete_instance('i-0fca396e0b2d630d0')