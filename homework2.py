#ask user to enter a string.
user=input("Enter a sentence:")

print(len(user))
print(user[0])
print(user[:4])
print(user[:-4])
print(user[::-1])
if user[:7]:
    print('it is there')
else:
    print('not there')  
      
