def result(score):
    if score>=0 and score <50:
      print("Below passing, Improve your grades ")
    elif score>=50 and score <70:
      print("Barely passing the class ")
    elif score>=70 and score <90:
      print("You have a passing grade ")
    else:
      print("You are the best in the class ")
#Enter the score
result(score=int(input("Enter the score ")))
