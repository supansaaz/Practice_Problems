n=int(input("Enter the number "))
i=1
while i<=n:
    name=str(input("Enter your name "))
    age=int(input("Enter your age "))
    if age>=18:
        print("Welcome to the party ")
    else:
        print("You must be 18 to drink ")
    i+=1
