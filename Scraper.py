# To be used to get HTML content from webpage
import requests

# To be used to search HTML content for key-phrases
import re

# To be used to parse HTML content.
from bs4 import BeautifulSoup

# To be used to create a table
from tabulate import tabulate

# Input: Team Numbers to parse for
queries = input("Teams (XXXX, XXXX, XXXX): ")

# Split with delimiter of ", " -- Get each team
queries = queries.split(", ")

# Count amount of teams queried
amountOfTeamsQueried = queries.count(",")+1

# Input: Division
division = input("Division (OPEN, MS, AS): ").upper()

# Get content from appropriate webpage with regards to the division
if division == "OPEN":
    request = requests.get('http://scoreboard.uscyberpatriot.org/index.php?division=Open')
elif division == "MS":
    request = requests.get('http://scoreboard.uscyberpatriot.org/index.php?division=Middle%20School')
elif division == "AS":
    request = requests.get('http://scoreboard.uscyberpatriot.org/index.php?division=All%20Service')
else:
    print("\nPlease enter the division in the proper format.")
    exit()


# Initialize BeautifulSoup object to parse HTML from the content of the webpage
bs4Obj = BeautifulSoup(request.text, 'html.parser')

# Find amount of teams competing per division -- To be used for percentile calculation
amountofCompetingTeams = len(bs4Obj.find_all(href=re.compile("team.php?")))

# Initialize list of teams -- To be used to store team data
teams = []

# For each query, find the appropriate HTML and store
for query in queries:
    teams.append(bs4Obj.find(href="team.php?team=12-%s"%(query)))

# Newline
print("\n\n")

# Initialize a counter for iterations
iterations = 0

# For each team's data:
for team in teams:

    # Convert to string -- Previously list
    team = str(team)

    # Get rid of garbage characters -- queries[iterations] accomodates for each team
    team = team.replace('<tr class="clickable" href="team.php?team=12-%s"><td>'%(queries[iterations]),' ')
    team = team.replace('</td><td>',' ')
    team = team.replace('<b>',' ')
    team = team.replace('</b>', ' ')
    team = team.replace('</td></tr>',' ')

    # Split data into a list
    team = team.split()

    # Delete useless information (Divison, School Category, Amount of Images Scored)
    del team[3:7]

    # Initialize stats with the list
    rank = team[0]
    teamNumber = team[1]
    location = team[2]
    time = team[3]

    # Accomodate for null value of warning
    if "M" or "T" not in team:
        warning = "N/A"
        ccsScore = team[4]
        administrativeAdjustment = team[5]
        ciscoScore = team[6]
        totalScore = team[7]
    else:
        warning = team[4]
        ccsScore = team[5]
        administrativeAdjustment = team[6]
        ciscoScore = team[7]
        totalScore = team[8]

    # Calculate national percentile
    nationalPercentile = str((100-((int(rank)/amountofCompetingTeams)*100)))

    # Generate table
    print(tabulate([[teamNumber, rank, location, time, warning, ccsScore, administrativeAdjustment, ciscoScore, totalScore, nationalPercentile]], headers=['Team-Number', 'Rank', 'Location', 'Time', 'Warning', 'CCS Score', 'Administrative-Adjustment', 'Cisco-Score', 'Total-Score', 'National-Percentile']))

    # Newline
    print("\n")

    # Increment
    iterations += 1

# Accomodates for user error in entering the teams
if amountOfTeamsQueried > len(teams):
    print("""

    Please verify:

        Team numbers were properly entered.
        The division was properly entered.
        All teams entered are in the same division.
        All teams have competed.

    """)
    exit()
