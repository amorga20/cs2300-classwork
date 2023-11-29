import numpy as np

def readInMat(Mat):
    file = open(Mat, "r")

    Mat1 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        Mat1.append(num)

    array = np.array(Mat1)

    file.close()
    return array

def findOutputMat(arrayD, arrayE):

    arrayI = np.identity(3)
    arrayIminD = arrayI - arrayD
    arrayIminDInv = np.linalg.inv(arrayIminD)
    outputMat = np.dot(arrayIminDInv, arrayE)
    return outputMat

MatD = "C:\\Users\\godch\\OneDrive\\Program 3\\amorgan_matD.txt"
MatE = "C:\\Users\\godch\\OneDrive\\Program 3\\amorgan_matE.txt"

arrayD = readInMat(MatD)
arrayE = readInMat(MatE)
outputMat = findOutputMat(arrayD, arrayE)
outputRnd = np.round(outputMat, decimals=1)
output = "C:\\Users\\godch\\OneDrive\\Program 3\\amorgan_output.txt"
print(outputRnd)

file = open(output, 'w')
for row in outputRnd:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()