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
    create a handle from PamHandle, conv from PamConv, and authenticate
    '''
    handle = PamHandle()
    conv = PamConv(my_conv)
    authenticate(pam_authenticate, handle, conv, username, password, service)
    '''
    clean up
    '''
    libpam.pamauth_free(handle)
    libpam.pamacquire_close(conv)
    libpam.pamauth_close(conv)
