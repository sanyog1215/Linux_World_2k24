import boto3

ec2 = boto3.resource('ec2')
print("Launching EC2 instance with RHEL GUI...")

instances = ec2.create_instances(
    ImageId='ami-022ce6f32988af5fa',  # Replace with a RHEL AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='redhat9_key',  # Ensure this key pair exists
    SecurityGroups=['launch-wizard-5'],  # Replace with your security group
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'RHEL-GUI-Instance'}]
        }
    ],
)

print(f"Instance {instances[0].id} launched successfully.")


