mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,2,3],[4,5,6],[7,8,9]]

res = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            res[i][j] = res[i][j]+mat1[i][k] * mat2[k][j]

for i in res:
        print(i)    
    