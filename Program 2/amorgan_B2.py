import sympy as sp

#takes input for flow values
flow1 = int(input('Please enter Flow 1 value: \n'))
flow2 = int(input('Please enter Flow 2 value: \n'))
flow3 = int(input('Please enter Flow 3 value: \n'))
flow4 = int(input('Please enter Flow 4 value: \n'))

#creates augmented array using flow values
array1 = sp.Matrix([[1,0,0,-1,flow4],[1,-1,0,0,flow3],[0,-1,1,0,flow2],[0,0,1,-1,flow1]])
print(array1)

#solve gauss exhation and returns matrix
array1_rref = array1.rref()
print(array1_rref)