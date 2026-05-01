import sys
import boto3
from botocore.exceptions import ClientError

from config import (
    AWS_REGION,
    AMI_ID,
    INSTANCE_TYPE,
    KEY_NAME,
    SECURITY_GROUP_ID,
    SUBNET_ID,
    VM_NAME,
    VM_OWNER,
    VM_ENVIRONMENT,
    validate_config,
)


ec2 = boto3.client("ec2", region_name=AWS_REGION)


def launch_instance():
    """Launch a new EC2 instance."""
    validate_config()

    try:
        response = ec2.run_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            MinCount=1,
            MaxCount=1,
            NetworkInterfaces=[
                {
                    "DeviceIndex": 0,
                    "SubnetId": SUBNET_ID,
                    "Groups": [SECURITY_GROUP_ID],
                    "AssociatePublicIpAddress": True,
                }
            ],
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {"Key": "Name", "Value": VM_NAME},
                        {"Key": "Owner", "Value": VM_OWNER},
                        {"Key": "Environment", "Value": VM_ENVIRONMENT},
                        {"Key": "Project", "Value": "boto3-ec2-vm-automation"},
                    ],
                }
            ],
        )

        instance = response["Instances"][0]
        instance_id = instance["InstanceId"]

        print("EC2 instance launch requested successfully.")
        print(f"Instance ID: {instance_id}")
        print(f"Initial State: {instance['State']['Name']}")

    except ClientError as error:
        print(f"AWS error launching instance: {error}")


def list_instances():
    """List EC2 instances managed by this project."""
    try:
        response = ec2.describe_instances(
            Filters=[
                {
                    "Name": "tag:Project",
                    "Values": ["boto3-ec2-vm-automation"],
                }
            ]
        )

        found = False

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                found = True
                instance_id = instance["InstanceId"]
                state = instance["State"]["Name"]
                instance_type = instance["InstanceType"]
                public_ip = instance.get("PublicIpAddress", "N/A")

                name = "N/A"
                for tag in instance.get("Tags", []):
                    if tag["Key"] == "Name":
                        name = tag["Value"]

                print("-" * 60)
                print(f"Name: {name}")
                print(f"Instance ID: {instance_id}")
                print(f"State: {state}")
                print(f"Type: {instance_type}")
                print(f"Public IP: {public_ip}")

        if not found:
            print("No EC2 instances found for this project.")

    except ClientError as error:
        print(f"AWS error listing instances: {error}")


def get_instance_status(instance_id):
    """Get status for one EC2 instance."""
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response["Reservations"][0]["Instances"][0]

        print(f"Instance ID: {instance['InstanceId']}")
        print(f"State: {instance['State']['Name']}")
        print(f"Type: {instance['InstanceType']}")
        print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")
        print(f"Private IP: {instance.get('PrivateIpAddress', 'N/A')}")

    except ClientError as error:
        print(f"AWS error getting status: {error}")


def stop_instance(instance_id):
    """Stop an EC2 instance."""
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stop requested for instance: {instance_id}")

    except ClientError as error:
        print(f"AWS error stopping instance: {error}")


def start_instance(instance_id):
    """Start an EC2 instance."""
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Start requested for instance: {instance_id}")

    except ClientError as error:
        print(f"AWS error starting instance: {error}")


def terminate_instance(instance_id):
    """Terminate an EC2 instance."""
    try:
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminate requested for instance: {instance_id}")

    except ClientError as error:
        print(f"AWS error terminating instance: {error}")


def print_usage():
    print("""
Usage:

  python ec2_automation.py launch
  python ec2_automation.py list
  python ec2_automation.py status <instance_id>
  python ec2_automation.py stop <instance_id>
  python ec2_automation.py start <instance_id>
  python ec2_automation.py terminate <instance_id>

Examples:

  python ec2_automation.py launch
  python ec2_automation.py list
  python ec2_automation.py status i-0123456789abcdef0
""")


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()

    if command == "launch":
        launch_instance()

    elif command == "list":
        list_instances()

    elif command == "status" and len(sys.argv) == 3:
        get_instance_status(sys.argv[2])

    elif command == "stop" and len(sys.argv) == 3:
        stop_instance(sys.argv[2])

    elif command == "start" and len(sys.argv) == 3:
        start_instance(sys.argv[2])

    elif command == "terminate" and len(sys.argv) == 3:
        terminate_instance(sys.argv[2])

    else:
        print_usage()


if __name__ == "__main__":
    main()
