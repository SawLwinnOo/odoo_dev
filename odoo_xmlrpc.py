from xmlrpc import client

url = 'http://localhost:8069'
db = 'library'
username = 'admin'
password = ('admin')

common = client.ServerProxy('%s/xmlrpc/2/common' % url)
user_id = common.authenticate(db, username, password, {})
if user_id:
    print("Success: User id is", user_id)
else:
    print("Failed: wrong credentials")
