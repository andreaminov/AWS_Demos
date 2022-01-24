#Install eksctl
chocolatey install -y eksctl aws-iam-authenticator

#Upgrade your version of eksctl
chocolatey upgrade -y eksctl aws-iam-authenticator

#You can check your version of eksctl
eksctl version

#Create your Amazon EKS cluster with Fargate support with the following command. 
eksctl create cluster --name eks-demo-april-30 --region us-east-1 --fargate

#Cluster provisioning status usually takes between 10 and 15 minutes. 
#When your cluster is ready, test that your kubectl configuration is correct.
kubectl get svc

#Delete Cluster
eksctl delete cluster --name eks-demo-april-30