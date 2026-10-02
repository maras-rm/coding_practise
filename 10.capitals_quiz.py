# Challenge: create a interactive quiz
# - display one capital city, and 4 non capital cities in random order
# - if you guess the correct city you score a point and move on to the next question - game ends when you guess incorrectly

# Challenge found - World Capital Cities Quiz - www.101computing.net/world-capital-cities-python-quiz/
import random

# List of non capital cities
non_capital_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
   "Miami", "Toronto", "Vancouver", "Montreal", "Calgary",
   "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide",
   "Manchester", "Birmingham", "Liverpool", "Glasgow",
   "Marseille", "Lyon", "Toulouse", "Nice", "Nantes",
   "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart",
   "Milan", "Naples", "Turin", "Palermo", "Genoa",
   "Barcelona", "Valencia", "Seville", "Zaragoza", "Málaga",
   "Porto", "Funchal", "Braga", "Setúbal",
   "Thessaloniki", "Patras", "Larissa", "Heraklion", "Volos",
   "Yokohama", "Osaka", "Nagoya", "Sapporo", "Kobe",
   "Shanghai", "Guangzhou", "Shenzhen", "Chongqing", "Chengdu",
   "Mumbai", "Bangalore", "Hyderabad", "Ahmedabad", 
   "Rio de Janeiro", "São Paulo", "Salvador", "Fortaleza", "Belo Horizonte", 
   "Medellin", "Cali", "Barranquilla", "Cartagena",
   "Lima", "Arequipa", "Trujillo", "Chiclayo", "Iquitos",
   "Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata",
   "Auckland", "Christchurch", "Hamilton", "Tauranga",
   "Dubai", "Sharjah", "Al Ain", "Ajman", "Istanbul",
   "Izmir", "Bursa", "Antalya", "Jeddah", "Mecca", 
   "Medina", "Dammam", "Durban", "Johannesburg",
   "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Lagos", 
   "Kano", "Ibadan", "Kaduna", "Port Harcourt", "Casablanca",
   "Fes", "Marrakech", "Tangier", "Accra", "Kumasi",
   "Tamale", "Sekondi-Takoradi", "Cape Coast", "Ho Chi Minh City", "Da Nang",
   "Hai Phong", "Can Tho", "Chiang Mai", "Pattaya", "Phuket",
   "Khon Kaen", "Penang", "Johor Bahru", "Ipoh", "Kuching",
    "Surabaya", "Bandung", "Medan", "Semarang"]

