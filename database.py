from pymongo import MongoClient
from util import hash_string

client = MongoClient()

class UserManager:
    def __init__(self, db):
        self.db = client[db]

    def isRegistered(self, username):
        result = self.db.users.find_one({
            'username': username
        })

        return bool(result)
    
    def login(self, username, password):
        result = self.db.users.find_one({
          'username': username,
          'passhash': hash_string(password)
        })

        print username, password
        print result
        
        if result is None:
            return False, 'Invalid username or password.'
        else:
            return True, 'Successfully logged in!'

    def register(self, username, password, confirm):
        if password != confirm:
            return False, 'Passwords must match.'
        elif self.isRegistered(username):
            return False, 'User already exists.'
        else:
            self.db.users.insert_one({
                'username': username,
                'passhash': sha512(password).hexdigest()
            })

            return True, 'Successfully registered!'

    def isAdmin(self, username):
        result = self.db.admins.find_one({
            'username': username
        })

        return bool(result)
            
    def makeAdmin(self, username):
        if isAdmin(username):
            return False, 'User is already an admin'
        else:
            return True, 'User is now an admin'

    def authAdmin(self, username, password):
        result = self.db.admins.find_one({
            'username': username,
            'passhash': hash_string(password)
        })

        if result is None:
            return False, 'Invalid username or password.'
        else:
            return True, 'Successfully logged in!'
