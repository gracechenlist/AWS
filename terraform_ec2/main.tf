provider "aws" {
  region = "us-east-1"
}

# ----------------------
# VPC
# ----------------------
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "grace-vpc"
  }
}

# ----------------------
# Subnet
# ----------------------
resource "aws_subnet" "main" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-east-1a"
  tags = {
    Name = "grace-subnet"
  }
}

# ----------------------
# Internet Gateway
# ----------------------
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "grace-igw"
  }
}

# ----------------------
# Route Table
# ----------------------
resource "aws_route_table" "rt" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "grace-rt"
  }
}

# Associate route table with subnet
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.main.id
  route_table_id = aws_route_table.rt.id
}

# ----------------------
# Security Group (SSH)
# ----------------------
resource "aws_security_group" "ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # (we’ll tighten this later if needed)
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ----------------------
# EC2 Instance
# ----------------------
resource "aws_instance" "vm" {
  ami                    = "ami-08a6efd148b1f7504"
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.main.id
  vpc_security_group_ids = [aws_security_group.ssh.id]

  tags = {
    Name = "grace-terraform-vm"
  }
}