l=input().split()
m,n=int(l[0]),int(l[1])
k=input()
count=0
index=[]
for i in range(m):
    r=input().split()
    if count==0:
        for j in range(n):
            if r[j]==k:
                count=1
                index.append(i)
                index.append(j)
                break
if count==0:
    print("False")
else:
    print("True\n",index[0]," ",index[1])