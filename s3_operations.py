import boto3

def upload_to_s3(file_name, bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"{file_name} uploaded to {bucket_name} successfully.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    file_name = 'voice.mp3'  
    bucket_name = 'myprojectbucket-01'  
    upload_to_s3(file_name, bucket_name)
