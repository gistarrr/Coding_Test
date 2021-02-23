N = int(input())

count = 0
for i in range(N):
    word = input()
    flag = 0
    for j in word:
        if word.count(j)>=2 and word.rfind(j)-word.find(j)+1 != word.count(j):
            flag = 1
            break
    if flag == 0 :
        count+=1                
print(count)


#result = 0
#for i in range(int(input())):
#    word = input()    
#    if list(word) == sorted(word, key=word.find):
#        result += 1
#print(result)