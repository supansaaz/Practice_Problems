#Customer Rating
rating=float(input("Please Rate Us out of 10 "))
if rating >0 and rating<=10 :
    if rating >=9:
        print("Thank you so much ")
    elif rating>=5 and rating<9:
        print("How we can improve ")
        feedback=str(input())
        print("We will work harder ")
    elif rating >=1 and rating<5:
        print("We are sorry to hear that ")
else:
    print("Invalid Rating! Please rate out of 10 ")