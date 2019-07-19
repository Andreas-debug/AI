#Shortest-Path-AI (based on Mk 5)
#This Q-Learning AI is reward-based, meaning you give it/take away points depending on how well it does
#It takes in the data-list/matrix and trains an AI to go to a specific spot

import numpy as np

#Matrix over all connected areas (0 means not a path, everything else is)
#You can change the negatives to the distance, and the AI finds the shortest one
#The one's with 100 lead to the correct area
#X-axis corresponds to paths out of one area, and Y-axis to the are you're in
areas = [       "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
data =        [[ 0, -1, -1,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0],   #A
               [-1,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0],   #B
               [-1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],   #C
               [ 0,  0, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0],   #D
               [ 0,  0,  0, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0],   #E
               [ 0,  0,  0, -1,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0],   #F
               [ 0,  0,  0,  0, -1, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0],   #G
               [ 0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  100], #H
               [ 0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0],   #I
               [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0],   #J
               [ 0,  0,  0,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0],   #K
               [ 0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0, -1,  0,  0],   #L
               [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0],   #M
               [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  100], #N
               [ 0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0]    #O
                ]

#Set goalArea to the area you want the AI to go to, it should be the index of the column of the matrix 
goalArea = 14

#Sets the reward-matrix with its data
R = np.matrix(data)

#Creates same matrix as above, but only filled with null
Q = np.matrix(np.zeros([len(data), len(data[0])])) 

#Future actions matter (0 = 0 * maxValue in future, 1 = 1 * maxValue in future)
gamma = 0.95 

#Chooses which area the first "episode" starts in
initialState = np.random.randint(0, (len(data)-1))

#Returns all available actions
def availableActions(state):
    currentStateRow = R[state, ]
    avAct = np.where(currentStateRow != 0) [1]
    return avAct

#Sets availableAct to all available actions
availableAct = availableActions(initialState)

#Chooses the next action, sometimes random and sometimes the best one
def sampleNextAction(availableActionsRange):
    nextAction = int(np.random.choice(availableActionsRange, 1))
    return nextAction

#Sets action to the next action
action = sampleNextAction(availableAct)

#Updates the state based on the action and gamma
def update(currentState, action, gamma):
    maxIndex = np.where(Q[action, ] == np.max(Q[action, ]))[1]

    if maxIndex.shape[0] > 1:
        maxIndex = int(np.random.choice(maxIndex, size=1))
    else:
        maxIndex = int(maxIndex)
    maxValue = Q[action, maxIndex]

    Q[currentState, action] = R[currentState, action] + gamma * maxValue

update(initialState, action, gamma)


#******************************TRAINING******************************


for i in range(200000): #Range = amount of steps taken
    currentState = np.random.randint(0, int(Q.shape[0]))
    availableAct = availableActions(currentState)
    action = sampleNextAction(availableAct)
    update(currentState, action, gamma)

print("Trained Q Matrix: ")
print(np.round((Q / np.max(Q) * 100), decimals= 2
))


#******************************TESTING******************************


#Set current state to starting postition for the test
currentState = 3
steps = [currentState]

#You can change the number to the specific spot you want it to go to
while currentState != goalArea:
    nextStepIndex = np.where(Q[currentState, ] == np.max(Q[currentState, ]))[1]

    if nextStepIndex.shape[0] > 1:
        nextStepIndex = int(np.random.choice(nextStepIndex, size=1))
    else: 
        nextStepIndex = int(nextStepIndex)
    steps.append(nextStepIndex)
    currentState = nextStepIndex

finalPath = "Walked "
finalPath += "from " + str(areas[steps[0]])
for a in steps[1:-1]:
    finalPath += ", to " + str(areas[a])
finalPath += " and stopped at " + str(areas[steps[-1]])

print("\n")
print(finalPath)