import boto3

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username,password):
    '''
    get the user information from users table by using username and password
    '''
