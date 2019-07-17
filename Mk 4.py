import random

seed = random.randint(-100000000,1000000000)
print("Current Seed:   " + str(seed))
random.seed(seed)

class NeuralNetwork:
        def __init__(self, x, hiddenCount, layerCount, weights1 = [random.randint(-150,150)/100], weights2 = [random.randint(-150,150)/100], weights = []):
                self.input =             x
                self.hiddenCount =       hiddenCount
                self.layerCount =        layerCount
                self.weights1 =          weights1
                self.middleWeights =     weights
                self.weights2 =          weights2
                self.output =            []
                self.outputNeuronCount = len(x)
                self.loss =              0

        def stepOne(self):
                if len(self.weights1) < len(self.input)*self.hiddenCount:
                        for i in range(len(self.input)*self.hiddenCount-len(self.weights1)):
                                self.weights1.append(random.randint(-150,150)/100)
                if len(self.middleWeights) < self.layerCount*self.hiddenCount:
                        for i in range((self.layerCount-1)*self.hiddenCount):
                                self.middleWeights.append(random.randint(-150,150)/100)
                self.layers = []
                for x in range(self.layerCount):
                        hiddenNode = []
                        if x == 0:
                                for y in range(len(self.input)):
                                        for i in range(self.hiddenCount):
                                                hiddenNode.append(self.input[y]*self.weights1[i])
                        else:
                                for i in range(self.hiddenCount):
                                        hiddenNode.append(self.layers[x-1][i]*self.middleWeights[x*self.hiddenCount+i-self.hiddenCount])
                        self.layers.append(hiddenNode[:])

        def lastStep(self):
                for x in range(self.outputNeuronCount):
                        a=0
                        if len(self.weights2) < self.outputNeuronCount*self.hiddenCount:
                                for i in range(self.outputNeuronCount*self.hiddenCount-len(self.weights2)):
                                        self.weights2.append(random.randint(-150,150)/100)
                                        a=1
                        tempFloat = 0.0
                        for i in range(self.hiddenCount):
                                tempFloat += self.weights2[x*self.hiddenCount+i]
                        tempFloat/=self.hiddenCount
                        self.output.append(tempFloat)
                for x in range(len(self.input)):
                        self.loss += ((self.input[x]-self.output[x])**2)**(1/2)

#x, y, hiddenCount, layerCount, weights1 = [random.randint(-150,150)/100], weights2 = [random.randint(-150,150)/100], activate = False, weights = []
def generation(AIs, scores):
        for n1 in AIs:
                n1.stepOne()
                n1.lastStep()
                scores.append(n1.loss)
        scores=sorted(scores)
        scores = scores[:int(len(scores)/2)]
        topAI = []
        #print (str(scores[0]))
        survivingAI = []
        for score in scores:
                for AI in AIs:
                        if score == AI.loss:
                                topAI.append(AI)
                                AIs.remove(AI)
                                break
        while topAI != []:
                try: tempInt = random.randint(1,(len(topAI)-1))
                except: tempInt = 0
                survivingAI.append(topAI[0])
                survivingAI.append(topAI[tempInt])
                for i in range(2):
                        weight1 = []
                        weight2 = []
                        midWeight = []
                        for weight in range(len(topAI[0].weights1)):
                                if random.randint(0,1):
                                        weight1.append((topAI[0].weights1[weight])+(random.randint(-10, 10)/100))
                                else:
                                        weight1.append((topAI[0].weights1[weight])+(random.randint(-10, 10)/100))
                        for weight in range(len(topAI[0].weights2)):
                                if random.randint(0,1):
                                        weight2.append((topAI[0].weights2[weight])+(random.randint(-10, 10)/100))
                                else:
                                        weight2.append((topAI[tempInt].weights2[weight])+(random.randint(-10, 10)/100))
                        #print(tempInt)
                        #print(len(topAI))
                        for weight in range(topAI[0].hiddenCount*(topAI[0].layerCount-1)):
                                if random.randint(0,1):
                                        midWeight.append((topAI[0].middleWeights[weight])+(random.randint(-10, 10)/100))
                                else:
                                        #print(len(topAI[tempInt].middleWeights))
                                        #print(weight)
                                        #midWeight.append((topAI[tempInt].middleWeights[weight])+(random.randint(-10, 10)/100))
                                        try: 
                                                midWeight.append((topAI[tempInt].middleWeights[weight])+(random.randint(-10, 10)/100))
                                        except: 
                                                midWeight.append((topAI[0].middleWeights[weight])+(random.randint(-10, 10)/100))
                                                #print("***************ERROR***************")
                                                #print(len(topAI[tempInt].middleWeights))
                                                #print(len(topAI[0].middleWeights))
                                                #print(weight)
                                                #print(tempInt)
                                                #print(len(topAI))
                                                #print("***********************************")
                                                #exit()
                        survivingAI.append(NeuralNetwork([random.randint(-150,150), random.randint(-150,150), random.randint(-150,150), random.randint(-150,150)], 4, 4, weight1, weight2, midWeight))
                if tempInt:
                        del topAI[tempInt]
                del topAI[0]
        return (survivingAI)

def play(generations, amount):
        AIs = []
        currentGen = 0
        scores = []
        for i in range(amount):
                AIs.append(NeuralNetwork([random.randint(-150,150), random.randint(-150,150), random.randint(-150,150), random.randint(-150,150)], 4, 2))
        AIs = generation(AIs, scores)
        while currentGen < generations:
                scores = []
                currentGen += 1
                AIs = generation(AIs, scores)
                #AIs.sort(key=lambda x: x.loss, reverse=False)
                #print(AIs[0].loss)
        #print (len(AIs))
        for n1 in AIs:
                n1.stepOne()
                n1.lastStep()
                scores.append(n1.loss)
        for AI in AIs:
                print(AI.loss)






play(100, 100)