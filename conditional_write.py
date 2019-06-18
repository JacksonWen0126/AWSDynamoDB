import boto3

dynamodb = boto3.client('dynamodb')

print("Conditional Write:")
response = dynamodb.update_item(
    TableName='MusicAlley',  # Table name
    Key={
        'Artist':{'S': "Anthony Haslett"},
        'SongTitle':{'S':"Blue Magenta"}
    },
    UpdateExpression='SET price = :val',
    ExpressionAttributeValues={
        ':val': {'N': '15.37'},  # Change value to 15.37 if the current value is 18.37
        ':currval': {'N': '18.37'}
    },
    ConditionExpression='price = :currval',
    ReturnValues="ALL_NEW"
)

