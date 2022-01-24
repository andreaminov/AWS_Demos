# Load the AWS SDK for Python
import boto3
import time

# Load the exceptions for error handling
from botocore.exceptions import ClientError, ParamValidationError

# Create AWS service client and set region
sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = "https://sqs.us-east-1.amazonaws.com/093086341349/awseducate-lab"

# Receive SQS messages
def receive_messages(queue_url): 
    print('Reading messages') 
    while True:
        try:
            data = sqs.receive_message(
                QueueUrl=queue_url, 
                MaxNumberOfMessages=10, 
                VisibilityTimeout=60, 
                WaitTimeSeconds=20
                )
        
        # An error occurred
        except ParamValidationError as e:
            print("Parameter validation error: %s" % e)
        except ClientError as e:
            print("Client error: %s" % e)
        
        # Check if empty receive
        try:
            data['Messages']
        except KeyError:
            data = None
        if data is None:
            print('Queue empty waiting 60s')  
            # Wait for 60 seconds 
            time.sleep(60)
        else:
            print(data['Messages'])  
            # Wait for 1 second 
            time.sleep(1)

def main():
    receive_messages(queue_url)

if __name__ == '__main__':
    main()
    