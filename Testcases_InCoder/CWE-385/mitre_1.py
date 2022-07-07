def validate_password(actual_pw, typed_pw):
    '''
    compare the actual password with the typed password by checking every character
    '''
    length = len(actual_pw)
    
    if length < 6 or length > 16:
        return False
    
    count_letters = 0
    count_numbers = 0
    count_special_characters = 0
    
    for character in typed_pw:
        if character in string.ascii_letters:
            count_letters = count_letters + 1
        elif character in string.digits:
            count_numbers = count_numbers + 1
        elif character in string.punctuation:
            count_special_characters = count_special_characters + 1
        
    
    if count_letters == length and count_numbers == length and count_special_characters == length:
        return True
    else:
        return False
    