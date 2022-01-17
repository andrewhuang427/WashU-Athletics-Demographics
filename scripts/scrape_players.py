import requests
from bs4 import BeautifulSoup
import pandas as pd
from constants import teams, headers, Athlete, getYears
import string
import re

years = getYears(16, 21)

columns = ["Sport", "Year", "First Name", "Last Name", "Class", "Hometown", "High School",  "Link"]

def get_players(sport, year, html):
    row = BeautifulSoup(html, "html.parser")
    rows = row.find_all("tr")
    players = []
    for row in rows:
        player = Athlete()
        player.sport = sport
        player.year = year
        
        # Name
        name = row.find("th").find("a", href=True)
        if name != None:
            trimmed = name.text.strip()
            parts = trimmed.split()
            player.first_name = parts[0]
            player.last_name =  parts[1]
            player.link = "https://washubears.com" + name["href"]

        # Class and High School / Hometown
        fields = row.find_all("td")
        for field in fields:
            value = field.text.strip()
            parts = value.split()

            if parts[0] == "Cl.:" or parts[0] == "Yr.:":
                player.grade = parts[1]
            
            elif parts[0] == "Hometown/High" or parts[0] == "Hometown:":
                hometownHighSchool = " ".join(parts[2:]).split(" / ")
                if len(hometownHighSchool) == 2:
                    player.hometown = hometownHighSchool[0]
                    player.highschool = hometownHighSchool[1]

        # if player.link != "":
        #     player.personal = personal_string(player.link)

        if player.first_name != "":
            row = player.to_row()
            if row != None:
                players.append(row)

    return players


def personal_string(url):
    print(url)
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    container = soup.find("div", {"class" : "synopsis"})
    if container != None:
        text = container.text
        parts = text.split("PERSONAL")
        if len(parts) >= 2:
            personal = parts[1].strip()
            personal_parts = re.split("…|\.{3,}|\n", personal)
            if len(personal_parts) > 0:
                major = personal_parts[0].strip().translate(str.maketrans('', '', string.punctuation)).strip()
                return major
    return ""


def scrape_teams():
    allAthletes = []
    for year in years:
        for team in teams:
            sportName = team["sport"]
            print(sportName + " -  " + year)
            linkBase = team["url"]
            url = linkBase + year + "/roster"
            
            response = requests.get(url, headers=headers)
            players = get_players(sportName, year, response.text)       
            for player in players:
                allAthletes.append(player)

    return allAthletes


df = pd.DataFrame(scrape_teams(), columns=columns)

df.to_csv("../data/players.csv", index=False)

