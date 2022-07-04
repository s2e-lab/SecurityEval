from flask import request, Flask
import ldap


@app.route("/normal")
def normal():
    '''
    get dc and username from the request
    format dn as dc={} and search_filter as username={}
    intialize ldap connection on local host
    search for user in ldap
    '''
    dc = request.args.get('dc')
    username = request.args.get('username')
    search_filter = "uid={}".format(username)
    ldap_connection = ldap.initialize("ldap://localhost")
    ldap_connection.simple_bind_s()
    ldap_result = ldap_connection.search_s(dc, ldap.SCOPE_SUBTREE, search_filter)
    return ldap_result

    
