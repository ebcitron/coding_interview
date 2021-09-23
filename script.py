import json
import sys

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



