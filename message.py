

class Login:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.error = "Enter a valid username and password"
    def check(self):
        if (self.id == log_id and self.password == log_pass):
            print("Login successful")
        else:
            print(self.error)

log = Login("admin",  "admin")
log_id = input("Enter your user ID: ")
log_pass = input("Enter password: ")

if log.check():
       alphabet='abcdefghijklmnopqrstuvwxyz'
       key=6
       newmessage=''
       message = input('Enter a message\n')

       for character in message:
        position=alphabet.find(character)
        newposition= (position+key)%26
        newcharacter=alphabet[newposition]
        newmessage+=newcharacter

       print('Encrypted message is\n',newmessage)
