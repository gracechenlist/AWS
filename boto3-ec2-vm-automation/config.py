import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AMI_ID = os.getenv("AMI_ID")
INSTANCE_TYPE = os.getenv("INSTANCE_TYPE", "t2.micro")
KEY_NAME = os.getenv("KEY_NAME")
SECURITY_GROUP_ID = os.getenv("SECURITY_GROUP_ID")
SUBNET_ID = os.getenv("SUBNET_ID")

VM_NAME = os.getenv("VM_NAME", "boto3-test-vm")
VM_OWNER = os.getenv("VM_OWNER", "grace")
VM_ENVIRONMENT = os.getenv("VM_ENVIRONMENT", "dev")


def validate_config():
    required_values = {
        "AMI_ID": AMI_ID,
        "KEY_NAME": KEY_NAME,
        "SECURITY_GROUP_ID": SECURITY_GROUP_ID,
        "SUBNET_ID": SUBNET_ID,
    }

    missing = [key for key, value in required_values.items() if not value]

    if missing:
        raise ValueError(
            "Missing required environment values: "
            + ", ".join(missing)
            + ". Please update your .env file."
        )
