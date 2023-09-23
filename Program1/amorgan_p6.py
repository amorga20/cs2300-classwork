def transVect(file):

    file = open(file, "r")

    vec1 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        vec1.append(num)

    file.close()

    row = len(vec1)
    col = len(vec1[0])

    vecT = [[0 for j in range(row)] for i in range(col)]

    for i in range(col):
        for j in range(row):
            vecT[i][j] = vec1[j][i]

    return vecT

def getFileName():

    Matrix = input('Please enter Vector to Transpose: \n')
    Matrix = Matrix.lower()
    file_path = "C:\\Users\\godch\\OneDrive\\Program1\\amorgan_" + Matrix + ".txt"
    return file_path

file1 = getFileName()
transposed = transVect(file1)

output = "amorgan_p6_mat5.txt"

file = open(output, 'w')
for row in transposed:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()