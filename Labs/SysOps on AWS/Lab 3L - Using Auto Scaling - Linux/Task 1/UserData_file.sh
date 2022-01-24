#!/bin/bash

###################################################################################################
###This  script performs a number of initialization task,
###including updating all intalled software on the box and installing a 
###small PHP web application that you can use to simulate a high CPU load on the instance.
###################################################################################################

yum update -y --security
yum -y install httpd php stress
chkconfig httpd on
/etc/init.d/httpd start
cd /var/www/html
wget https://us-west-2-tcprod.s3.amazonaws.com/courses/ILT-TF-100-SYSOPS/v3.3.15/lab-3-scaling-linux/scripts/ec2-stress.zip
unzip ec2-stress.zip

echo 'UserData has been successfully executed. ' >> /home/ec2-user/result

###These lines erase any history or security information that may have accidentally been left on the instance when the image was taken.
find -wholename /root/.*history -wholename /home/*/.*history -exec rm -f {} \;
find / -name 'authorized_keys' -exec rm -f {} \;
rm -rf /var/lib/cloud/data/scripts/*