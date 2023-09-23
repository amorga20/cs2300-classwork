def Mat_add12(file1, file2):

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

    if row != row2:
        print("Can't preform addition")
    elif col != col2:
        print("Can't preform addition")
    else:

        Mat12 = [[0 for j in range(col)] for i in range(row)]

        for i in range(row):
            for j in range(col):
                num = Mat1[i][j] + Mat2[i][j]
                Mat12[i][j] = num

        return Mat12

def getFileName():

    Matrix = input('Please enter Matrix to Add: \n')
    Matrix = Matrix.lower()
    file_path = "C:\\Users\\godch\\OneDrive\\Program1\\amorgan_" + Matrix + ".txt"
    return file_path

file1 = getFileName()
file2 = getFileName()
Mat_add = Mat_add12(file1, file2)

output = "amorgan_p2_out" + file1[44] + file2[44] + ".txt"

file = open(output, 'w')
for row in Mat_add:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()