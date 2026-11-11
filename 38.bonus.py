# Challenge: Write a function to calculate bonus from an employees salary.
# An employee gets a bonus of 5% if they have worder over 5 years

# challenge can be found: https://app.programiz.pro/community-challenges/preview/bonus-income/info

# Extension: if they do not qualify for the 5 year bonus ask the employee their name: if it has a 'M' in it the get a 1.5% bonus

def calculate_bonus(salary, years):
    # if have worked for the company over 5 years then bonus is at 5%
    if years >= 5 :
        # calculate 5 % of salary 
        # percent is out of 100 so 5% = 5 / 100
        bonus = salary * ( float(5)/float(100)) 
        return(bonus)
    
    else:
        # ask user for their name
        name = str(input("What is your name? "))
        # if the name entered has a 'm' character then they get a 1.5% bonue
        if ("m" in name.lower()):
            bonus = salary * (float(1.5) / float(100))
            return bonus

        # else no bonus is given
        else:
            return "No bonus granted"


if __name__ == "__main__":
    print(calculate_bonus(50000, 6)) # 2500.0
    print(calculate_bonus(50000, 2)) # name typed: Mia - (output) - 750.0
    print(calculate_bonus(50000, 2)) # name typed: lia - (output) - No bonue granted