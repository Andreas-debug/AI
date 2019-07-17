# -*- coding:latin-1 -*-

import random
import math


seed = random.randint(1,100000000000)
print("Current Seed: " + str(seed))
random.seed(seed)

class Input: #takes in its value, most of the time a random number
    def __init__(self, value):
        self.value = value

class Neuron: #takes in its value from a synapse
    def __init__(self, value=0, connections=[]):
        self.value = value
        self.connections = connections

class Synapse: #takes in its value and weight, can be from Neuron, other synapse, or random number
    def __init__(self, weight, value, connection_in, connection_out):
        self.weight = weight
        self.value = value
        self.connections = [connection_in, connection_out]

class First_AI: #Needs target x and y position to operate
    def __init__(self, x_pos, y_pos, Syn_Values = []):
        self.Input1 = []
        self.Synapse1 = []
        self.Neuron1 = []
        self.Synapse2 = []
        self.Output = []

        self.Input1.append(Input(x_pos)) #two neurons for directions, position of x and y
        self.Input1.append(Input(y_pos))
                
        for i in range(4): #Neuron1 (1st layer of Neurons)
            self.Neuron1.append(Neuron(0))

        for i in range(8): #Synapse1 (1st layer of Synapses(between In and L1))
            #Weight, Value, Connection_In, Connection_Out
            temp_int_1 = random.randint(0,1)
            temp_int_2 = random.randint(0,3)
            self.Synapse1.append(Synapse(random.randint(-100,100)/100, self.Input1[temp_int_1].value, temp_int_1, temp_int_2))

            self.Neuron1[temp_int_2].value += self.Synapse1[i].value * self.Synapse1[i].weight
            self.Neuron1[temp_int_2].connections.append(self.Synapse1[i]) #adds synapse to connections list of target neuron

        for each_neuron in self.Neuron1:
            temp_float = 1.0
            for i in range(len(each_neuron.connections)):
                temp_float += 1.0
            each_neuron.value/=temp_float

        for i in range(2): #Output
            self.Output.append(Neuron(0))

        for i in range(8): #Synapse2 (2nd layer of Synapses(between L1 and Out))
            #Weight, Value, Connection_In, Connection_Out
            temp_int_1 = random.randint(0,3)
            temp_int_2 = random.randint(0,1)
            self.Synapse2.append(Synapse(random.randint(-100,100)/100, self.Neuron1[temp_int_1].value, temp_int_1, temp_int_2))

            self.Output[temp_int_2].value += self.Synapse2[i].value * self.Synapse2[i].weight
            self.Output[temp_int_2].connections.append(self.Synapse2[i]) #adds synapse to connections list of target neuron
        
        for each_neuron in self.Output:
            temp_float = 1.0
            #print(str(x_pos) + ' ' + str(x_pos) + ' ' + str(each_neuron.value))
            for i in range(len(each_neuron.connections)):
                temp_float += 1.0
            each_neuron.value/=temp_float
            #print(str(x_pos) + ' ' + str(x_pos) + ' ' + str(each_neuron.value))

def Generate_First_AI(amount = 100, generations = 10, print_all = False):
    x_pos = random.randint(-100,100)
    y_pos = random.randint(-100,100)
    Points = {}
    for i in range(amount):
        exec("A%d = First_AI(x_pos, y_pos)" %i)
        exec("Points.update({A%d : A%d.Output})" %(i, i))
    Sorted = []
    for i in range(amount):
        xd=0
        yd=0
        #print(exec("A%d.Output[0].value" %i))
        #exec("""for each_neuron in A%d.Output:
            #print(each_neuron.value)""" %i)
        exec("xd = A%d.Output[0].value - x_pos" %i)
        exec("yd = A%d.Output[1].value - x_pos" %i)
        exec("Sorted.append([(xd*xd + yd*yd)**(1/2), A%d])" %i)
    temp_list = Generation(Sorted, Points)
    Generate(temp_list[0], temp_list[1], x_pos, y_pos, generations, print_all)
    
