import boto3

# Initialize the EC2 resource
myec2 = boto3.resource(
    service_name="ec2",
   
)

# Launch the EC2 instance
ec2_instances = myec2.create_instances(
    InstanceType="t2.micro",
    ImageId="ami-0ec0e125bb6c6e8ec",
    MaxCount=1,
    MinCount=1
)

# Get the ID of the launched instance
for instance in ec2_instances:
    print(f"Your instance ID: {instance.id}")
