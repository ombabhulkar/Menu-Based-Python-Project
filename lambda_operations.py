import boto3

def trigger_transcribe_on_upload(event, context):
    transcribe = boto3.client('transcribe')
    s3_object = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    job_name = f"TranscribeJob-{s3_object.split('.')[0]}"

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': f"s3://{bucket_name}/{s3_object}"},
        MediaFormat='mp3',  
        LanguageCode='en-US',
        OutputBucketName=bucket_name
    )
    print(f"Transcription job {job_name} started for file {s3_object}.")
