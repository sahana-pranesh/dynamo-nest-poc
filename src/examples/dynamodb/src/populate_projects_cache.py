import boto3
import json

dynamodb =  boto3.client(
              'dynamodb',
              endpoint_url="http://localstack:4566",
              use_ssl=False,
              aws_access_key_id='mock',
              aws_secret_access_key='mock'
            )


existing_tables = dynamodb.list_tables()['TableNames']
table_name = 'projects_cache'
if table_name in existing_tables:
  dynamodb.delete_table(TableName=table_name)

params = {
    'TableName': table_name,
    'KeySchema': [
        {'AttributeName': 'ID', 'KeyType': 'HASH'},
    ],
    'AttributeDefinitions': [
        {'AttributeName': 'ID', 'AttributeType': 'S'},
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
}
table = dynamodb.create_table(**params)
print(f"Creating {table_name}...")
