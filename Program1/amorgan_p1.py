Aubrey = 6
Morgan = 6

Mat1 = [[0 for j in range(Aubrey)] for i in range(Morgan)]

num = 1

for i in range(Morgan): 
    for j in range(Aubrey):
        Mat1[i][j] = num
        num += 1

file = open('amorgan_mat1.txt', 'w')
for row in Mat1:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()

Mat2 = [[0 for j in range(Aubrey)] for i in range(Morgan)]

num = 2

for i in range(Morgan):
    for j in range(Aubrey):
        Mat2[j][i] = num
        num += 3

file = open('amorgan_mat2.txt', 'w')
for row in Mat2:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()

rows = 2
columns = 4

Mat3 = [[0 for j in range(columns)] for i in range(rows)]
num = 10
for i in range(rows):
    for j in range(columns):
        Mat3[i][j] = num
        num -= 2

file = open('amorgan_mat3.txt', 'w')
for row in Mat3:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()

rows = 4
columns = 2

Mat4 = [[0 for j in range(columns)] for i in range(rows)]
num = -6
for i in range(columns):
    for j in range(rows):
        Mat4[j][i] = num
        num = num * 1.5

file = open('amorgan_mat4.txt', 'w')
for row in Mat4:
    file.write(' '.join(map(str, row)))
    file.write("\n")
file.close()