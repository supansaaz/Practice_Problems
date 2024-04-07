print("Do You want to watch a movie ?")
choice = str(input("Yes or No"))
if choice=='Yes':
    genre=str(input("What genre do you want to watch "))
    if(genre=='Comedy'):
        print("You can watch the \"Hangover Trilogy\"")
    else :
        print("You can Watch \"Top Gun\"")
else :
    print("You should watch a TV series")


