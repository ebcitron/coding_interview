import json
import sys
from datetime import datetime, time, timedelta
from typing import List



#Hardcoded Variables
startDate = '2021-07-05T13:00:00'
endDate = '2021-07-07T21:00:00'
officeClosed = [('2021-07-05T21:00:00','2021-07-06T13:00:00'), ('2021-07-06T21:00:00','2021-07-07T13:00:00')]

lookingFor = []
# Determine input variables
n = len(sys.argv)
for i in range(1, n):
    lookingFor.append(sys.argv[i])
    


#Print out confirmation
print("FreetimeScript looking for:", lookingFor)


#Parse through the given JSON files to extract a users and schedules dictionary
users = json.load(open("./users.json"))
events = json.load(open("./events.json"))


# Figuring out whats most efficient in terms of adding the hours in between the 9-5 workdays in as their own scheduled times to be worked around.


#Splitting up events[] by user_id
# Checking lookingFor[] inputs for validity and their user_id

#Returns the id associated with the name its fed
def getId(name):
    foundId = next((person['id'] for person in users if person['name'] == name), False)
    return foundId

#Returns events associated with provided user_id
def getEvents(foundId):
    foundEvents = [event for event in events if event['user_id'] == foundId]

    return foundEvents

def cleanUpEvents(foundEvents):
    cleanEvents = []
    for x in foundEvents:
        cleanEvents.append((x['start_time'], x['end_time']))

    return cleanEvents

def convertCleanTostripped(cleanEvents):
    stripped = []
    for x in cleanEvents:
        a = convertToMinSinceStart(x[0])
        b = convertToMinSinceStart(x[1])
        newOne = (a,b)
        stripped.append(newOne)
     
    
    
    return stripped
    
# Merging everyones schedule



#Convert dateTime string into a workable number.

def convertToMinSinceStart(s):
    dt = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
    startDate = datetime.strptime('2021-07-05T13:00:00', "%Y-%m-%dT%H:%M:%S")
    tDelta = dt-startDate
    minsSince = int(tDelta.total_seconds()/60)
    
    # print("StartDate: ", startDate)
    # print("dt: ", dt)
    
    # print("dt object: ", {dt})
    # print("tDelta: ", tDelta)
    # print("minsSince: ", minsSince)
    return minsSince

def convertBackToDate(s):
    startDate = datetime.strptime('2021-07-05T13:00:00', "%Y-%m-%dT%H:%M:%S")


    #print("STartDate", startDate)
    dateProper = startDate + timedelta(minutes=s)
    
    #print("DateProper", dateProper)
    return dateProper




def combineOverlapping(sortedMergedList):
#Research conventional python syntax, I remember like 3 different ways of writing the same function out, and mix/matching as I go is getting gross to look at.


    sml = sortedMergedList

    print("SML: ", sml)

    if len(sml) == 0:
        return []

    clean = []

    x,y = sml[0]

    for (start, end) in sml[1:]:
        if x <= start and start <= y:
            y = max(end, y)
        else:
            clean.append((x,y))
            x, y = start, end
    clean.append((x,y))

    return clean


def returnTimesFree(timesBusy):

    tb = timesBusy

    tf = []
    start = []
    prevEnd = []    
    for x,y in zip(tb[::], tb[1::]):
        print(x[1],y[0])
  
        tf.append((convertBackToDate(x[1]), convertBackToDate(y[0])))
    
    print("tf: ", tf)
    
    
    # lst = [1,7,8,4,5,3]

    # for x,y in zip(lst[::],lst[1::]):
    #     print(x,y)
   

    return tf
def displayResults(finalResults):
    
    print("FINAL RESULTS")
    for x in finalResults:
        a = (x[0].strftime("%m/%d/%Y, %H:%M:%S"))
        b = (x[1].strftime("%H:%M:%S"))

        print(a, " --- ", b)
        
    return

    # st = 0
    # ed = 3360
    # x,y = tb[0]
    # for z in tb:
    #     if z[1]




        
    #   loop through tb looking at each set
    #   if x[0] >
    #
    #
    #

    # for y in sml:
    #     if not clean or clean[-1][1] < y[0]:
    #         clean.append(y)
    #     else:
    #         clean[-1][1] = max(clean[-1][1], y[1])

    # return clean


#Testing
def returnSchedule(x):
   
    foundId = getId(x)
    foundEvents = getEvents(foundId)
    cleanEvents = cleanUpEvents(foundEvents)
    stripped = convertCleanTostripped(cleanEvents)
   
    
    print("Testing Results-----")
    print("Searching for: ", x)
    print("We found the id of: ", foundId)
    print("Which is associated with these events: ", foundEvents)
    print("------------------------------------------------------")
    print("Cleaned up data: ", cleanEvents)
    print("------------------------------------------------------")
    print("Converted by mins Passed: ", stripped)
    

    print("------------------------------------------------------")

    return stripped




def returnForAllSysArgs():
    merged = []
    for x in lookingFor:
        merged.extend(returnSchedule(x))

    closedClean = convertCleanTostripped(officeClosed)
    print("ClosedClean: ", closedClean)
    merged.extend(closedClean)
    print("merge.extend closedclean: ", merged)
    merged.sort()
    print("merge sorted: ", merged)
    combined = combineOverlapping(merged)
#Now I have a merged list of all input schedules cleaned up into a comparable format of minsSinceStartTime/Date

#Will have to add a default "Schedule" of "events" for the hours closed in between each day
    # print("Merged list:  ", merged)
    print("Combined: ", combined)

    timesBusy = combined
    fTimes=returnTimesFree(timesBusy)
    displayResults(fTimes)
   # print("FreeTimes pre formatting", fTimes)
##Note : Look into "Propper" python naming conventions (camelCase, hyph-ened, etc_etc) :p
returnForAllSysArgs()




  
