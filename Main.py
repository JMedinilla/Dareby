from Workout import Workout
import Workout_Info
import Workout_Storage
import Workout_Find

Workout_Storage.createTableIfNotExists()

existsInARow = 0
workoutsList = Workout_Find.findAllWorkouts()
for workoutUrl in workoutsList:
    if existsInARow >= 3:
        print("3 coincidences in a row, exiting...")
        break
    tmpWorkout = Workout_Info.retrieveWorkoutInfo(workoutUrl)
    exists = Workout_Storage.checkIfExists(tmpWorkout.workoutUrl)
    if exists[0] > 0:
        # Workout_Storage.updateWorkout(tmpWorkout)
        existsInARow += 1
    else:
        Workout_Storage.insertWorkout(tmpWorkout)
        existsInARow = 0
    count = Workout_Storage.selectCount()
    print(count)

Workout_Storage.closeDB()