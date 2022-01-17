from app import db, Athlete
import pandas as pd

df = pd.read_csv("./data/players.csv")

for index, row in df.iterrows():
    athlete = Athlete(
                sport = row["Sport"],
                year = row["Year"],
                first_name = row["First Name"],
                last_name = row["Last Name"],
                grade = row["Class"],
                hometown = row["Hometown"],
                highschool = row["High School"],
                link = row["Link"])
    db.session.add(athlete)
    db.session.commit()
