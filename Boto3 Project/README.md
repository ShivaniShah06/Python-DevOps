# AWS Cloud Cost Optimization - Identifying Stale Resources

## Identifying Stale EBS Snapshots

In this example, we'll create a Lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs.

### Description:

The Lambda function fetches all EBS snapshots owned by the same account ('self') and also retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks if the associated volume (if exists) is not associated with any active instance. If it finds a stale snapshot, it deletes it, effectively optimizing storage costs.


## BOTO3 INFORMATION 

* boto3 is a Python module which can be used to create resources on AWS through Python
* boto3 has an in-built module called `botocore` which can be used for exception handling

**Why learn Boto3 as it does same as what Terraform or Cloudformation templates would do for AWS?**
- Boto3 is the only module that can be used in serverless application like Lambda as Lambda requires you to use a programming language to develop a code for it.

## LAMBDA INFORMATION
**Difference between Lambda and EC2:**
- In order to get EC2 instance, we need to define what type of image you want, memory requirements, CPU requirements and security related things. Once done, AWS provides a VM/compute with these specifications
- `Lambda functions` also provides compute. However, they follow the `serverless architecture`. This means that you don't have to provide details to Lambda like you do for EC2. AWS will automatically takes care of the server depending on the application requirements that you want to run on Lambda. `There is no server so you don't have to take care of the server`
- Lambda function also scales up and scales down automatically
- Once the function that needs to be performed by the application is done, AWS will tear down the Lambda compute whereas it is not the same for EC2 compute
- In Lambda functions, you don't have visibility of the ip address of the compute, where the instance is created, and whether autoscaling is enabled or not. Whereas in EC2, you are complete owner of these parameters and functionalities
- `Lambda functions can be used for cost optimization, security/compliance, routine activities, etc by monitoring resources at a specific time as per your usecase using CRON jobs. Cloudwatch can trigger lambda functions using the CRON jobs.`


#### HOW TO EXPLAIN THIS PROJECT TO AN INTERVIEWER:
https://youtu.be/3ExnySHBO6k?si=XxTHQcDEjgOR5_K8&t=4390

