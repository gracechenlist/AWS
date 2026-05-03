output "public_ip" {
  value = aws_instance.web.public_ip
}

output "public_dns" {
  value = aws_instance.web.public_dns
}

output "ansible_inventory" {
  value = local_file.ansible_inventory.filename
}

output "ssh_command" {
  value = "ssh -i ${var.private_key_path} ec2-user@${aws_instance.web.public_ip}"
}
