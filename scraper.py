# To be Used to Get HTML From Webpage
import requests

# To be Used to Search HTML With RegEX
import re

# To be Used to Parse HTML
from bs4 import BeautifulSoup

# To be Used to Format
from tabulate import tabulate

"""Function scrape()
@param queries: list of queried teams
@param division: division of teams
Description: The scrape() function takes two parameters, queries and
             divisions, and then outputs a scoreboard with all the teams in
             queries' scores.
"""

def scrape(queries, division):

    # Get Relevant Scoreboard According to Division
    if division == "OPEN":
        request = requests.get("http://scoreboard.uscyberpatriot.org/index.php?division=Open")
    elif division == "MS":
        request = requests.get("http://scoreboard.uscyberpatriot.org/index.php?division=Middle%20School")
    elif division == "AS":
        request = requests.get("http://scoreboard.uscyberpatriot.org/index.php?division=All%20Service")
    else:
        print("\nPlease enter the division in the proper format.")
        exit()

    # Instantiate BeautifulSoup Class to Parse HTML
    bs4Obj = BeautifulSoup(request.text, "html.parser")

    # Find Amount of Competing Teams -- To be Used for Percentile Calculation
    amountofCompetingTeams = len(bs4Obj.find_all(href=re.compile("team.php?")))

    # Initialize list of Teams for RAW DATA
    teams = []

    # For Each Query: Find Appropriate HTML Data
    for query in queries:
        teams.append(bs4Obj.find(href="team.php?team=13-%s"%(query)))

    # Initialize a Counter for Iterations -- To be Used for Refining Input
    iterations = 0

    # Initialize list for Final Output
    outputs = []

    # Initialize list of Teams -- To be Used for REFINED and SORTED Team Data
    refinedTeams = []

    # For Each Team's Data
    for team in teams:

        # Convert to String -- Previously list
        team = str(team)

        # Get Rid of Garbage Characters -- queries[iterations] accomodates for Each Team
        team = team.replace(" ", "_")
        team = team.replace("<tr_class=\"clickable\"_href=\"team.php?team=13-%s\"><td>"%(queries[iterations])," ")
        team = team.replace("</td><td>"," ")
        team = team.replace("<b>"," ")
        team = team.replace("</b>", " ")
        team = team.replace("</td></tr>"," ")

        # Split Data Into a List
        team = team.split()
        refinedTeams.append(team)

        # Increment
        iterations += 1

    # Sort by Rank
    refinedTeams.sort()

    # Assign Values to Indices
    for team in refinedTeams:

        try:
            rank = team[0]
            teamNumber = team[1]
            location = team[2]
            # Division Not Necessary (Index 3)
            tier = team[4]
            # Scored Images Not Necessary (Index 3)
            time = team[6]

            if len(team) == 9:
                warning = team[7]
                ccsScore = team[8]
            else:
                warning = "N/A"
                ccsScore = team[7]

            # Calculate National Percentile
            nationalPercentile = str((100-((int(rank)/amountofCompetingTeams)*100)))
            team.append(nationalPercentile)

        except:
            print("""
            Please verify:
                Team numbers were properly entered.
                The division was properly entered.
                All teams entered are in the same division.
                All teams have competed.
            """)
            exit()


        # Generate Table
        outputs.append(tabulate([[teamNumber, rank, tier, location, time, warning, ccsScore, nationalPercentile]], headers=["Team-Number", "Rank", "Tier", "Location", "Time", "Warning", "CCS Score", "National-Percentile"]))
        outputs.append("\n")


    # Print
    for output in outputs:
        print(output)

# Driver
if __name__ == "__main__":

    # Input: Team Numbers to parse ; get each team.
    queries = input("Teams (XXXX, XXXX, XXXX): ").split(", ")

    # Input: Division
    division = input("Division (OPEN, MS, AS): ").upper()

    # Newline
    print("\n\n")

    scrape(queries, division)
