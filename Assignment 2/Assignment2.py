import matplotlib.pyplot as plt
import numpy as np
#Part A
dimensions=(4,100)
X = np.zeros(dimensions)
#print(X)            

#Create i.i.d. Random Variables for height and weight
mu,mu1,sigma,sigma1 = 165, 137, 25,100
height = sigma * np.random.randn(1, 100) + mu
X[0,] = height
weight = sigma1 * np.random.randn(1,100) + mu1
X[1,] = weight
#print(X)

x=np.arange(1,101)
plt.scatter(x,X[0,],c='blue',label="height")
plt.scatter(x,X[1,],c='red',label="weight")
plt.xlabel("Sample Number")
plt.ylabel("Value")
plt.legend()
#plt.show()
plt.clf()
#Computes the ratio of weight:height from the first row (Weight) to the Second Row (height)
holdValues = np.zeros(dimensions)
np.divide(X[1,:],X[0,:],holdValues[0,:])
plt.hist(holdValues[0,],10)
plt.title("Histogram of Weight:Height")
plt.xlabel("Ratio")
plt.ylabel("Number of Samples")
#plt.show()
plt.clf()

#Glucose level
glucosemu,glucosesigma = 0, 1
#Add the noise values
holdValues[1,] = glucosesigma * np.random.randn(1,100) + glucosemu
#Store the noise in row 2 of holdValues
np.add(holdValues[0,].T,holdValues[1,].T,X[2,])
#print(X[2,])
#If Healthy = 0, Diabetic = 1, we will make a threshold of 0
#If the glucose is over 0, Diabetic
for i in range (0,100):
    if X[2,i] > 0:
        #diabetic
        X[3,i] = 1
    else:
        #Healthy
        X[3,i]=0



#Visualize/Plot the Data for Different Values of sigma and threshold, Row 1 will be sigma, Row 2 will be threshold
DiffValues= np.random.randn(2, 4)
#for loop in range(0,5):
for loop in range(0,4):
    #Glucose level
    glucosemu,glucosesigma = 0, DiffValues[0,loop]
    #Add the noise , store the noise in row 2 of holdValues
    holdValues[1,] = glucosesigma * np.random.randn(1,100) + glucosemu
    #Store the glucose level in row 3 of MatrixX
    np.add(holdValues[0,].T,holdValues[1,].T,X[2,])

    thresholdval = DiffValues[1,loop]

    #If Healthy = 0, Diabetic = 1, we will make a threshold of 0
    #If the glucose is over 0, Diabetic
    for i in range (0,100):
        if X[2,i] > thresholdval :
            #diabetic
            X[3,i] = 1
        else:
            #Healthy
            X[3,i]=0
    
    x=np.arange(1,101)
    plt.scatter(x,X[2,],c='green',label="Glucose at Noise Sigma"+ str(glucosesigma))
    plt.scatter(x,X[3,], c='red',label="Healthy/Diabetic at threshold" + str(thresholdval))
    plt.xlabel("Sample Number")
    plt.ylabel("Value")
    plt.legend()
    plt.show()
    plt.clf()
    





