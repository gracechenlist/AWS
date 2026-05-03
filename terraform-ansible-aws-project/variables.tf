variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "availability_zone" {
  description = "Availability Zone for subnet"
  type        = string
  default     = "us-east-1a"
}

variable "ami_id" {
  description = "Amazon Linux 2 AMI ID. Update if needed."
  type        = string
  default     = "ami-08a6efd148b1f7504"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "key_name" {
  description = "Existing AWS EC2 key pair name"
  type        = string
  default     = "grace_key"
}

variable "private_key_path" {
  description = "Local path to your private key for Ansible SSH"
  type        = string
  default     = "~/.ssh/grace_key.pem"
}

variable "ssh_allowed_cidr" {
  description = "CIDR allowed for SSH. Use your public IP /32 in real projects."
  type        = string
  default     = "0.0.0.0/0"
}
