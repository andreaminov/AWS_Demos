#!/bin/bash
yum install -y https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-latest-x86_64/postgresql10-libs-10.7-2PGDG.rhel7.x86_64.rpm
yum install -y https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-latest-x86_64/postgresql10-10.7-2PGDG.rhel7.x86_64.rpm
yum install -y https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-latest-x86_64/postgresql10-server-10.7-2PGDG.rhel7.x86_64.rpm
yum install -y httpd php git
service httpd start
yum install -y postgresql10
yum install php-pgsql -y
amazon-linux-extras install epel -y
yum install -y amazon-efs-utils
cd
git clone https://github.com/nkean97/Class_Demos.git
cp ./Class_Demos/ELB/* /var/www/html
mv /var/www/html/htaccess /var/www/html/.htaccess
systemctl enable httpd.service
systemctl start httpd.service