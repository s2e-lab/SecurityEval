from django.http import HttpResponse


def sendReply(request):
    '''
    read the data from request and send back the data as response as a HTML page
    '''
    msg = ""
    reply_msg = ""
    
    try:
        msg = request.body.decode("utf-8")
        reply_msg = msg.split(':')[1]
    except:
        reply_msg = "Invalid request"
    
    return HttpResponse("""<html><body>
    <h1>Request received!</h1>
    <p>
    Request received from: {{ request.META.HTTP_HOST }}<br>
    Message: {{ msg }}<br>
    Message: {{ reply_msg }}
    </p>
    </body></html>""".format(msg=msg, reply_msg=reply_msg))


