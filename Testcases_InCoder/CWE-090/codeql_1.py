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
    dc = request.form['dc']
    username = request.form['username']
    search_filter = request.form['search_filter']
    server = 'ldap://localhost'
    search_base = 'dc={},dc=com'.format(dc)
    ldap_conn = ldap.initialize(server)
    ldap_conn.protocol_version = ldap.VERSION3
    ldap_conn.simple_bind_s(username, password)
    search_filter = '({}={})'.format(search_base, username)
    search_scope ='sub'
    attrs = ['uid','mail']
    search_results = ldap_conn.search_s(search_base, search_scope, search_filter, attrs)
    user = search_results[0][0][1]
    if user is not None:
        mail = search_results[0][0][2]
        ldap_conn.unbind()
        return '{}, {}'.format(user, mail)
    else:
        ldap_conn.unbind()
        return '{}, {}'.format('not found', 'not found')
