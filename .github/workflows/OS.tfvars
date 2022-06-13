#Ami Rocky 85
ami_id        = "ami-0d824d9c499f27c8a"
ami_os        = "rhel9"
ami_username  = "ec2-user"
ami_user_home = "/home/ec2-user"
instance_tags = {
  Name        = "RHEL9-CIS"
  Environment = "lockdown_github_repo_workflow"
}
