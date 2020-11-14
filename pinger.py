# Import Scraper File ; Brains of Code
import scraper

# To be Used for Delay
import time

# To be Used for Clear Screen
import os

# Input: Team Numbers to Parse ; Get Each Tean
queries = input("Teams (XXXX, XXXX, XXXX): ").split(", ")

# Input: Division
division = input("Division (OPEN, MS, AS): ").upper()

while True:
    scraper.scrape(queries, division)
    time.sleep(300)
    os.system("cls" if os.name=="nt" else "clear")
