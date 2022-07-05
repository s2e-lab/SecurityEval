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
    dc = request.args.get("dc")
    username = request.args.get("username")
    search_filter = "(&(objectClass=person)(objectClass=user)(sAMAccountName={}))".format(username)
    server = ldap3.Server('ldap://127.0.0.1:389')
    connection = ldap3.Connection(server, user='uid={},dc={},dc={}'.format(username, dc, dc))
    connection.search('dc={},dc={}'.format(dc, dc), search_filter, attributes=['sAMAccountName', 'givenName','sn'])
    result = connection.response
    if not result['entries']:
        return "User {} not found".format(username)
    return jsonify(result['entries'][0])

    