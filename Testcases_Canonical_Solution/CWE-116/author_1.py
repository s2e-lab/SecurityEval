def sendReply(request):
    '''
    read the data from request and send back the data as response as a HTML page
    '''
    data = request.read()
    request.send_response(200)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(data)
    return

