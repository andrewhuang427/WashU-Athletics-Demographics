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
                self.link, ]


def getYears(start, end):
    years = []
    for i in range(start, end):
        start = "20" + str(i)
        end = str(i+1)
        string = start + "-" + end
        years.append(string)
    return years


teams = [
    {"sport": "Baseball", "code": "bsb"},
    {"sport": "Men's Basketball", "code": "mbkb", },
    {"sport": "Men's Football", "code": "fball", },
    {"sport": "Men's Soccer", "code": "msoc", },
    {"sport": "Men's Tennis", "code": "mten", },
    {"sport": "Women's Basketball", "code": "wbkb", },
    {"sport": "Women's Golf", "code": "wgolf", },
    {"sport": "Women's Soccer", "code": "wsoc", },
    {"sport": "Softball", "code": "sball", },
    {"sport": "Women's Tennis", "code": "wten", },
    {"sport": "Women's Volleyball", "code": "wvball", },
    {"sport": "Track and Field", "code": "track"},
    {"sport": "Swimming and Diving", "code": "swimdive"},
    {"sport": "Cross Country", "code": "xc"},
]