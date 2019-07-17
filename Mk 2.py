# -*- coding:latin-1 -*-

import random
import math


seed = 56879075098234
random.seed(seed)

class Neuron: #takes in its value, can be from synapse, other Neuron, or random number
    def __init__(self, value):
        self.value = value

class Synapse: #takes in its value and weight, can be from Neuron, other synapse, or random number
    def __init__(self, weight,value):
        self.weight = weight
        self.value = value

class AI: #Needs 2 Neurons and One Synapse to operate
    def __init__(self, Input, Synapse1, Output):
        self.Input = Input
        self.Synapse1 = Synapse1
        self.Output = Output

def Generate_First(amount = 100, generations = 10, print_all = False): #Generates 100 "Random" AI
    correct_numb = random.randint(1,10)
    Points = {}
    for i in range(amount):
        In = Neuron(correct_numb)
        Syn = Synapse(math.floor(random.randint(-100,100))/10, In.value)
        Out = Neuron(Syn.value*Syn.weight)
        exec("A%d = AI(In, Syn, Out)" %i)
        exec("Points.update({A%d : A%d.Output.value})" %(i, i))
    if print_all:
        for i in range(generations-1):
            Points = Children(Generate_Children(Points, correct_numb, True), correct_numb)
    else:
        for i in range(generations-1):
            Points = Children(Generate_Children(Points, correct_numb, False), correct_numb)
    Points = Children(Generate_Children(Points, correct_numb, True), correct_numb)
    

def Generate_Children(Points, correct_numb, Print_Best):
    Values = []
    Old_Values = []
    for value in Points.values():
        Old_Values.append(value)
    for value in range(len(Old_Values)):
        Values.append(min(Old_Values, key=lambda x:abs(x-correct_numb)))
        Old_Values.remove(min(Old_Values, key=lambda x:abs(x-correct_numb)))
    #print(Values)
    #print(Old_Values)
    Values = Values[:50]
    AI_children = []
    Top_AI_This_Gen = [number for number, AI in Points.items() if AI == Values[0]][0]
    if Print_Best == True:
        print(str(Top_AI_This_Gen.Synapse1.weight) + "\n" + str(Top_AI_This_Gen.Output.value))
    while Values != []:
        Temporary_Int = random.randint(0, len(Values)-1)
        AI1 = [number for number, AI in Points.items() if AI == Values[0]][0].Synapse1.weight
        AI2 = [number for number, AI in Points.items() if AI == Values[Temporary_Int]][0].Synapse1.weight
        CH1 = (AI1+AI2)/2 + random.randint(-100,100)/1000
        CH2 = (AI1+AI2)/2 + random.randint(-100,100)/1000
        CH3 = (AI1+AI2)/2 + random.randint(-100,100)/1000
        CH4 = (AI1+AI2)/2 + random.randint(-100,100)/1000
        AI_children +=CH1, CH2, CH3, CH4
        Values.pop(Temporary_Int)
        Values.pop(0)
    #print (AI_children)
    return AI_children

def Children(AI_children, correct_numb):
    Points = {}
    for i in range(len(AI_children)):
        In = Neuron(correct_numb)
        Syn = Synapse(AI_children[i], In.value)
        Out = Neuron(Syn.value*Syn.weight)
        exec("A%d = AI(In, Syn, Out)" %i)
        exec("Points.update({A%d : A%d.Output.value})" %(i, i))
    return Points
    #Generate_Children(Points,correct_numb, False)

Generate_First(20, 10, True)