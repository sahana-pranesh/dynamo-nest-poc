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

dynamodb.put_item(
  TableName='projects_cache',
  Item={
    'ID': {'S': 'keyword1' },
    'data': {'S': json.dumps([100023,100024,10089,10026]) }
  }
)

dynamodb.put_item(
  TableName='projects_cache',
  Item={
    'ID': {'S': 'keyword2' },
    'data': {'S': json.dumps([100045,1000904,100897,1004536]) }
  }
)

dynamodb.put_item(
  TableName='projects_cache',
  Item={
    'ID': {'S': 'keyword3' },
    'data': {'S': json.dumps([100345,101904,103897,104536]) }
  }
)

dynamodb.put_item(
  TableName='projects_cache',
  Item={
    'ID': {'S': 'keyword4' },
    'data': {'S': json.dumps([100456,101978,103823,1045390]) }
  }
)

