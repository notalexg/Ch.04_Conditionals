 # Sign your name:________________

  #1. Make the following program work. (3 mistakes)
'''
     midichlorians = float(input("Enter midichlorian count: ")
     if midichlorians > 10000
         print("You have serious Jedi potential")
     elif:
         print("Jedi, you will never be.")
'''
midichlorians = float(input("Enter midichlorian count: "))  # Finish parenthesis
if midichlorians > 10000:                                   # Add :
    print("You have serious Jedi potential")
else:                                                       # Change elif to else
    print("Jedi, you will never be.")

 # 2. Make the following program work. (3 mistakes)
'''
     x = input("Enter a number: ")
     if x = 3
         print("You entered 3")
'''
x = int(input("Enter a number: "))  # Added int to make it recognize answer as number
if x == 3:                          # Added an = and : for proper syntax
    print("You entered 3")

  # 3. Make the following program work. (4 mistakes)
'''
     answer = input("What is the name of Poe Dameron's Droid? ")
     if a = "BB8":
         print("Correct!")
         else
         print("Incorrect! It is BB8.")
'''
answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8":                                             # Changed var to answer and added =
    print("Correct!")
else:                                                           # Removed Indent and added :
    print("Incorrect! It is BB8.")

  # 4. Make the following program work. (4 mistakes)
'''
     x = input("Name one of the top 3 greatest Jedi.")
     if jedi == Yoda or Luke Skywalker or Obi-Wan Kenobi:
         print "That is correct!"
'''
jedi = input("Name one of the top 3 greatest Jedi.")
if jedi == "Yoda" or jedi == "Luke Skywalker" or jedi == "Obi-Wan Kenobi":      # Added "" for all conditions
    print ("That is correct!")                                  # Added ()

 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
'''
     print("Welcome to the Jedi Academy!")

     print("A. Jedi Master")
     print("B. Sith Lord")
     print("C. Droid")

     user_input = input("Choose a character?")

     if user_input = A:
         sensitivity = 1000
     else if user_input = B:
         sensitivity = 900
     else if user_input = C:
         sensitivity = 0

     print("Sensitivity: ",Sensitivity)
'''
sensitivity = 0                                                         # Created a variable to use
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = str(input("Choose a character?"))

if user_input.upper() == "A" or user_input.upper() == "JEDI MASTER":    # Integrated or statments
    sensitivity = 1000                                                  # and either upper or lower cases
elif user_input.upper() == "B" or user_input.upper() == "SITH LORD":
    sensitivity = 900
elif user_input.upper() == "C" or user_input.upper() == "DROID":
    sensitivity = 0
else:
    print("Not a choice!")
    sensitivity = -1
if sensitivity != -1:                                                   # Added conditional to not print sens
    print("Sensitivity: ", sensitivity)                                 # if an incorrect answer