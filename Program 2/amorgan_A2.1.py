import numpy as np
import math 

#reads in input file
fileTxt = "C:\\Users\\godch\\OneDrive\\Program 2\\input-A21.txt"
file = open(fileTxt, 'r')

#creates matrix list
Mat1 = []

#reads in file and removes enter.
for line in file:
    strings = line.split('\n')

#grabs first string
strings = strings[0]

#goes through string and cast each character to decimal and appends it to Mat1
for char in strings:
    num = ord(char)
    Mat1.append(num)

#determines the amount of columns needed for B matrix, rounds up so last spots are zeros
col = math.ceil(len(Mat1) / 4)

#creates an int array of 4xN full of zeros. 
B = np.zeros((4, col), int)

#counter to keep track of Mat1 and prevent out of bound error
count = 0

#fills the B array with values in Mat1
for j in range(col):
    for k in range(len(B)):
        if count < len(Mat1):
            B[k][j] = int(Mat1[count])
            count += 1

output = "amorgan_A2.1_out_B.txt"

#prints the output of plaintext matrix B
file = open(output, 'w')
for row in B:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()

#Coding Matrix
A = np.array([[1,-1,-1,1], [2,-3,-5,4], [-2,-1,-2,2], [3,-3,-1,2]])

#Inverse Coding Matrix
Ainv = np.array([[6,-1,0,-1],[22,-4,1,-4],[14,-3,1,-2],[31,-6,2,-5]])

#Cipher text
C = np.dot(A,B)

output = "amorgan_A2.1_out_C.txt"

#prints the output of ciphertext matrix C
file = open(output, 'w')
for row in C:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()