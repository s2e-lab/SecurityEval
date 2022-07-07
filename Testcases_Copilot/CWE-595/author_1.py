def isEqual(account1, account2):
    '''
    compare two accounts in the argument
    '''
    if len(account1) != len(account2):
        return False
    for i in range(len(account1)):
        if account1[i] != account2[i]:
            return False
    return True
