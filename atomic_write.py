import boto3

dynamodb = boto3.client('dynamodb')

print("Atomic Counter:")
response = dynamodb.update_item(
    TableName='MusicAlley',  # Table name
    Key={
        'Artist':{'S': "Anthony Haslett"},  # Partition key
        'SongTitle':{'S':"Ivory Maroon"}    # Sort key
    },
    UpdateExpression='SET price = price + :inc',
    ExpressionAttributeValues={
        ':inc': {'N': '3'}  # incrementing by 3
    },
    ReturnValues="UPDATED_NEW"
)
print("UPDATING ITEM")
print(response)
