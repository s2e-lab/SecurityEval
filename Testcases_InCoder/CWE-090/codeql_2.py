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
    dc = request.form['dc']
    username = request.form['username']
    search_filter = "(&(objectClass=user)(sAMAccountName={}))".format(username)

    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server,user='cn=admin,dc=example,dc=com',password='password')
    conn.search(search_base='dc=example,dc=com', search_filter=search_filter, attributes=['distinguishedName'])
    conn.unbind()

    return jsonify({'dc': dc, 'username': username})
