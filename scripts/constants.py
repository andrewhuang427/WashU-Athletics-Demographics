headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

class Athlete:
    def __init__(self) -> None:
        self.sport = ""
        self.year = ""
        self.first_name = ""
        self.last_name = ""
        self.grade = ""
        self.hometown = ""
        self.highschool = ""
        self.link = ""
    
    def to_row(self):
        return [self.sport, 
                self.year, 
                self.first_name, 
                self.last_name, 
                self.grade, 
                self.hometown, 
                self.highschool, 
                self.link,]


def getYears(start, end):
    years = []
    for i in range(start,end):
        start = "20" + str(i)
        end = str(i+1)
        string = start + "-" + end
        years.append(string)
    return years


teams = [ 
    {
        "sport": "Baseball",
        "url": "https://www.washubears.com/sports/bsb/",
    },
    {
        "sport": "Men's Basketball",
        "url": "https://www.washubears.com/sports/mbkb/",
    },
    {
        "sport": "Men's Football",
        "url": "https://www.washubears.com/sports/fball/",
    },
    {
        "sport": "Men's Soccer",
        "url": "https://www.washubears.com/sports/msoc/",
    },
    {
        "sport": "Men's Tennis",
        "url": "https://www.washubears.com/sports/mten/",
    },
    {
        "sport": "Women's Basketball",
        "url": "https://www.washubears.com/sports/wbkb/",
    },
    {
        "sport": "Women's Golf",
        "url": "https://www.washubears.com/sports/wgolf/",
    },
    {
        "sport": "Women's Soccer",
        "url": "https://www.washubears.com/sports/wsoc/",
    },
    {
        "sport": "Women's Softball",
        "url": "https://www.washubears.com/sports/sball/",
    },
    {
        "sport": "Women's Tennis",
        "url": "https://www.washubears.com/sports/wten/",
    },
    {
        "sport": "Women's Volleyball",
        "url": "https://www.washubears.com/sports/wvball/",
    },
    {
        "sport": "Track and Field",
        "url": "https://washubears.com/sports/track/",
    },
    {
        "sport": "Swimming and Diving",
        "url": "https://washubears.com/sports/swimdive/",
    },
    {
        "sport": "Cross Country",
        "url": "https://washubears.com/sports/xc/",
    },
]