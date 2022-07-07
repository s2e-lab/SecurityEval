from flask import Flask, make_response, request

app = Flask("Leak password")

@app.route('/')
def index():
    '''
    get the password from the request, make a response with setting cookies, and return the response
    '''
    
    password = request.cookies.get('password')
    
    response = make_response(
        'Your password is {}'.format(password)
    )
    
    response.set_cookie('password', '12345678', secure = True)
    
    return response