import numpy as np
import matplotlib.pyplot as mp

def readInFile(pair):

    file = open(pair, "r")

    Mat1 = []
    for line in file:
        a,b = line.strip('()').split(',')
        b = b.strip('\n')
        b = b.strip(')')
        Mat1.append((int(a),int(b)))

    file.close()
    return Mat1

ordered_pairs = "C:\\Users\\godch\\OneDrive\\Program 3\\amorgan_orderedPair.txt"

Mat = readInFile(ordered_pairs)

arrayX = np.ones((len(Mat),2), int)
arrayY = np.zeros((1,len(Mat)), int)
arrayY = np.transpose(arrayY)
x_list = []
for i in range(len(Mat)):
    xy = Mat[i]
    x = xy[0]
    x_list.append(x)
    y = xy[1]
    arrayX[i][1] = x
    arrayY[i] = y
    mp.scatter(x, y, color='blue')

arrayXT = np.transpose(arrayX)
xTx = np.dot(arrayXT, arrayX)
xTy = np.dot(arrayXT,arrayY)
xTxInv = np.linalg.inv(xTx)
a = np.dot(xTxInv, xTy)
a = np.round(a, decimals=1)

linEq = 'y = ' + str(a[1]) + 'x + ' + str(a[0])
print(linEq)
output = "C:\\Users\\godch\\OneDrive\\Program 3\\amorgan_linearEqoutput.txt"
file = open(output, 'w')
file.write(linEq)
file.close()

x = np.linspace(min(x_list), max(x_list), 75)
y = a[1] * x + a[0]
mp.plot(x,y,color="black")

mp.xlabel('Price')
mp.ylabel('Sales')
mp.grid(True)
mp.show()