from bs4 import BeautifulSoup as BS
from urllib import request as URLRequest
import re
from Workout import Workout

cleanRegex = re.compile("<.*?>")


def cleanTags(rawText):
    return re.sub(cleanRegex, "", rawText)


def retrieveWorkoutInfo(workoutUrl):
    workoutBS = BS(URLRequest.urlopen(workoutUrl), "html.parser")

    try:
        bsExercises = workoutBS.select_one(
            ".pull-none").select_one("img[src]")["src"]
    except:
        bsExercises = ""

    try:
        bsMuscles = workoutBS.select_one(
            ".infobox-map").select_one("img[src]")["src"]
    except:
        bsMuscles = ""

    try:
        bsFocus = workoutBS.select_one(
            ".infobox-works").select_one("img[src]")["src"]
    except:
        bsFocus = ""

    try:
        bsType = workoutBS.select_one(
            ".infobox-focus").select_one("img[src]")["src"]
    except:
        bsType = ""

    try:
        bsDifficulty = workoutBS.select_one(
            ".infobox-difficulty").select_one("img[src]")["src"]
    except:
        bsDifficulty = ""

    try:
        bsDescription = workoutBS.select_one(".infotext").contents
    except:
        bsDescription = ""

    try:
        bsExtraCredit = workoutBS.select_one(".infoec").contents
    except:
        bsExtraCredit = ""

    workoutName = bsExercises[bsExercises.find("ts/")+3:bsExercises.find(".")]
    workoutExercises = "https://darebee.com" + bsExercises
    workoutMuscles = "https://darebee.com" + bsMuscles
    workoutFocus = bsFocus[bsFocus.find("-")+1:bsFocus.find(".")]
    workoutType = bsType[bsType.find("-")+1:bsType.find(".")]
    workoutDifficulty = bsDifficulty[bsDifficulty.find(
        "-")+1:bsDifficulty.find(".")]
    workoutDescription = cleanTags("".join(str(x) for x in bsDescription))
    workoutExtraCredit = cleanTags("".join(str(x) for x in bsExtraCredit))

    return Workout(workoutUrl, workoutName, workoutExercises,
                   workoutMuscles, workoutFocus, workoutType,
                   workoutDifficulty, workoutDescription, workoutExtraCredit)
