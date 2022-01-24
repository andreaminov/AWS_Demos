# Load the AWS SDK for Python
import boto3

# Load the exceptions for error handling
from botocore.exceptions import ClientError, ParamValidationError

# Create AWS service client and set region
sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = "https://sqs.us-east-1.amazonaws.com/093086341349/awseducate-lab"

# Send 50 SQS messages
def create_messages(queue_url):
    # Create 50 messages
    TempMessages = []
    for a in range(50):
        tempStr = 'This is the content for message ' + str(a)
        TempMessages.append(tempStr)

    # Deliver messages to SQS queue_url
    for message in TempMessages:
        try:
            data = sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=message
                )
            print(data['MessageId'])

        # An error occurred
        except ParamValidationError as e:
            print("Parameter validation error: %s" % e)
        except ClientError as e:
            print("Client error: %s" % e)

# Main program
create_messages(queue_url)
