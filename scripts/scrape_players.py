import requests
from bs4 import BeautifulSoup
from utils.constants import getYears, teams, headers
from utils.MapBox import MapBox
from app import db, Athlete
from dotenv import dotenv_values
config = dotenv_values(".env")

mb = MapBox(config["MAP_BOX_TOKEN"])
years = getYears(13, 22)

def get_players(sport, year, html):
    row = BeautifulSoup(html, "html.parser")
    rows = row.find_all("tr")
    for row in rows:
        first_name = ""
        last_name = ""
        link = ""
        grade = ""
        hometown = ""
        highschool = ""

        # Name
        name = row.find("th").find("a", href=True)
        if name != None:
            trimmed = name.text.strip()
            parts = trimmed.split()
            first_name = parts[0]
            last_name = parts[1]
            link = "https://washubears.com" + name["href"]

        # Class and High School / Hometown
        fields = row.find_all("td")
        for field in fields:
            value = field.text.strip()
            parts = value.split()

            if parts[0] == "Cl.:" or parts[0] == "Yr.:":
                grade = parts[1]

            elif parts[0] == "Hometown:":
                hometownHighSchool = " ".join(parts[1:]).split(" / ")
                if len(hometownHighSchool) == 2:
                    hometown = hometownHighSchool[0]
                    highschool = hometownHighSchool[1]

            elif parts[0] == "Hometown/High":
                hometownHighSchool = " ".join(parts[2:]).split(" / ")
                if len(hometownHighSchool) == 2:
                    hometown = hometownHighSchool[0]
                    highschool = hometownHighSchool[1]

        hometown_coordinates = mb.getCoordinates(hometown)

        if first_name != "":
            # Save Player here
            athlete = Athlete(
                sport=sport,
                year=year,
                first_name=first_name,
                last_name=last_name,
                grade=grade,
                hometown=hometown,
                hometown_latitude=hometown_coordinates[0],
                hometown_longitude=hometown_coordinates[1],
                highschool=highschool,
                link=link
            )

            db.session.add(athlete)
            db.session.commit()


def scrape_teams():
    allAthletes = []
    for year in years:
        for team in teams:
            sportName = team["sport"]
            print(sportName + " -  " + year)
            code = team["code"]
            url = "https://washubears.com/sports/" + \
                str(code) + "/" + str(year) + "/roster"
            response = requests.get(url, headers=headers)
            get_players(sportName, year, response.text)

    return allAthletes


scrape_teams()
