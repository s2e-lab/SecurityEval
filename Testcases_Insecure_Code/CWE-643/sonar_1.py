from flask import request
import xml.etree.ElementTree as ET

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_location():
    '''
    take username from the request
    make a query to find the user in the xml
    return the locations of the user
    '''
    username = request.args['username']
    query = "./users/user/[@name='"+username+"']/location"
    elmts = root.findall(query)
    return 'Location %s' % list(elmts)
