l = []
k=[]
n= int(input("Enter the number of elements you want to input : "))
for i in range(n):
    X=int(input())
    l.append(X)
for j in l:
    if j>0:
        k.append(j)

    #if j <0:
    #   del l[l.index(j)]

print(k)
