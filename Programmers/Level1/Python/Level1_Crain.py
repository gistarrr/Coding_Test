board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
crain = []
count = 0
for i in moves:
    flag = 0
    for j in board:        
        if j[i-1]!=0 and flag == 0:
            if len(crain)>=1 and crain[-1]==j[i-1]:
                count+=1
                del crain[-1]
                j[i-1]=0
                flag = 1
            else :
                crain.append(j[i-1])
                j[i-1]=0
                flag = 1
count*=2             
