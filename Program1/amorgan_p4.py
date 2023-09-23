import numpy as np

def Mat_add12(file1, file2):

    file = open(file1, "r")

    Mat1 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        Mat1.append(num)

    array1 = np.array(Mat1)

    file.close()
    file = open(file2, "r")

    Mat2 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        Mat2.append(num)

    array2 = np.array(Mat2)

    file.close()

    add_array = array1 + array2 
    return add_array

def Mat_mult12(file1, file2):

    file = open(file1, "r")

    Mat1 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        Mat1.append(num)

    array1 = np.array(Mat1)

    file.close()
    file = open(file2, "r")

    Mat2 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        Mat2.append(num)

    array2 = np.array(Mat2)

    file.close()

    mult_arr = np.dot(array1,array2)
    return mult_arr

def getFileName(Matrix):

    Matrix = Matrix.lower()
    file_path = "C:\\Users\\godch\\OneDrive\\Program1\\amorgan_" + Matrix + ".txt"
    return file_path

def add_array(Matrix1, Matrix2):
    file1 = getFileName(Matrix1)
    file2 = getFileName(Matrix2)
    Mat_add = Mat_add12(file1, file2)

    output = "amorgan_p4_out" +"A" +file1[44] + file2[44] + ".txt"

    file = open(output, 'w')
    for row in Mat_add:
        file.write(' '.join(map(str, row)))
        file.write("\n")
    file.close()

def mult_array(Matrix1, Matrix2):
        file1 = getFileName(Matrix1)
        file2 = getFileName(Matrix2)
        Mat_mult = Mat_mult12(file1, file2)

        output = "amorgan_p4_out" +"M" +file1[44] + file2[44] + ".txt"

        file = open(output, 'w')
        for row in Mat_mult:
            file.write(' '.join(map(str, row)))
            file.write("\n")
        file.close()

add_array('mat1', 'mat2')
add_array('mat2', 'mat1')
mult_array('mat1', 'mat2')
mult_array('mat2', 'mat1')
mult_array('mat3', 'mat4')
mult_array('mat4', 'mat3')
