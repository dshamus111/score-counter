from tinydb import TinyDB, Query
import sys

db = TinyDB('scoredb.json')
Score = Query()

#db.insert({'wins': 0, 'loses': 0})

argument = sys.argv[1]
score = db.all()
wins = score[0]["wins"]
loses = score[0]["loses"]

if argument == 'w':
    db.update({'wins': wins + 1})
    wins = wins + 1

if argument == 'l':
    db.update({'loses': loses + 1})
    loses = loses + 1

if argument == 'r':
    db.update({'wins': 0})
    db.update({'loses': 0})
    wins = 0
    loses = 0

f = open("winloss.txt", "w")
f.write("Score: " + str(wins) + "-" + str(loses))
f.close()

print(str(wins) + "-" + str(loses))