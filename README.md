**AWS Text-to-Speech Automation Using Amazon Polly**

This project showcases a simple, event-driven workflow on AWS for automatically converting text files into speech. When a user uploads a .txt file into a designated input folder in an S3 bucket, it triggers an AWS Lambda function. The Lambda function reads the file’s content and uses Amazon Polly to synthesize the text into an MP3 audio file, which is then saved to the output folder within the same bucket.
This automated setup provides a seamless, hands-off solution for transforming text into audio.

**Workflow**

1-A user uploads a .txt file to the input folder of the S3 bucket.

2-This upload triggers the pre-configured AWS Lambda function.

3-The Lambda function reads the uploaded text file.

4-Amazon Polly synthesizes the text into an MP3 audio file.

5-The Lambda function saves the MP3 file to the output folder in the same S3 bucket.

**Tools and Services Used**

1-Amazon S3 — For storing input text files and output audio files.

2-AWS Lambda — To process S3 events and coordinate the text-to-speech conversion using Polly.

3-Amazon Polly — To perform the actual text-to-speech synthesis.

4-IAM Roles and Policies — To provide the necessary permissions for Lambda to interact with S3 and Polly.

**How to Use This Setup**

1. Configure Your Lambda Function
Ensure your Lambda function is properly set up with:

An S3 trigger that listens for object creation events only in the input folder.

IAM permissions that allow it to:

Read from the input folder.

Write to the output folder.

Access Amazon Polly services.

2. Prepare Your S3 Bucket
Confirm that your S3 bucket contains two folders:

input — Upload your .txt files here.

output — This is where the generated .mp3 files will appear automatically.

3. Upload a Text File
To start the conversion, simply upload your .txt file into the input folder of your S3 bucket.

4. Automatic Processing
Once the file upload completes:

The S3 event will automatically trigger your Lambda function.

Lambda will process the text and invoke Amazon Polly for audio synthesis.

5. Retrieve Your Audio File
After successful processing:

Find the corresponding .mp3 file in the output folder.

The MP3 filename will generally match the name of your original text file.

