username=input('enter your username:')
print('hello' + username)

password= input('enter your password:')

if password.isalpha():
    print('invalid password')
else:
    print('valid password')    

#say
name='x123edwin'
print(name[4:9])

email='bob123@gmail.com'
print(email[-1:-2])

email=input('enter email:')

if email[-10:]=='@gmail.com':
    print('account is from gmail')
if email[-10]== '@yahoo.com':
    print("account is from yahoo")






