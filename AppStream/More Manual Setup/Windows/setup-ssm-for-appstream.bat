
set MyVPCcidr=10.255.0.0/16
set MyPubSub1=10.255.0.0/24
set MyPrivSub1=10.255.1.0/24
set MyPrivSub2=10.255.2.0/24
set MyFleetImage=arn:aws:appstream:us-east-1:403147448834:image/BaseImage-20200415v4
echo %MyVPCcidr% %MyPrivSub1% %MyPrivSub1% %MyPrivSub2%

aws --profile default ssm put-parameter --name MyVPCcidr --description "VPC /CIDR block to use for setting up Appstream2 environment" --value %MyVPCcidr% --type String --overwrite

aws --profile default ssm put-parameter --name MyPubSub1 --description "Public subnet /CIDR block to use for setting up Appstream2 environment" --value %MyPubSub1% --type String --overwrite

aws --profile default ssm put-parameter --name MyPrivSub1 --description "Private subnet #1 /CIDR block to use for setting up Appstream2 environment" --value %MyPrivSub1% --type String --overwrite

aws --profile default ssm put-parameter --name MyPrivSub2 --description "Private subnet #2 /CIDR block to use for setting up Appstream2 environment" --value %MyPrivSub2% --type String --overwrite

aws --profile default ssm put-parameter --name MyFleetImage --description "Appstream image created with Firefox, Chrome, Putty, Notepad+" --value %MyFleetImage% --type String --overwrite
