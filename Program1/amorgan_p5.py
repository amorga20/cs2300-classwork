r = [[0 for j in range(1)] for i in range(2)]
r[0][0] = -1
r[1][0] = -2

file = open('amorgan_r.txt', 'w')
for row in r:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()

s = [[0 for j in range(1)] for i in range(2)]
s[0][0] = -3
s[1][0] = 3

file = open('amorgan_s.txt', 'w')
for row in s:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()

u = [[0 for j in range(1)] for i in range(2)]
u[0][0] = 2
u[1][0] = -1

file = open('amorgan_u.txt', 'w')
for row in u:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()

v = [[0 for j in range(1)] for i in range(2)]
v[0][0] = 3
v[1][0] = 1

file = open('amorgan_v.txt', 'w')
for row in v:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()

w = [[0 for j in range(1)] for i in range(2)]
w[0][0] = 1
w[1][0] = 3

file = open('amorgan_w.txt', 'w')
for row in w:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()

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

    for i in range(col2):
        for j in range(row2):
            vecT1[i][j] = vec2[j][i]

    num = 0
    for i in range(col):
        for k in range(row):
            num = num + vecT[i][k] * vecT1[i][k]
            dotrs = num

    return dotrs

def getFileName():

    Matrix = input('Please enter Vector to Dot: \n')
    Matrix = Matrix.lower()
    file_path = "C:\\Users\\godch\\OneDrive\\Program1\\amorgan_" + Matrix + ".txt"
    return file_path

file1 = getFileName()
file2 = getFileName()
Mat_dot = Mat_dotrs(file1, file2)

output = "amorgan_p5_out" + file1[41] + file2[41] + ".txt"

file = open(output, 'w')
file.write(str(Mat_dot))
file.write("\n")
file.close()