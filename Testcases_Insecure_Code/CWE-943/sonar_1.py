import boto3

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username,password):
    '''
    get the user information from users table by using username and password
    '''

    return DYNAMO_CLIENT.scan(
        FilterExpression= username + " = :u AND password = :p",
        ExpressionAttributeValues={
            ":u": { 'S': username },
            ":p": { 'S': password }
        },
        ProjectionExpression="username, password",
        TableName="users"
    )