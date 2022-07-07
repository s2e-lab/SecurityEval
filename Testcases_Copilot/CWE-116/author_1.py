def sendReply(request):
    '''
    read the data from request and send back the data as response as a HTML page
    '''
    data = request.args.get('data')
    html = '<html><body><h1>' + data + '</h1></body></html>'
    return html
