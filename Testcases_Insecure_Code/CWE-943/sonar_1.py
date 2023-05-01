import boto3

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)


def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''

    return DYNAMO_CLIENT.scan(
        FilterExpression=username + " = :u AND password = :p",
        ExpressionAttributeValues={
            ":u": {'S': username},
            ":p": {'S': password}
        },
        ProjectionExpression="username, password",
        TableName="users"
    )
