#Ami Rocky 85
ami_id        = "ami-0c41531b8d18cc72b"
ami_os        = "rhel9"
ami_username  = "ec2-user"
ami_user_home = "/home/ec2-user"
instance_tags = {
  Name        = "RHEL9-CIS"
  Environment = "lockdown_github_repo_workflow"
}
