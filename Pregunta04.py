n =[[1, 11, -5, 3],[3, 22, -2, 4],[5, 10, -6, 8],[9, 16, -1, 3]]

for i in range (0,2):
    if n[i+1][i+1] > n[i][i]:
        y = n[i+1][i+1]
        
print(y)