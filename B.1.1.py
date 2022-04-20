l=input().split()
m,n=int(l[0]),int(l[1])
k=input() #getting k as a string
count=0
index=[]
for i in range(m):
    r=input().split() #input rows one by one
    if count==0: #if k is not found yet, then we search for it
        for j in range(n):
            if r[j]==k: #if k is found in the added row
                count=1 
                index.append(i) #update index with position of k, we dont have to check for k from the next row.
                index.append(j)
                break
if count==0:
    print("False")
else:
    print("True\n",index[0]," ",index[1])
