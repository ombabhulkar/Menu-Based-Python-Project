import boto3

def process_email_ids(event, context):
    s3 = boto3.client('s3')
    ses = boto3.client('ses')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    email_data = response['Body'].read().decode('utf-8').splitlines()

    for email in email_data:
        ses.send_email(
            Source='babhulkarom09@gmail.com',
            Destination={'ob.ombabhulkar@gmail.com': [email]},
            Message={
                'Subject': {'Data': 'Testing'},
                'Body': {'Text': {'Data': 'Hello, How are you?'}}
            }
        )
        print(f"Email sent to: {email}")
