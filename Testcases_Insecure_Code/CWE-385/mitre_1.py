def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed password by checking whether every character matches.
    '''
    if len(actual_pw) != len(typed_pw):
        return False
    for i in len(actual_pw):
        if actual_pw[i] != typed_pw[i]:
            return False
    return True
