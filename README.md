# CyberPatriotScraper
This bundle is meant to be used to get statistics of different CyberPatriot teams using the CyberPatriot scoreboard.

	Required Dependencies:

		python3
    	requests
    	bs4
    	tabulate
		pinger.py
		scraper.py
    
python3 is the language in which the script is written in. If python3 is not installed on the system where the script will be ran, install it by going to https://www.python.org/downloads/ and downloading the latest stable version. From there, follow all directions. To run the file after all dependencies are installed, execute python3 pinger.py

requests is a module that is used to get the HTML content of the scoreboard. If not installed already, run 'pip install requests' or 'pip3 install requests'

bs4 is a module that is used to parse the HTML content of the scoreboard. If not installed already, run 'pip install bs4' or 'pip3 install bs4'

tabulate is a module that is used to output the results in an easy-to-read format.

pinger.py is optional. It can be used to generate a live scoreboard. If the user does not desire a live scoreboard, scraper.py can be used standalone.

scraper.py is the brains of the bundle. It is used to scrape data as well as output the data in a readable format.

Input Format:

	Teams (XXXX, XXXX, XXXX): >>> XXXX, XXXX, XXXX, XXXX...
	Division (OPEN, MS, AS): >>> OPEN || MS || AS

Output Format:

	See Sample Use.png
