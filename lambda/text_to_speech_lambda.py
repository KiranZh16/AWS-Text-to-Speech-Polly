import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    polly = boto3.client('polly')

    # Get bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Download the text file from S3
    file_content = s3.get_object(Bucket=bucket_name, Key=object_key)['Body'].read().decode('utf-8')

    # Synthesize speech using Amazon Polly
    response = polly.synthesize_speech(
        Text=file_content,
        OutputFormat='mp3',
        VoiceId='Joanna'  # You can change voice!
    )

    # Save the audio file back to S3
    audio_key = object_key.replace('.txt', '.mp3')
    s3.put_object(
        Bucket=bucket_name,
        Key=f"output/{audio_key}",
        Body=response['AudioStream'].read()
    )

    return {
        'statusCode': 200,
        'body': 'Text to speech conversion completed!'
    }
