# Terraform + Ansible AWS Automation Project

## Overview

This project demonstrates a DevOps workflow that combines Terraform and Ansible:

- Terraform provisions AWS infrastructure.
- Ansible configures the EC2 instance after it is created.

## Resources Created by Terraform

- VPC
- Public subnet
- Internet gateway
- Route table
- Security group for SSH and HTTP
- EC2 instance
- Dynamic Ansible inventory file

## Configuration Done by Ansible

- Installs Apache HTTP server
- Starts and enables the service
- Deploys a custom web page

## Project Structure

```text
terraform-ansible-aws-project/
├── main.tf
├── variables.tf
├── outputs.tf
├── README.md
└── ansible/
    └── playbook.yml
```

## Prerequisites

- Terraform installed
- AWS CLI configured
- Ansible installed
- Existing AWS key pair, for example `grace_key`
- Private key available locally, for example `~/.ssh/grace_key.pem`

## Usage

### 1. Initialize Terraform

```bash
terraform init
```

### 2. Review the plan

```bash
terraform plan
```

### 3. Apply Terraform

```bash
terraform apply
```

Type `yes` when prompted.

### 4. Run Ansible

```bash
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```

### 5. Test the web server

Open the public IP from Terraform output in a browser:

```text
http://<public_ip>
```

### 6. Cleanup

```bash
terraform destroy
```

## Notes

- In production, restrict SSH access to your own IP instead of `0.0.0.0/0`.
- Changing subnet or Availability Zone can cause Terraform to replace the EC2 instance.
- The AMI ID may need to be updated depending on region and availability.

