# Challenge: write a function to find the date of the first Tuesday of a given month and year.

# Challenge can be found here: https://app.programiz.pro/community-challenges/preview/first-tuesday/info

from datetime import datetime

def first_tuesday(month, year):
    # The first tuesday of a month can fall only on 7 days (as thats how many days are in a week)
    for i in range(1, 7):
        # Get that as a date
        dateDay = datetime(year,month,i)
        # if that weekday (which is a num, starting from 0 - 6 )
        # is 1 (Tuesday) - that date is the first tuesday of the month - so return that date - without time stamp
        if (dateDay.weekday() == 1):
            return dateDay.date()
        

if __name__ == "__main__":
    print(first_tuesday(1,2022)) # '2022-01-04'
    print(first_tuesday(11,2026)) # '2026-11-03'
    print(first_tuesday(7,2025)) # '2025-07-01'