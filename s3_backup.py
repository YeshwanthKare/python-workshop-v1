"""
This is script to take a backup from local to AWS S3
"""

import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
	# print(s3.buckets.all())
	buckets = s3.buckets.all()	
	for bucket in buckets:
		print(bucket.name)
	

def create_bucket(s3):
	s3.create_bucket(Bucket="python-for-devops-yesh-phoenix",CreateBucketConfiguration={
    'LocationConstraint': 'us-east-2'})
	print("Bucket created successfully!")

def delete_bucket(s3):
	bucket = s3.Bucket("python-for-devops-junoon")
	bucket.delete()
	print("Bucket Deleted successfully!")

def upload_backup(s3, file_name, bucket_name, key_name):
	"""

	uploads a given backup file path to a given s3 bucket
	with a new name(key)
	"""


	data = open(file_name, "rb") # file gets read in binary
	s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
	print("Backup uploaded successfully!")

bucket_name= "python-for-devops-yesh-phoenix"
region = "us-east-2"

# create_bucket(s3, bucket_name, region)

# create_bucket(s3)

# delete_bucket(s3)

# show_buckets(s3)
file_name="/Users/yesh/Documents/LocalDisk-D/DevOps_with_shubam/Python_for_DevOps/September_1-2024/python_workshop_practice/backups/backup_2024-09-02.tar.gz"
upload_backup(s3, file_name, bucket_name, "my-backup.tar.gz")
