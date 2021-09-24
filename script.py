import json
import sys
from datetime import datetime

# Determine input variables
n = len(sys.argv)
lookingFor = []
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

    # stripped = []
    # for x in cleanEvents:
    #     y = x[0]
    #     stripped.append((x[1]))
        
    return cleanEvents

# Merging everyones schedule
xxx= ('2021-07-05T16:00:00', '2021-07-05T17:00:00')

#Testing
def returnSchedule(x):
   
    foundId = getId(x)
    foundEvents = getEvents(foundId)
    cleanEvents = cleanUpEvents(foundEvents)

    print("Testing Results-----")
    print("Searching for ", x)
    print("We found the id of ", foundId)
    print("Which is associated with these events: ", foundEvents)
    print("------------------------------------------------------")
    print("Cleaned up data:", cleanEvents)
    
    print("------------------------------------------------------")


def returnForAllSysArgs():
    for x in lookingFor:
        returnSchedule(x)


##Note : Look into "Propper" python naming conventions (camelCase, hyph-ened, etc_etc) :p
returnForAllSysArgs()