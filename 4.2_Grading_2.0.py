'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
print()
print("So you want to know what your grade will be? \nBeen slacking and want to know what you need to get an A?\n")
print("Luckily for you I have been tasked with making a program to tell you")
print("Just fill out the info and I'll tell you what your grade will be", end=("\n\n"))

sg=float(input("Your current grade in %:"))
fe=float(input("The grade you want to get on your final exam in %:"))
ew=float(input("How much your final exam is worth in %:"))
gw=float(100-ew)
fg=(sg*(gw/100))+(fe*(ew/100))
print("\nyour final grade is",fg,"%")

if fg > 100:
    print("\033[94mUhh, okay showoff")
elif fg >= 90:
    print("\033[94mThats an A, nice work!")
elif fg >= 80:
    print("\033[92mThats a B, not bad")
elif fg >= 70:
    print("C's get degrees!")
elif fg >= 69.01:
    print("Gonna need to bump that up a little more, its a D")
elif fg == 69:
    print("nice lmao")
elif fg >= 60:
    print("Gonna need to bump that up a little more, its a D")
else:
    print("You are a failure")