
#author:shiaihua
#date: 2020-09-08

ageNum = 9
# num_array5 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# num_array6 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
# num_array = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

num_array = []
for i in range(ageNum):
    num_array.append([0] * ageNum)

lastNum =0;
lastAge =0;
count =  0;
for i in range(ageNum, 1, -2):
    count = count +1
    for a1 in range(0,i):
        lastNum = lastNum + 1
        cc = count -1
        cl = count -1+ a1
        num_array[cc][cl] = lastNum

    for a2 in range(0,i-1):
        lastNum = lastNum + 1
        cc = count + a2
        cl = ageNum-count
        num_array[cc][cl] = lastNum

    for a3 in range(1,i):
        lastNum = lastNum + 1
        cc = ageNum -count
        cl = ageNum - count - a3
        num_array[cc][cl] = lastNum

    for a4 in range(1,i-1):
        lastNum = lastNum + 1
        tmpRow = ageNum - count
        num_array[ageNum-count-a4][count-1] = lastNum
    print(i)
    lastAge = i;

if (i==3):
    i =  i-2
    count  = count + 1
    lastAge = i;
    lastNum = lastNum + 1
    cc = ageNum - count
    cl = ageNum - count
    num_array[cc][cl] = lastNum

print(i)
print(num_array);





#
# [[1, 2, 3, 4, 5],
# [16, 17, 18, 19, 6],
# [15, 24, 25, 20, 7],
# [14, 23, 22, 21, 8],
# [13, 12, 11, 10, 9]]
#
#
#
# [[1, 2, 3, 4, 5, 6],
# [20, 21, 22, 23, 24, 7],
# [19, 32, 33, 34, 25, 8],
# [18, 31, 36, 35, 26, 9],
# [17, 30, 29, 28, 27, 10],
# [16, 15, 14, 13, 12, 11]]
#
#
#
#
# [[1,  2,  3,  4,  5,  6, 7],
# [24, 25, 26, 27, 28, 29, 8],
# [23, 40, 41, 42, 43, 30, 9],
# [22, 39, 48, 49, 44, 31, 10],
# [21, 38, 47, 46, 45, 32, 11],
# [20, 37, 36, 35, 34, 33, 12],
# [19, 18, 17, 16, 15, 14, 13]]