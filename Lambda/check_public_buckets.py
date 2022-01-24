# The Lambda fuction will scan all your buckets and look for the customer tag
# CanBePublic.  If any bucket is assigned public access and does not have the tag 
# CanBePublic set to 1, the Lambda fuction will treat it as a polcy violoation.  
# When this happns it weill set the bucket ACL to private and send a message to SNS


def checkBucketTags(tags):
    print("Tags: {}".format(tags))
    for tag in tags:
        print(tag)
        if tag["Key"] == "CanBePublic":
            return tag["Value"] == "1"
    return False

def lambda_handler(event, context):
    # instantiate Amazon S3 client
    s3 = boto3.client("s3")
    print("{}".format(event))
    resource = list(event["detail"]["requestParameters"]["evaluations"])[0]
    bucketName = resource["complianceResourceId"]
    bucketTags = s3.get_bucket_tagging(Bucket=bucketName)
    if (bucketTags is not None):
        shouldBePublic = checkBucketTags(bucketTags["TagSet"])
        if not shouldBePublic:
            complianceFailure = event["detail"]["requestParameters"]["evaluations"][0]["annotation"]
            if(complianceFailure == ACL_RD_WARNING or complianceFailure == ACL_WRT_WARNING):
                s3.put_bucket_acl(Bucket = bucketName, ACL = "private")
            elif(complianceFailure == PLCY_RD_WARNING or complianceFailure == PLCY_WRT_WARNING):
                policyNotifier(bucketName, s3)
            elif(complianceFailure == RD_COMBO_WARNING or complianceFailure == WRT_COMBO_WARNING):
                s3.put_bucket_acl(Bucket = bucketName, ACL = "private")
                policyNotifier(bucketName, s3)
    return 0  # done