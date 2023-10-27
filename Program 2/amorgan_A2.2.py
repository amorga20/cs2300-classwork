import numpy as np
import math

#reads in input text linear sequence
fileTxt = "C:\\Users\\godch\\OneDrive\\Program 2\\input-A22.txt"
file = open(fileTxt, 'r')

#fill Mat1 with int number from string
Mat1 = []
for line in file:
    strings = line.split()
    for num in strings:
        num = int(num)
        Mat1.append(num)

#creates array B of zeros 
col = math.ceil(len(Mat1) / 4)
B = np.zeros((4, col), int)

#fills array B with ints from Mat1
count = 0
for j in range(col):
    for k in range(len(B)):
        if count < len(Mat1):
            B[k][j] = Mat1[count]
            count += 1

#Coding Matrix
A = np.array([[1,-1,-1,1], [2,-3,-5,4], [-2,-1,-2,2], [3,-3,-1,2]])

#Inverse Coding Matrix
Ainv = np.array([[6,-1,0,-1],[22,-4,1,-4],[14,-3,1,-2],[31,-6,2,-5]])

#Creates ciphertext matrix C
C = np.dot(A,B)

#Takes inverse coding matrix and ciphertext and multiplies them to give B plaintext
textMat = np.dot(Ainv, C)

text = []
returntext = []

#places textmat values in text list
for j in range(col):
    for k in range(len(textMat)):
            text.append(textMat[k][j])

#Goes through text list and decodes to Plaintext character, removes zeros          
for i in range(len(text)):
     character = chr(text[i])
     if character != '\x00':
        returntext.append(character)

#puts list in string and prints to console. 
returntext = ''.join(returntext)
print(returntext)