def Generate(AI_Children, AI_Sorted, x_pos, y_pos, generations, print_all):
    i=0
    for Synapses in AI_Children:
        #print(Synapses)
        #print(Synapses[0][2]) #- Syn1 Weight
        #print(Synapses[0][0]) #- Syn2 Connection in
        #print(Synapses[0][1]) #- Syn1 Connection out
        #for i in range(2):
            #Temp = Synapses[i][0]
            #Synapses[i][0] = Synapses[i][1]
            #Synapses[i][1] = Temp
        exec("A%d = Gen_AI(x_pos, y_pos, [], Synapses)" %i)
        i+=1

class Gen_AI:
    def __init__(self, x_pos, y_pos, Syn_Values, Synapses):
        self.Input1 = []
        self.Synapse1 = []
        self.Neuron1 = []
        self.Synapse2 = []
        self.Output = []
        self.Synapses = Synapses

        self.Input1.append(Input(x_pos)) #two neurons for directions, position of x and y
        self.Input1.append(Input(y_pos))
                
        for i in range(4): #Neuron1 (1st layer of Neurons)
            self.Neuron1.append(Neuron(0))

        temp_int_1 = Synapses[0][0]
        temp_int_2 = Synapses[0][0]
        for i in range(8): #Synapse1 (1st layer of Synapses(between In and L1))
            #Weight, Value, Connection_In, Connection_Out
            
            #print(temp_int_1)
            #print(temp_int_2)
            #print(Synapses[0])
            self.Synapse1.append(Synapse(Synapses[0][2], self.Input1[Synapses[0][0]].value, self.Input1[Synapses[0][0]], Synapses[0][1]))

            self.Neuron1[temp_int_2].value += self.Input1[Synapses[0][0]].value * self.Synapse1[i].weight
            self.Neuron1[temp_int_2].connections.append(self.Synapse1[i]) #adds synapse to connections list of target neuron

        for each_neuron in self.Neuron1:
            temp_float = 1.0
            for i in range(len(each_neuron.connections)):
                temp_float += 1.0
            each_neuron.value/=temp_float

        for i in range(2): #Output
            self.Output.append(Neuron(0))

        for i in range(8): #Synapse2 (2nd layer of Synapses(between L1 and Out))
            #Weight, Value, Connection_In, Connection_Out
            temp_int_1 = Synapses[1][0]
            temp_int_2 = Synapses[1][1]
            #print(len(Synapses))
            #print(temp_int_1)
            print(temp_int_2)
            self.Synapse2.append(Synapse(Synapses[1][2], self.Input1[Synapses[1][1]].value, Synapses[1][1], Synapses[1][0]))

            self.Output[temp_int_2].value += self.Synapse2[i].value * self.Synapse2[i].weight
            self.Output[temp_int_2].connections.append(self.Synapse2[i]) #adds synapse to connections list of target neuron
        
        for each_neuron in self.Output:
            temp_float = 1.0
            #print(str(x_pos) + ' ' + str(x_pos) + ' ' + str(each_neuron.value))
            for i in range(len(each_neuron.connections)):
                temp_float += 1.0
            each_neuron.value/=temp_float
            #print(str(x_pos) + ' ' + str(x_pos) + ' ' + str(each_neuron.value))


