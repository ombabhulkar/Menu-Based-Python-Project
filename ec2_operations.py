import boto3

def launch_rhel_instance():
    ec2 = boto3.resource('ec2')

    instance = ec2.create_instances(
        ImageId= 'ami-022ce6f32988af5fa',  
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='MyProjectKey',
        SecurityGroupIds=['sg-04e707a433cae5b23'],  
        SubnetId='subnet-0cf56df7f41f295ca' 
    )

    print(f"Launching RHEL instance with ID: {instance[0].id}")

if __name__ == "__main__":
    launch_rhel_instance()

def access_logs(instance_id):
    ec2_client = boto3.client('ec2')
    logs = ec2_client.get_console_output(InstanceId=instance_id)
    print(logs['Output'])

if __name__ == "__main__":
    instance_id = 'i-077afa00398fc690f'  
    access_logs(instance_id)

