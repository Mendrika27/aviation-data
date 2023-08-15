import boto3
from config.aws_config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

def upload_to_s3():
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    filename = f"flight_data_{datetime.now().strftime('%Y_%m_%d')}.json"
    
    with open(filename, 'rb') as file:
        s3.upload_fileobj(file, 'your-s3-bucket-name', filename)

if __name__ == "__main__":
    upload_to_s3()
