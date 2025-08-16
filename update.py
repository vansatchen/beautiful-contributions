#!/usr/bin/env python

import os
import time
from datetime import datetime
import git


# Available patterns:
# "fillDark" - just fill all contributions like 1 commit per day
# "fillLight" - just fill all contributions like 4 commits per day
# "chess" - make your contributions like chessboard
pattern = "chess"

timeNow = datetime.now()
numWeekDay = timeNow.weekday()
numWeekYear = timeNow.isocalendar().week

scriptPath = os.path.abspath(__file__).split('/')
workPath = '/'.join(scriptPath[:-1])


def updateTextFile():
    timeNow = datetime.now()
    with open(workPath + '/update.txt', 'w') as textFile:
        textFile.write(str(timeNow) + '\n')


def makeCommit(times):
    for i in range(times):
        updateTextFile()
        time.sleep(3)


def drawPattern(pattern):
    if pattern == "chess":
        if numWeekYear % 2 == 1:
            if numWeekDay % 2 == 1:
                makeCommit(3)
        else:
            if numWeekDay % 2 == 0:
                makeCommit(3)


drawPattern(pattern)
