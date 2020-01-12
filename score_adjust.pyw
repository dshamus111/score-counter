from tinydb import TinyDB, Query
import sys

db = TinyDB('scoredb.json')
Score = Query()

#db.insert({'wins': 0, 'loses': 0})

argument = sys.argv[1]
score = db.all()
wins = score[0]["wins"]
losses = score[0]["loses"]

if argument == 'w':
    db.update({'wins': wins + 1})
    wins = wins + 1

if argument == 'l':
    db.update({'loses': losses + 1})
    losses = losses + 1

if argument == 'r':
    db.update({'wins': 0})
    db.update({'loses': 0})
    wins = 0
    losses = 0

lines = []
replacements = {'%wins':str(wins), '%losses':str(losses), '%total':str(wins + losses)}

with open('format.txt') as infile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        lines.append(line)
with open('winloss.txt', 'w') as outfile:
    for line in lines:
        outfile.write(line)

print(lines)