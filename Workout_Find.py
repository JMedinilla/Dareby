#System
from bs4 import BeautifulSoup as BS
from urllib import request as URLRequest

urlBase = "https://darebee.com"
urlFilter = "https://darebee.com/workouts.html?start="

def findAllWorkouts():
    workoutList = []
    loopCount = 0
    loopMax = 9999
    while loopCount <= loopMax:
        tmpFilter = urlFilter + str(loopCount)
        workoutDivs = BS(URLRequest.urlopen(tmpFilter), "html.parser").select(".pull-none")
        if len(workoutDivs) < 1:
            loopMax = 0
        else:
            for div in workoutDivs:
                wkUrl = div.select_one("a[href]")["href"]
                workoutList.append(urlBase + wkUrl)
            loopCount += 15
        print(len(workoutList))
    return workoutList