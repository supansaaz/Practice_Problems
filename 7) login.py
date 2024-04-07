i=1
count=0
while i<=5:
    username=str(input("Enter username "))
    password=int(input("Enter password "))
    count+=1
    if username=="admin" and password==1234:
        print("No. of tries ",count)
        break
    elif username!="admin"  and password!=1234:
        print("Wrong Credentials")
    elif username!="admin":
        print("Incorrect Username")  
    elif password!=1234:
        print("Incorrect password") 
    i+=1
    
else:
    print("You are not the admin")
