# Quick Start: Run a EC2 instance and access it from the Internet
Following steps accomplish [Scenario 1：VPC with a Single Public Subnet on AWS document](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario1.html).

1. Create VPC
2. Create Subnet on the VPC created at step 1
  * Enable "Auto-assign Public IP" option at this Subnet
3. Create Internet Gateway(IGW)
4. Attach IGW created at step 3 into the VPC
5. Add route:"0.0.0.0/0 to the IGW" into Route Table on the Subnet created at step 2
  * After done this step, the Subnet becomes "public subnet"
6. Create Security Group(SG)
  * Inbound: Allow only 22/tcp from 0.0.0.0/0
  * Outbound: Allow only 80/tcp and 443/tcp to 0.0.0.0/0
  * Associate this SG with the VPC
7. Create EC2 instance from public AMI
  * Select a Suitable public AMI: e.g. Amazon Linux 2
  * Associate this EC2 instance with the VPC and Subnet
  * Apply SG created at step 6 with this EC2 instance
  * Generate SSH keypair and download the SSH private key
  * After this EC2 instance is created, run the EC2 instance
8. Set passphrase the SSH private key downloaded at step 7
  * You can use `ssh-keygen` command with `-p` option to do it
9. Access public IP address of the EC2 instance via SSH
10. Congratulations! Done.

## Related Links
- [20190313 AWS Black Belt Online Seminar Amazon VPC Basic](https://www.slideshare.net/AmazonWebServicesJapan/20190313-aws-black-belt-online-seminar-amazon-vpc-basic/24) (in Japanese)
  * slide 24-47: ウォークスルー: インターネット接続VPCセットアップ
- [Scenario 1： VPC with a Single Public Subnet - Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario1.html)
- https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html
  * *public subnet is a subnet that's associated with a route table that has a route to an Internet gateway.*
