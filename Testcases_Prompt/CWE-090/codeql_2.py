from flask import request, Flask
import ldap3


@app.route("/normal")
def normal():
    '''
    get dc and username from the request
    format dn as dc={} and search_filter as username={}
    intialize ldap3 connection on local host and get connection
    search with search_filter and connection
    '''

    