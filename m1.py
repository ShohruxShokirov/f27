#ukam
def Sum(x):
    a=0
    for i in x[::-1]:
        a=a*10 + i
    print(a)
    return a
def bolish(a,b):
    x=Sum(a)+Sum(b)
    print(x)
    k=[]
    while(x):
        k.append(x%10)
        x//=10
    print(k)
    return k
l1=[5,2]
l2=[5,1]
print(bolish(l1, l2))
print(-23<-22)
#1 opp
#2 
