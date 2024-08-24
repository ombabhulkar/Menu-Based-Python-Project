
# Cloud-Based Python Application

## Overview

This project is a Python application that integrates with various AWS services to automate cloud tasks. It demonstrates how to manage cloud resources, process files, and use serverless functions. 

## Features

- **EC2 Instance Management:** Launch and manage Amazon EC2 virtual servers.
- **RHEL GUI Instance:** Deploy and access a Red Hat Enterprise Linux instance with a graphical interface.
- **Log Access:** Access and manage log files stored in AWS.
- **Audio to Text Conversion:** Automatically convert audio files uploaded to Amazon S3 into text using AWS Transcribe.
- **Serverless MongoDB Connection:** Use AWS Lambda to connect to a MongoDB database.
- **S3 File Handling:** Automate file uploads to Amazon S3 with Lambda functions.
- **Email Notifications:** Send email notifications based on files uploaded to S3 using AWS SES.

## Getting Started

### Prerequisites

- **Python 3.x**
- **AWS Account** (with appropriate permissions for EC2, S3, Lambda, SES, and Transcribe services)
- **Boto3 Library:** Install using `pip install boto3`


### Usage

1. **Launch EC2 Instances:**
   Use the provided scripts or commands to launch and manage EC2 instances.

2. **Deploy RHEL GUI Instance:**
   Follow the instructions in the `ec2_operations.py` script to deploy a RHEL instance with a GUI.

3. **Access Logs:**
   Use the `ec2_operations.py` script to access and manage log files.

4. **Process Audio Files:**
   Upload audio files to the specified S3 bucket. AWS Transcribe will automatically convert these files into text.

5. **Connect to MongoDB:**
   Use the `mongodb_operations.py` script to connect to MongoDB.

6. **Handle S3 Uploads:**
   Upload files to the S3 bucket and use the `s3_operations.py` script for automated processing.

7. **Send Email Notifications:**
   Upload a file with email addresses to S3. The Lambda function will send emails to the addresses using AWS SES.

### Contributing

Feel free to submit pull requests or open issues if you have suggestions or encounter problems.

### License

This project is licensed under the Om Babhulkar.

## Acknowledgments

- AWS Services (EC2, S3, Lambda, SES, Transcribe)
- Boto3 Library
