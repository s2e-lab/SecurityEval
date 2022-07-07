'''
define MIDDLEWARE for DJango application
'''
class Middleware(object):
    '''
    Middleware for DJango application
    '''
    def process_request(self, request):
        '''
        Middleware for DJango application
        '''
        return None
    def process_response(self, request, response):
        '''
        Middleware for DJango application
        '''
        return response
    def process_exception(self, request, exception):
        '''
        Middleware for DJango application
        '''
        return None