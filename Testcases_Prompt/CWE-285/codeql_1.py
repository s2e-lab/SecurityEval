libpam                    = CDLL(find_library("pam"))

pam_authenticate          = libpam.pam_authenticate
pam_authenticate.restype  = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        pass
    '''
    Create a handle from PamHandle,
    configure the PAM conversation to use my_conv as a callback function to allow PAM to send messages to and get input from a user.  
    Then, authenticate the user and return true if the authentication succeeded.
    '''