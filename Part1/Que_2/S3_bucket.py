import boto3

s3 = boto3.resource(service_name='s3',
                    region_name='us-east-1',
                    aws_access_key_id='AKIAWEUQWUKRPX2PJLFY',
                    aws_secret_access_key='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')

BUCKET_NAME = 'review-ratings'
for obj in s3.Bucket(BUCKET_NAME).objects.all():
    print(obj)