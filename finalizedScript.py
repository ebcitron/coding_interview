import json
import sys
from datetime import datetime, timedelta




#Hardcoded Variables
startDate = '2021-07-05T13:00:00'
endDate = '2021-07-07T21:00:00'
officeClosed = [('2021-07-05T21:00:00','2021-07-06T13:00:00'), ('2021-07-06T21:00:00','2021-07-07T13:00:00')]

lookingFor = []
# Determine input variables
n = len(sys.argv)
for i in range(1, n):
    lookingFor.append(sys.argv[i])
    
#Parse through the given JSON files to extract a users and schedules dictionary
users = json.load(open("./users.json"))
events = json.load(open("./events.json"))


#Splitting up events[] by user_id
#Checking lookingFor[] inputs for validity and their user_id

#Returns the id associated with the name its fed
def getId(name):
    foundId = next((person['id'] for person in users if person['name'] == name), False)
    return foundId

#Returns events associated with provided user_id
def getEvents(foundId):
    foundEvents = [event for event in events if event['user_id'] == foundId]

    return foundEvents


#Cleans the data, passing it into a list of objects with start and end times
def cleanUpEvents(foundEvents):
    cleanEvents = []
    for x in foundEvents:
        cleanEvents.append((x['start_time'], x['end_time']))

    return cleanEvents

#Function to run my datetime magick, converting the values out of strings into ints
def convertCleanTostripped(cleanEvents):
    stripped = []
    for x in cleanEvents:
        a = convertToMinSinceStart(x[0])
        b = convertToMinSinceStart(x[1])
        newOne = (a,b)
        stripped.append(newOne)
     
    
    
    return stripped
    

#Convert dateTime string into a workable number.

def convertToMinSinceStart(s):
    dt = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
    startDate = datetime.strptime('2021-07-05T13:00:00', "%Y-%m-%dT%H:%M:%S")
    tDelta = dt-startDate
    minsSince = int(tDelta.total_seconds()/60)
    
    return minsSince
#Reverts a normal number back into a date value based on the starting date/time
def convertBackToDate(s):
    startDate = datetime.strptime('2021-07-05T13:00:00', "%Y-%m-%dT%H:%M:%S")


    dateProper = startDate + timedelta(minutes=s)

    return dateProper


#Takes the sorted list containing all of everyones events, and reduces it by combining overlapping tiimeframes into single timeslots
def combineOverlapping(sortedMergedList):
    sml = sortedMergedList


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

#Compares the start time of 0 to the first busy minute, and every subsequent busy period end_time with the next busy periods starttime, and the last appointments end_time with the final possible minute before the office closes, appending these gaps into a new list of time free of appointments. 
def returnTimesFree(timesBusy):

    tb = timesBusy
    tf = []

    start = 0
    end = 3360
    if tb[0][0]>start:
        a=(convertBackToDate(0),convertBackToDate(tb[0][0]))
        tf.append(a)
  
    for x,y in zip(tb[::], tb[1::]):
  
        tf.append((convertBackToDate(x[1]), convertBackToDate(y[0])))
    
    if tb[-1][1]<end:
        a =(convertBackToDate(tb[-1][1]),convertBackToDate(end))
        tf.append(a)
    return tf

#Handles the formatting and printing of final results into the terminal
def displayResults(finalResults):
    
    print("Free Schedule")
    
    print("------------------------------------------------------")

    for x in finalResults:
        a = (x[0].strftime("%m/%d/%Y, %H:%M:%S"))
        b = (x[1].strftime("%H:%M:%S"))

        print(a, " --- ", b)

    print("------------------------------------------------------")
        
    return


#Runs the above functions that handle the finding, sorting, and cleaning up of data on the names passed in as arguements
def returnSchedule(x):
   
    foundId = getId(x)
    foundEvents = getEvents(foundId)
    cleanEvents = cleanUpEvents(foundEvents)
    stripped = convertCleanTostripped(cleanEvents)

    return stripped



#Runs the above function on each name passed in argv, merges them into a single list, sends that list off to be further proccessed, and calls the function to display the final results
def returnForAllSysArgs():
    merged = []
    for x in lookingFor:
        merged.extend(returnSchedule(x))

    closedClean = convertCleanTostripped(officeClosed)

    merged.extend(closedClean)

    merged.sort()

    combined = combineOverlapping(merged)



    timesBusy = combined
    fTimes=returnTimesFree(timesBusy)
    displayResults(fTimes)

#And finally, we run it all by calling the above function!
returnForAllSysArgs()
