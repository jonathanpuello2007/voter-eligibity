# Registration for voting
print("Welcome to Voter Eligibity Checker.")
print("Let's see if you are eligible to vote")
print()
age = int(input("please enter your age:"))
citizen = input("Are you a legal citizen of the US?(y/n):")
registration = input("Are you registered to vote? (y/n):")
incarceration_status = input("are you currently incarcerated?.")
eligible = False

if age >=18 and citizen == "y" and registration == "y" and incarceration_status == "n":
  eligible = True

if eligible:
  print("You are eligible to vote!")
else:
  print("Sorry, you are not eligible to vote.")
  
 

