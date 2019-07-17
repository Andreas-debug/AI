import math
import random

random.seed(28492)

class Synapse:
    def __init__(self, weight):
        self.weight=random.random()
        self.value=0  
    def output():
        self.out = weight*value

class Neuron(Synapse):
    def __init__(self, value):
        self.value = 0
        self.connect_to = []
    def calc():
        self.value = connect_to[0].out

class AI:
    def __init__(self, Synapse, Neuron):
        #Input
        self.input_neuron = Neuron
        #1st Layer
        self.l1_neuron = Neuron
        self.l1_neuron.connect_to.append(Synapse) #(self.input.neuron.value)
        #Output
        self.out_neuron = Neuron
        self.out_neuron.connect_to.append(Synapse) #(self.l1.neuron.value)


A1 = AI(Synapse, Neuron)
A1.input_neuron.value = random.randint(1,9)
A1.l1_neuron.connect_to[0].value = A1.input.neuron.value
A1.l1_neuron.connect_to[0].output()
A1.l1_neuron.calc()
A1.out_neuron.connect_to[0].value = A1.l1.neuron.value
A1.out_neuron.connect_to[0].output()
A1.out_neuron.calc()