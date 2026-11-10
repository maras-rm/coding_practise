# Challenge: Write a function to check if a student passed, failed or if the entered marks are invalid.
# The exam is graded from 0 to 100 - to pass need minimum of 40
# check and return the appropriate string - Pass, Fail, Invalid for a given score

# challenge can be found: https://app.programiz.pro/community-challenges/preview/pass-fail-or-invalid/info

def check_result(marks):
    # If score is between 40 - 100 the user has passed
    if (marks >= 40 and marks <= 100):
        return "Pass"
    # If score is between 0 and 40 the user has failed
    elif (marks >= 0 and marks < 40):
        return "Fail"
    # If it is any other input - it is not a valid score
    else:
        return "Invalid"

if __name__ == "__main__":
    print(check_result(45)) # Pass
    print(check_result(145)) # invalid
    print(check_result(25)) # Fail
    print(check_result(78)) # pass