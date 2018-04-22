import random

def printList(list):
    list.sort()
    for x in range(len(list)):
        print list[x].rstrip('\n'),
    print '\n'

fh = open('participants.txt', 'r')

participantList = []
for line in fh:
    participantList.append(line)
 	
print '\nSorted list of participants is:',
printList(participantList)
nParticipants = len(participantList)

teamA = []
teamB = []
while (nParticipants > 1):
    idx = random.randint(1, nParticipants)
    nParticipants = nParticipants - 1
    teamA.append(participantList.pop(idx-1))	
    idx = random.randint(1, nParticipants)
    nParticipants = nParticipants - 1
    teamB.append(participantList.pop(idx-1))	

'''
N = 100000
iter = N
sum = 0
while (iter > 0):
    iter = iter - 1
    sum = sum + random.randint(0, 1)
prob = sum/float(N)
print '[Test for fairness of coin toss:', prob, 'fraction of heads for', N, 'tosses\n'
'''

if (nParticipants > 0):
    toss = random.randint(0, 1)
    if (toss == 0):	
       print 'Extra player goes to Team A\n'
       teamA.append(participantList[0])	
    else:	
       print 'Extra player goes to Team B\n'
       teamB.append(participantList[0])	

print 'Team A is:',
printList(teamA)
print 'Team B is:',
printList(teamB)

fh.close()
quit()
