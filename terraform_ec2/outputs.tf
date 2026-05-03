output "public_ip" {
  value = aws_instance.vm.public_ip
}

output "ssh_command" {
  value = "ssh ec2-user@${aws_instance.vm.public_ip}"
}