import os

aws_access_key_id = os.environ.get("aws_access_key_id", "AKIAYHWETL5W4DM5AG2A")
aws_secret_access_key = os.environ.get("aws_secret_access_key", "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")
ami_id = "ami-051f7e7f6c2f40dc1"
instance_type = "t2.micro"
SecurityGroups = 'launch-wizard-1'
KeyName="ec2_rsa"