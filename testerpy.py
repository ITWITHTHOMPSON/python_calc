def MetaAccount():
    username = input('ENTER YOUR USERNAME: ')
    password = input('ENTER YOUR PASSWORD: ')
    print('your username is: ' + username)
    
    print('your password is: ' + password)
MetaAccount()
    
class MetaAccount():
    def __init__(self, username, password):
        self.username = username
        self.password = password

account = MetaAccount('ITWithThompson', 'Squidward1996@')


print(account.username)
print(account.password)


mylist = ['tom', 'fred', 'tim']
print(mylist)
print(mylist[0])


print(str('+'))




