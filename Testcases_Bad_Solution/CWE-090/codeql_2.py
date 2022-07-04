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
    unsafe_dc = request.args['dc']
    unsafe_filter = request.args['username']

    dn = "dc={}".format(unsafe_dc)
    search_filter = "(user={})".format(unsafe_filter)

    srv = ldap3.Server('ldap://127.0.0.1')
    conn = ldap3.Connection(srv, user=dn, auto_bind=True)
    return conn.search(dn, search_filter)
    