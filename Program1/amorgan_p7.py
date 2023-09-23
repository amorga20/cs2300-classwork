import numpy as np

def Mat_dotrs(file1, file2):

    file = open(file1, "r")

    vec1 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        vec1.append(num)

    file.close()
    file = open(file2, "r")

    vec2 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        vec2.append(num)

    file.close()

    row = len(vec1)
    col = len(vec1[0])

    row2 = len(vec2)
    col2 = len(vec2[0])

    vecT = [[0 for j in range(row2)] for i in range(col2)]
    vecT1 = [[0 for j in range(row2)] for i in range(col2)]

    for i in range(col):
        for j in range(row):
            vecT[i][j] = vec1[j][i]

    dotrs = np.dot(vecT, vec2)

    return dotrs

def transVect(file):

    file = open(file, "r")

    vec1 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        vec1.append(num)

    file.close()

    trans = np.transpose(vec1)

    return trans

def transpose(file1):
    file = getFileName(file1)
    transposed = transVect(file)

    output = "amorgan_p7_outT" + str(file1) + ".txt"

    file = open(output, 'w')
    for row in transposed:
        file.write(' '.join(map(str, row)))
        file.write("\n")
    file.close()

def getFileName(Matrix):

    Matrix = Matrix.lower()
    file_path = "C:\\Users\\godch\\OneDrive\\Program1\\amorgan_" + Matrix + ".txt"
    return file_path

def dotrs(vect1, vect2):
    file1 = getFileName(vect1)
    file2 = getFileName(vect2)
    Mat_dot = Mat_dotrs(file1, file2)

    output = "amorgan_p7_out" + "D" + file1[41]   + file2[41] + ".txt"

    file = open(output, 'w')
    file.write(str(Mat_dot))
    file.write("\n")
    file.close()

dotrs('r','s')
dotrs('r','u')
dotrs('r','v')
dotrs('r','w')
dotrs('s','u')
dotrs('s','v')
dotrs('s','w')
dotrs('u','v')
dotrs('u','w')
dotrs('v','w')
transpose('r')
transpose('s')
transpose('u')
transpose('v')
transpose('w')