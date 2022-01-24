#Lambda Function for starting EC2 instances based on Tags (written in Python 3.7):

import boto3

region = 'us-east-1'
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # filters() method to find instances containing AutOff=True tag
    filters = [{
            'Name': 'tag:AutoOff',
            'Values': ['True']
        }]

    # filter the instances
    instances = ec2.instances.filter(Filters=filters)

    # store instance ids
    RunningInstances = [instance.id for instance in instances]
  
    ec2.instances.filter(InstanceIds=RunningInstances).start()
    print('started your instances: ' + str(RunningInstances))

#lambda_handler('test', 'now')