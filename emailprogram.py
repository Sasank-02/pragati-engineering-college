email = "balaji@gmail.com"
pwd=123456
otp=5678
cemail=str(input("Enter the email:"))
cpwd=int(input("Enter the pwd:"))
cotp=input("enter the otp:")
if(email==cemail and pwd==cpwd and otp==cotp):
    print("Login successfully")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd):
    print("login failed due to pwd")
elif(email!=cemail and pwd!=cpwd):
    print("login failed due to both mail and pwd")
elif(otp != cotp):
    print("Login failed due to wrong otp")
