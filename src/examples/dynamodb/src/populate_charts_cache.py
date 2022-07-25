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
table_name = 'reports_cache'
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
  TableName='reports_cache',
  Item={
    'ID': {'S': 'athena/national/category-tender-volume' },
    'data': {'S': json.dumps([{"stageCategoryName":"Retail","value":"94"},{"stageCategoryName":"Residential","value":"89"},{"stageCategoryName":"Medical","value":"89"},{"stageCategoryName":"Education","value":"88"},{"stageCategoryName":"Construction","value":"104"}]) }
  }
)

dynamodb.put_item(
  TableName='reports_cache',
  Item={
    'ID': {'S': 'athena/national/state-volume'},
    'data': {'S': json.dumps([{"state":"VIC","value":"157"},{"state":"QLD","value":"147"},{"state":"NSW","value":"160"}]) }
  }
)

dynamodb.put_item(
  TableName='reports_cache',
  Item={
    'ID': {'S': 'athena/national/tender-trend-volume'},
    'data': {'S': json.dumps([{"month":"2021-08","value":"52"},{"month":"2021-09","value":"44"},{"month":"2021-10","value":"53"},{"month":"2021-11","value":"41"},{"month":"2021-12","value":"62"},{"month":"2022-01","value":"48"},{"month":"2022-02","value":"65"},{"month":"2022-03","value":"44"},{"month":"2022-04","value":"55"}]) }
  }
)


dynamodb.put_item(
  TableName='reports_cache',
  Item={
    'ID': {'S': 'athena/vic/category-tender-volume' },
    'data': {'S': json.dumps([{"stageCategoryName":"Retail","value":"29"},{"stageCategoryName":"Residential","value":"40"},{"stageCategoryName":"Medical","value":"29"},{"stageCategoryName":"Education","value":"29"},{"stageCategoryName":"Construction","value":"30"}]) }
  }
)

dynamodb.put_item(
  TableName='reports_cache',
  Item={
    'ID': {'S': 'athena/national/tender-trend-volume' },
    'data': {'S': json.dumps([{"month":"2021-08","value":"52"},{"month":"2021-09","value":"44"},{"month":"2021-10","value":"53"},{"month":"2021-11","value":"41"},{"month":"2021-12","value":"62"},{"month":"2022-01","value":"48"},{"month":"2022-02","value":"65"},{"month":"2022-03","value":"44"},{"month":"2022-04","value":"55"}]) }
  }
)

dynamodb.put_item(
  TableName='reports_cache',
  Item={
    'ID': {'S': 'athena/vic/tender-trend-volume' },
    'data': {'S': json.dumps([{"month":"2021-08","value":"18"},{"month":"2021-09","value":"15"},{"month":"2021-10","value":"20"},{"month":"2021-11","value":"18"},{"month":"2021-12","value":"19"},{"month":"2022-01","value":"12"},{"month":"2022-02","value":"24"},{"month":"2022-03","value":"17"},{"month":"2022-04","value":"14"}]) }
  }
)

dynamodb.put_item(
  TableName='reports_cache',
  Item={
    'ID': {'S': 'athena/national/retail/tender-trend-volume' },
    'data': {'S': json.dumps([{"month":"2021-08","value":"3","state":"QLD"},{"month":"2021-08","value":"3","state":"NSW"},{"month":"2021-08","value":"3","state":"VIC"},{"month":"2021-09","value":"3","state":"QLD"},{"month":"2021-09","value":"1","state":"VIC"},{"month":"2021-09","value":"4","state":"NSW"},{"month":"2021-10","value":"8","state":"QLD"},{"month":"2021-10","value":"6","state":"VIC"},{"month":"2021-10","value":"2","state":"NSW"},{"month":"2021-11","value":"1","state":"QLD"},{"month":"2021-11","value":"3","state":"NSW"},{"month":"2021-11","value":"3","state":"VIC"},{"month":"2021-12","value":"6","state":"QLD"},{"month":"2021-12","value":"4","state":"VIC"},{"month":"2021-12","value":"2","state":"NSW"},{"month":"2022-01","value":"1","state":"VIC"},{"month":"2022-01","value":"3","state":"QLD"},{"month":"2022-01","value":"2","state":"NSW"},{"month":"2022-02","value":"4","state":"VIC"},{"month":"2022-02","value":"4","state":"NSW"},{"month":"2022-02","value":"6","state":"QLD"},{"month":"2022-03","value":"5","state":"VIC"},{"month":"2022-03","value":"3","state":"NSW"},{"month":"2022-03","value":"3","state":"QLD"},{"month":"2022-04","value":"5","state":"QLD"},{"month":"2022-04","value":"2","state":"VIC"},{"month":"2022-04","value":"4","state":"NSW"}]) }
  }
)

dynamodb.put_item(
  TableName='reports_cache',
  Item={
    'ID': {'S': 'athena/national/tender-trend-volume-state'},
    'data': {'S': json.dumps([{"month":"2021-08","value":"21","state":"NSW"},{"month":"2021-08","value":"18","state":"VIC"},{"month":"2021-08","value":"13","state":"QLD"},{"month":"2021-09","value":"15","state":"NSW"},{"month":"2021-09","value":"14","state":"QLD"},{"month":"2021-09","value":"15","state":"VIC"},{"month":"2021-10","value":"15","state":"QLD"},{"month":"2021-10","value":"20","state":"VIC"},{"month":"2021-10","value":"18","state":"NSW"},{"month":"2021-11","value":"18","state":"VIC"},{"month":"2021-11","value":"14","state":"NSW"},{"month":"2021-11","value":"9","state":"QLD"},{"month":"2021-12","value":"22","state":"QLD"},{"month":"2021-12","value":"19","state":"VIC"},{"month":"2021-12","value":"21","state":"NSW"},{"month":"2022-01","value":"17","state":"NSW"},{"month":"2022-01","value":"19","state":"QLD"},{"month":"2022-01","value":"12","state":"VIC"},{"month":"2022-02","value":"20","state":"NSW"},{"month":"2022-02","value":"24","state":"VIC"},{"month":"2022-02","value":"21","state":"QLD"},{"month":"2022-03","value":"12","state":"NSW"},{"month":"2022-03","value":"15","state":"QLD"},{"month":"2022-03","value":"17","state":"VIC"},{"month":"2022-04","value":"22","state":"NSW"},{"month":"2022-04","value":"19","state":"QLD"},{"month":"2022-04","value":"14","state":"VIC"}]) }
  }
)


print(
  json.dumps(
    dynamodb.get_item(
      TableName=table_name,
      Key={
          'ID': {'S': 'athena/national/tender-trend-volume'},
      }
    ),
    indent=2
  )
)