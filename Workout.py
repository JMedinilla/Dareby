class Workout(object):
    workoutUrl = ""
    workoutName = ""
    workoutExercises = ""
    workoutMuscles = ""
    workoutFocus = ""
    workoutType = ""
    workoutDifficulty = ""
    workoutDescription = ""
    workoutExtraCredit = ""

    def __init__(self, url, name, exercises, muscles, focus, wType, difficulty, description, extraCredit):
        self.workoutUrl = url
        self.workoutName = name
        self.workoutExercises = exercises
        self.workoutMuscles = muscles
        self.workoutFocus = focus
        self.workoutType = wType
        self.workoutDifficulty = difficulty
        self.workoutDescription = description
        self.workoutExtraCredit = extraCredit

    def printWorkout(self):
        print("URL: " + self.workoutUrl)
        print("\nName: " + self.workoutName)
        print("\nExercises: " + self.workoutExercises)
        print("\nMuscles: " + self.workoutMuscles)
        print("\nFocus: " + self.workoutFocus)
        print("\nType: " + self.workoutType)
        print("\nDifficulty: " + self.workoutDifficulty)
        print("\nDescription: " + self.workoutDescription)
        print("\nExtra credit: " + self.workoutExtraCredit)
