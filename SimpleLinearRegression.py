#This file contains code to predict output for  linear regression with one input parameter
#Closed-form solution is implemented here
#every function is implemented from scratch

X_datapoints = [0, 1, 2, 3, 4]
Y_datapoints = [1, 3, 7, 13, 21]

def getIntercept(X_datapoints,Y_datapoints):

    return getMean(Y_datapoints) - getSlope(X_datapoints,Y_datapoints) * getMean(X_datapoints)

def getMean(X_datapoints):

    sum = 0
    for i in range(0,len(X_datapoints)):
        sum += X_datapoints[i]

    return sum / len(X_datapoints)


def getSlope(X_datapoints,Y_datapoints):
    XY_datapoints = []
    XSquare_datapoints = [x * x for x in X_datapoints]

    for i in range(0,len(X_datapoints)):
        XY_datapoints.append(X_datapoints[i]*Y_datapoints[i])

    Mean_X = getMean(X_datapoints)
    Mean_Y = getMean(Y_datapoints)
    Mean_XY = getMean(XY_datapoints)
    Mean_XSquare = getMean(XSquare_datapoints)


    Numerator = Mean_XY - (Mean_X * Mean_Y)
    Denominator = Mean_XSquare - (Mean_X * Mean_X)

    return Numerator/Denominator

def getEstimatedOutput(x_value):

    y_value = getSlope(X_datapoints,Y_datapoints) * x_value + getIntercept(X_datapoints,Y_datapoints)
    return y_value

#print getSlope(X_datapoints,Y_datapoints)
#print getIntercept(X_datapoints,Y_datapoints)

#Give the required input x value here
#getEstimatedOutput(input_value)
