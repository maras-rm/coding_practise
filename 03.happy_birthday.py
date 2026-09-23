# Challenge: Ask user their date of birth in following format dd/mm/yyyy
# Then calculate and display:
# - The age of the user
# - The number of days the user has lived 
# - The week day (monday to sunday) corresponding with their DOB
# - The number of days left till next birthday
# - A hbd message if today is the users birthday

from datetime import *

# todays date:
today = date.today()

# users dob
dob = input("What is your date of birth (in format: dd/mm/yyyy)? ")
dobData = dob.split('/')
dobDay = int(dobData[0])
dobMonth = int(dobData[1])
dobYear = int(dobData[2])
dateOfBirth = date(dobYear, dobMonth, dobDay)

# age of user = todays year - year of birth (If current month/date are less than birth month/day minus 1 otherwise 0)
age = today.year - dobYear - ((today.month, today.day) < (dobMonth, dobDay)) 

print("You are " +str(age) +" years old.")

# Number of days the user has lived:
daysLived = (today - dateOfBirth).days

print("You have spent " + str(daysLived) + " days on Earth.")

# The week day of birth:
wkday = dateOfBirth.weekday() 
# Decoding num to weekday
match wkday:
    case 1:
        wkdResult = "Tuesday" 
    case 2:
        wkdResult = "Wednesday" 
    case 3:
        wkdResult = "Thursday" 
    case 4:
        wkdResult = "Friday" 
    case 5:
        wkdResult = "Saturday" 
    case 6:
        wkdResult = "Sunday" 
    case _:
        wkdResult = "Monday" 
print("You were born on a " + str(wkdResult))

# number of days till next birthday:
# if birthday has already happend? : 1 = no / 0 = yea
hasBDayHappened = (today.month, today.day) < (dobMonth, dobDay)

#if birthday is today:
if (date(today.year, dobMonth, dobDay) == today):
    print("Your birthday is today! Happy Birthday!")

# if happened: 
elif (hasBDayHappened == 0):
    nextYearsDate = date(((today.year) + 1), dobMonth, dobDay)
    numOfDaysTillNextBD = (nextYearsDate - today).days
    print ("Your birthday is in " + str(numOfDaysTillNextBD) + " days.") 

# if not happened:
else :
    dateOfThisBday = date(today.year, dobMonth, dobDay)
    numOfDaysTillBD = ((dateOfThisBday) - today).days
    print ("Your birthday is in " +str(numOfDaysTillBD) + " days.") 

