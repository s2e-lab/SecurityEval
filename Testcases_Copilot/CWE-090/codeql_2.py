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
    dc = request.args.get('dc')
    username = request.args.get('username')
    dn = 'dc=' + dc + ',dc=com'
    search_filter = 'uid=' + username
    conn = ldap3.Connection(ldap3.Server('localhost'), auto_bind=True)
    conn.search(dn, search_filter)
    return str(conn.entries)