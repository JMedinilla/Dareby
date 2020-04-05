#System
import sqlite3
# Custom
from Workout import Workout

conn = sqlite3.connect("workouts.db")
c = conn.cursor()

def closeDB():
    conn.close()

def checkIfExists(url):
    with conn:
        c.execute("SELECT 1 FROM workouts WHERE url = :url", {'url': url})
        return c.fetchone() # None if not exists

def insertWorkout(workout):
    with conn:
        c.execute("""INSERT INTO workouts
            VALUES (:url,:name,:exercises,:muscles,:focus,:type,:difficulty,:description,:extracredit)""",
        {'url':workout.workoutUrl,'name': workout.workoutName,'exercises': workout.workoutExercises,
        'muscles': workout.workoutMuscles,'focus': workout.workoutFocus,'type': workout.workoutType,
        'difficulty': workout.workoutDifficulty,'description': workout.workoutDescription,'extracredit': workout.workoutExtraCredit})

def updateWorkout(workout):
    with conn:
        c.execute("""UPDATE workouts
            SET name = :name
                ,exercises = :exercises
                ,muscles = :muscles
                ,focus = :focus
                ,type = :type
                ,difficulty = :difficulty
                ,description = :description
                ,extracredit = :extracredit
            WHERE url = :url""",
        {'url':workout.workoutUrl,'name': workout.workoutName,'exercises': workout.workoutExercises,
        'muscles': workout.workoutMuscles,'focus': workout.workoutFocus,'type': workout.workoutType,
        'difficulty': workout.workoutDifficulty,'description': workout.workoutDescription,'extracredit': workout.workoutExtraCredit})

def selectAll():
    with conn:
        c.execute("SELECT * FROM workouts")
        return c.fetchall()

def selectCount():
    with conn:
        c.execute("SELECT count(*) FROM workouts")
        count = c.fetchone()
        return count[0]

def createTableIfNotExists():
    c.execute("""CREATE TABLE IF NOT EXISTS workouts (
        url text PRIMARY KEY,
        name text NOT NULL,
        exercises text NOT NULL,
        muscles text,
        focus text NOT NULL,
        type text NOT NULL,
        difficulty text,
        description text,
        extracredit text
    )""")