print("Welcome to my The originals quiz!")

score = 0

playing = input("Do you wanna play the game bro? ")

if playing.lower() != "yes":
    quit()

print("Alright lets play (:")

answer = input("""Which of the following is correct:
               
                  A- klaus is stronger than elijah.
                  B- A.
                  C- All of the above.
                  D- klaus is gay.
                  
                  """)

if answer.upper() == "D":
    print("Correct!!")
    score = score + 1
else:
    print("Incorrect!")
   

answer = input("""Which of the following is correct:
               
                  A- Dahlia is a mikaelson.
                  B- The hollow is 1000 years old.
                  C- All of the above.
                  D- Shall we?
                  
                  """)
if answer.upper() == "D":
    print("Correct!!")
    score = score + 1
else:
    print("Incorrect!")
    
answer = input("""Which of the following is correct:
               
                  A- Rebekah isn't the first ever vampire.
                  B- Rebekah isn't stronger than Fin.
                  C- All of the above.
                  D- Not C.
                  
                  """)
if answer.upper() == "D":
    print("Correct!!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("""Which of the following is correct:
               
                  A- Matt donavan had a stronger plot armor than damon salvatore.
                  B- Vincent griffith was the best person to use witch-craft ever.
                  C- All of the above.
                  D- Not C.
                  
                  """)
if answer.upper() == "C":
    print("Correct!!")
    score = score + 1
else:
    print("Incorrect!")


if score < 2:
    print("You have failed the test sadly): ")   
elif score == 2:
    print("Congrats!! you have passed the test and got 2/4 overall score.")
elif score == 3:
    print("Congrats!! you have passed the test and got 3/4 overall score.")   
else:
    print("Congrats!! you have passed the test and got 4/4 overall score.")


