def Mat_mult12(file1, file2):

    file = open(file1, "r")

    Mat1 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        Mat1.append(num)

    file.close()
    file = open(file2, "r")

    Mat2 = []
    for line in file:
        strings = line.split()
        num = [float(i) for i in strings]
        Mat2.append(num)

    file.close()

    row = len(Mat1)
    col = len(Mat1[0])

    row2 = len(Mat2)
    col2 = len(Mat2[0])

    if col != row2:
        print("Can't preform multiplication")
    else:

        Mat12 = [[0 for j in range(col2)] for i in range(row)]

        Mat3 = [[0 for j in range(row2)] for i in range(col2)]

        for i in range(col2):
            for j in range(row2):
                Mat3[i][j] = Mat2[j][i]

        num = 0
        for i in range(row):
            for j in range(col2):
                arr = Mat1[i]
                arr2 = Mat3[j]
                for k in range(len(arr)):
                    num = num + arr[k] * arr2[k]
                Mat12[i][j] = num
                num = 0

        return Mat12

def getFileName():

    Matrix = input('Please enter Matrix to Multiply: \n')
    Matrix = Matrix.lower()
    file_path = "C:\\Users\\godch\\OneDrive\\Program1\\amorgan_" + Matrix + ".txt"
    return file_path

file1 = getFileName()
file2 = getFileName()
Mat_mult = Mat_mult12(file1, file2)

output = "amorgan_p3_out" + file1[44] + file2[44] + ".txt"

file = open(output, 'w')
for row in Mat_mult:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()