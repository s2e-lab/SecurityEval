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
    search_filter = f"uid={username}"
    dn = f"dc={dc}"
    ldap_connection = ldap3.Connection(ldap3.Server('ldap://localhost:389'), auto_bind=True)
    ldap_connection.search(dn, search_filter)
    return ldap_connection.entries[0].entry_to_json()
