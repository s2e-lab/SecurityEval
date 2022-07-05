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
    dn = request.form['dn']
    username = request.form['username']
    search_filter = request.form['search_filter']
    server = ldap.initialize('ldap://127.0.0.1')
    server.search(dn, search_filter, attributes=['dn','sn', 'cn'])
    attrs = ['cn','sn', 'givenName','sn', 'displayName']
    results = server.entries[0]
    search_string = '{}={}'.format(username, username)
    for attr in attrs:
        results.pop(attr)
    return render_template('search.html', results=results, dn=dn, search_filter=search_string)

    
