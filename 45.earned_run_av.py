# Challenge: Write a function to calculate the earned run average in baseball
# ERA = No. earned runs * 9 and divided by number of innings pitched
# Return era rounded to 2dp

# Challenge can be found here: https://app.programiz.pro/community-challenges/preview/earned-run-average/info

def calculate_era(earned_runs, innings_pitched):
    # era calculations from above formula
    era = (earned_runs * 9) / innings_pitched

    # return rounded era to 2 dp
    return (round(era, 2))

if __name__ == "__main__":
    print(calculate_era(3,9)) # 3.0
    print(calculate_era(5,19)) # 2.37
    print(calculate_era(6,18)) # 3.0