# Boto3 EC2 VM Automation Project

A beginner-friendly AWS project that uses Python and boto3 to automate EC2 virtual machine lifecycle tasks.

This project is designed to help you gain hands-on AWS experience and explain cloud automation in interviews.

## What This Project Does

Using Python, this project can:

- Launch an EC2 instance
- Check EC2 instance status
- Stop an EC2 instance
- Start an EC2 instance
- Terminate an EC2 instance
- List EC2 instances
- Tag EC2 instances with name, owner, and environment

## AWS Services Used

- EC2
- IAM
- VPC
- Security Groups
- Key Pair

## Project Structure

```text
boto3-ec2-vm-automation/
├── ec2_automation.py
├── config.py
├── .env.example
├── requirements.txt
├── README.md
└── resume_bullets.md
```

## Setup

### 1. Install AWS CLI

Download and install AWS CLI v2:

https://aws.amazon.com/cli/

Verify:

```bash
aws --version
```

### 2. Configure AWS credentials

```bash
aws configure
```

Use:

```text
AWS Access Key ID: your_access_key
AWS Secret Access Key: your_secret_key
Default region name: us-east-1
Default output format: json
```

### 3. Install Python packages

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

Copy `.env.example` to `.env` and fill in your values:

```powershell
copy .env.example .env
```

Mac/Linux:

```bash
cp .env.example .env
```

## Required AWS Values

You need these from AWS:

```env
AWS_REGION=us-east-1
AMI_ID=ami-xxxxxxxxxxxxxxxxx
INSTANCE_TYPE=t2.micro
KEY_NAME=your-key-pair-name
SECURITY_GROUP_ID=sg-xxxxxxxxxxxxxxxxx
SUBNET_ID=subnet-xxxxxxxxxxxxxxxxx
```

## How to Run

### Launch a VM

```bash
python ec2_automation.py launch
```

### List VMs

```bash
python ec2_automation.py list
```

### Check one VM

```bash
python ec2_automation.py status i-xxxxxxxxxxxxxxxxx
```

### Stop a VM

```bash
python ec2_automation.py stop i-xxxxxxxxxxxxxxxxx
```

### Start a VM

```bash
python ec2_automation.py start i-xxxxxxxxxxxxxxxxx
```

### Terminate a VM

```bash
python ec2_automation.py terminate i-xxxxxxxxxxxxxxxxx
```

## Example Interview Explanation

I built a Python-based AWS EC2 automation project using boto3. It automates common VM lifecycle actions including launch, status check, start, stop, terminate, and list. This helped me translate my on-prem VM automation experience with KVM/oVirt into AWS cloud automation using EC2, IAM, VPC networking, key pairs, and security groups.

## Security Notes

Do not upload `.env` or AWS credentials to GitHub.

Use IAM least privilege when possible.

For learning, you can start with EC2 permissions, but for production, limit permissions to only required actions.
