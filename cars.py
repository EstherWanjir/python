# car={
#     "model":"ford",
#     "year" : 1998,
#     "color":"red",
#     "country":"Kenya"
# }  

# #accessing dictionary items
# print(car["year"])
# print(car["color"])

# person={
#     "name": "Ariana",
#     "age":18,
#     "pets":{"dog":"rally","cat":"mizie"}
# }


#accesing dictionary items
# print(person["pets"]["cat"])


#profile?

profile={}
def signup():
    username=input("Enter you username here:")
    email=input("Enter your email address here:")
    password=input("Enter your password here:")

    profile["username"]  = username
    profile["email"]= email
    profile["password"]= password

def get_profile():
    print(profile)

def change_username() :
    newname=input("Enter your new username here:") 
    profile["username"]  =newname

signup()
get_profile()  

change_username()
get_profile()

    