def Generation(Sorted, Points): #Sorts AI's and creates children, returns all Surviving + Children
    sorted(Sorted, key=lambda x: x[0], reverse=False)
    Sorted[:int((len(Sorted)/2))]
    AI_Sorted = Sorted[:]
    AI_Children = []
    while Sorted != []:
        Temporary_Int = random.randint(1, len(Sorted)-1)
        GAIs = [] #Good AIs
        RAIs = [] #Random AIs
        GAI_Synapses = []
        RAI_Synapses = []
        Surviving_AI1_Synapse1 = []
        Surviving_AI1_Synapse2 = []
        Surviving_AI2_Synapse1 = []
        Surviving_AI2_Synapse2 = []
        #AI1_1 = [number for number, AI in Points.items() if AI == Sorted[0]][0].Synapse1.weight
        #AI1_2 = [number for number, AI in Points.items() if AI == Sorted[0]][0].Synapse2.weight

        #AI2_1 = [number for number, AI in Points.items() if AI == Sorted[Temporary_Int]][0].Synapse1.weight
        #AI2_2 = [number for number, AI in Points.items() if AI == Sorted[Temporary_Int]][0].Synapse2.weight

        for Score in Sorted: #Finds best AI
            if Score == Sorted[0]:
                ListedAI = AI_Sorted[0][1]
                GAIs.append(ListedAI)
                print(ListedAI)
                break
        for Score in Sorted: #Finds random AI
            if Score == Sorted[Temporary_Int]:
                ListedAI = AI_Sorted[Temporary_Int][1]
                RAIs.append(ListedAI)
                break

        for each_syn in GAIs[0].Synapse1: #Stores all Syn1 Data from best AI
            GAI_Synapses.append([each_syn.weight, each_syn.connections[0], each_syn.connections[1]])
            Surviving_AI1_Synapse1.append([each_syn.weight, each_syn.connections[0], each_syn.connections[1]])

        for each_syn in RAIs[0].Synapse1:#Stores all Syn1 Data from random AI
            RAI_Synapses.append([each_syn.weight, each_syn.connections[0], each_syn.connections[1]])
            Surviving_AI2_Synapse1.append([each_syn.weight, each_syn.connections[0], each_syn.connections[1]])

        CHAI_Syn1 = []
        CHAI_Syn2 = []

        while GAI_Synapses != []: #Gives Children AI all Syn1 data
            for i in range(2):
                syn_from = 0
                syn_to = 0
                if random.randint(0,1):
                    syn_from = GAI_Synapses[0][1]
                else:
                    syn_from = RAI_Synapses[0][1]

                if random.randint(0,1):
                    syn_to = GAI_Synapses[0][2]
                else:
                    syn_to = RAI_Synapses[0][2]

                CHAI_Syn1.append([syn_from, syn_to, (GAI_Synapses[0][0]+RAI_Synapses[0][0])/2 + random.randint(-100,100)/1000])

            GAI_Synapses.pop()
            RAI_Synapses.pop()


        for each_syn in GAIs[0].Synapse2: #Stores all Syn2 Data from best AI
            GAI_Synapses.append([each_syn.weight, each_syn.connections[0], each_syn.connections[1]])
            Surviving_AI1_Synapse2.append([each_syn.weight, each_syn.connections[0], each_syn.connections[1]])

        for each_syn in RAIs[0].Synapse2: #Stores all Syn2 Data from random AI
            RAI_Synapses.append([each_syn.weight, each_syn.connections[0], each_syn.connections[1]])
            Surviving_AI2_Synapse2.append([each_syn.weight, each_syn.connections[0], each_syn.connections[1]])


        while GAI_Synapses != []: #Gives Children AI all Syn2 data
            for i in range(2):
                syn_from = 0
                syn_to = 0
                if random.randint(0,1):
                    syn_from = GAI_Synapses[0][1]
                else:
                    syn_from = RAI_Synapses[0][1]

                if random.randint(0,1):
                    syn_to = GAI_Synapses[0][2]
                else:
                    syn_to = RAI_Synapses[0][2]

                CHAI_Syn2.append([syn_from, syn_to, (GAI_Synapses[0][0]+RAI_Synapses[0][0])/2 + random.randint(-100,100)/1000])

            GAI_Synapses.pop()
            RAI_Synapses.pop()
        
        AI_Children.append([CHAI_Syn1[0], CHAI_Syn2[0]])
        AI_Children.append([CHAI_Syn1[1], CHAI_Syn2[1]])
        AI_Children.append([Surviving_AI1_Synapse1,
        Surviving_AI1_Synapse2])
        AI_Children.append([Surviving_AI2_Synapse1, 
        Surviving_AI2_Synapse2])
        Sorted.pop(Temporary_Int)
        Sorted.pop(0)
    return (AI_Children, AI_Sorted)

Generate_First_AI(amount=10, generations=10, print_all=True)