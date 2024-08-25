import boto3

def access_cloud_logs():
    # Initialize the CloudWatch Logs client
    logs = boto3.client('logs')
    
    # User input for log group and log stream
    log_group = input("Enter the CloudWatch log group name: ")
    log_stream = input("Enter the CloudWatch log stream name: ")

    try:
        # Fetch log events from the specified log group and log stream
        response = logs.get_log_events(
            logGroupName=log_group,
            logStreamName=log_stream,
            startFromHead=True  # Set to True to start from the oldest log events
        )
        
        # Print each log event
        for event in response['events']:
            print(event['message'])

    except logs.exceptions.ResourceNotFoundException:
        print("The specified log group or log stream does not exist.")
    except logs.exceptions.ClientError as e:
        print(f"An error occurred: {e}")

# Call the function to access CloudWatch logs
access_cloud_logs()
