# AWS-Text-to-Speech-Polly
WS project to convert uploaded text into speech using S3, Lambda, and Polly

           [You / User]
                │
                ▼
    (Upload a .txt file to S3 bucket under input/)
            e.g., input/hello.txt
                │
                ▼
   ┌─────────────────────────────┐
   │       S3 Bucket (input/)     │
   └─────────────────────────────┘
                │
    (Triggers Event to Lambda)
                │
                ▼
   ┌─────────────────────────────┐
   │      Lambda Function         │
   │ - Downloads text file        │
   │ - Sends text to Polly        │
   │ - Gets MP3 audio stream      │
   │ - Uploads to output/ folder  │
   └─────────────────────────────┘
                │
                ▼
   ┌─────────────────────────────┐
   │       S3 Bucket (output/)    │
   └─────────────────────────────┘
                │
    (Stores MP3 file e.g., output/hello.mp3)

