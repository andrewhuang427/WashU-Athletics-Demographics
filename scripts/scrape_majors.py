from bs4 import BeautifulSoup
import requests
import pandas as pd

class Major:
    def __init__(self, name, school) -> None:
        self.name = name
        self.school = school

    def to_row(self):
        return [self.name, self.school]
    
url = "https://admissions.wustl.edu/academics/majors-and-programs/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

major_containers = soup.find_all("div", {"class", "post-item"})
majors = []
for container in major_containers:
    tags = container.find_all("a")
    if len(tags) >= 2:
        name = tags[0].text
        school = tags[1].text
        major = Major(name.strip(), school.strip())
        majors.append(major)

data = [x.to_row() for x in majors]

df = pd.DataFrame(data, columns=["name", "school"])
df.to_csv("./data/majors.csv", index=False)
