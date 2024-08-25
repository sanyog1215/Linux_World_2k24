import boto3

def upload_object_to_s3():
    s3 = boto3.client('s3')
    file_name_with_path = input("Enter the file name with path to upload: ")
    bucket = input("Enter the S3 bucket name: ")
    file_name = input("enter the file name to display: ")

    try:
        s3.upload_file(file_name_with_path, bucket, file_name)
        print(f"File '{file_name}' uploaded successfully to '{bucket}'.")
    except Exception as e:
        print(f"Error: {e}")

upload_object_to_s3()