# Dictionary of capital cities
capital_cities = {
    "Paris": "France", "Berlin": "Germany", "Rome": "Italy",
    "Madrid": "Spain", "Lisbon": "Portugal", "Athens": "Greece",
    "Tokyo": "Japan",  "Beijing": "China", "New Delhi": "India",
    "Brasília": "Brazil", "Canberra": "Australia", "Ottawa": "Canada",
    "Washington, D.C.": "United States",  "Moscow": "Russia", "London": "United Kingdom",
    "Cairo": "Egypt", "Pretoria": "South Africa", "Nairobi": "Kenya",
    "Buenos Aires": "Argentina", "Lima": "Peru", "Oslo": "Norway",
    "Stockholm": "Sweden", "Helsinki": "Finland", "Copenhagen": "Denmark",
    "Wellington": "New Zealand", "Vienna": "Austria", "Brussels": "Belgium",
    "Amsterdam": "Netherlands", "Dublin": "Ireland", "Seoul": "South Korea",
    "Bangkok": "Thailand", "Kuala Lumpur": "Malaysia", "Jakarta": "Indonesia",
    "Singapore": "Singapore", "Ankara": "Turkey", "Riyadh": "Saudi Arabia",
    "Abu Dhabi": "United Arab Emirates", "Tehran": "Iran", "Baghdad": "Iraq",
    "Mexico City": "Mexico", "Santiago": "Chile",
    "Bogotá": "Colombia", "Quito": "Ecuador", "Caracas": "Venezuela",
    "Sucre": "Bolivia", "Asunción": "Paraguay", "Montevideo": "Uruguay",
    "Georgetown": "Guyana", "Havana": "Cuba", "Santo Domingo": "Dominican Republic",
    "San Salvador": "El Salvador", "Guatemala City": "Guatemala", "Tegucigalpa": "Honduras",
    "Managua": "Nicaragua", "San José": "Costa Rica", "Panama City": "Panama",
    "Kingston": "Jamaica", "Nassau": "Bahamas", "Port-au-Prince": "Haiti",
    "Philipsburg": "Sint Maarten", "Reykjavik": "Iceland", "Warsaw": "Poland",
    "Budapest": "Hungary", "Bucharest": "Romania", "Sofia": "Bulgaria",
    "Zagreb": "Croatia", "Ljubljana": "Slovenia", "Bratislava": "Slovakia",
    "Prague": "Czech Republic", "Belgrade": "Serbia", "Sarajevo": "Bosnia and Herzegovina",
    "Podgorica": "Montenegro", "Pristina": "Kosovo", "Skopje": "North Macedonia",
    "Tirana": "Albania", "Valletta": "Malta", "Nicosia": "Cyprus",
    "Yerevan": "Armenia", "Baku": "Azerbaijan", "Tbilisi": "Georgia",
    "Kiev": "Ukraine", "Minsk": "Belarus", "Vilnius": "Lithuania",
    "Riga": "Latvia", "Tallinn": "Estonia", "Hanoi": "Vietnam",
    "Phnom Penh": "Cambodia", "Vientiane": "Laos", "Rangoon": "Myanmar",
    "Manila": "Philippines", "Kathmandu": "Nepal", "Colombo": "Sri Lanka",
    "Dhaka": "Bangladesh", "Thimphu": "Bhutan", "Male": "Maldives",
    "Islamabad": "Pakistan", "Kabul": "Afghanistan", "Tashkent": "Uzbekistan",
    "Dushanbe": "Tajikistan", "Ashgabat": "Turkmenistan", "Bishkek": "Kyrgyzstan",
    "Nur-Sultan": "Kazakhstan", "Ulaanbaatar": "Mongolia", "Pyongyang": "North Korea",
    "Bandar Seri Begawan": "Brunei", "Taipei": "Taiwan", "Hong Kong": "Hong Kong",
    "Macau": "Macau", "Canberra": "Australia", "Rabat":"Morocco"
}



def questionGenerator():
    # Randomly select a capital city from dictionary of capital cities:
    capital_city = random.choice(list(capital_cities.items()))
    # capital_city = [0]: capital , [1] : country
    # Randomly select four non capital cities from the list of cities - but no repeats
    nonCap = []
    for i in range (4):
        randomCity = random.choice(non_capital_cities)
        while (randomCity in nonCap):
            randomCity = random.choice(non_capital_cities)
        nonCap.append(randomCity)
    
    # add capitalCity to same list as other cities:
    nonCap.append(capital_city[0])

    # shuffle list
    random.shuffle(nonCap) 

    # return the list of cities / correct answer
    return (nonCap, capital_city)


def startQuiz():
    # Flags to track score / if user get answer right
    score = 0
    correct = True

    # While user gets answer correct the game continues
    while (correct):
        # get question and answer:
        nonCap, capital_city = questionGenerator()

        # Print question
        print("Which of the following 5 cities is a capital City? ")
        for city in nonCap:
            print(city)

        # Ask user for answer
        usersChoice = input("Please enter the capital city: ")

        # User validation - so if not an option then reask question
        while (usersChoice.casefold() not in (city.casefold() for city in nonCap)):
            print("Error: Your choice was not in list")
            usersChoice = input("Please enter the capital city: ")

        # Check if player is correct and give feedback / update scoring
        if (usersChoice.lower() == capital_city[0].lower()):
            print("Correct: " + capital_city[0] + " is the capital of " + capital_city[1])
            score += 1
            print ("Your current score is: " + str(score))

        else :
            # if user got question wrong - tell right answer, score and end game
            print("Incorrect: The correct answer was " + capital_city[0] + " which is the capital of " + capital_city[1])
            print("Game Over. Your overall score is: " + str(score))

            # reset flags
            score = 0
            correct = False
        


if __name__ == "__main__":
    startQuiz()