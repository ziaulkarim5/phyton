


#list
li=[1,2,3]
print(li)
li[1]=10
print(li)

#acces list item
ziaul = ["one","two","three","five"]
print(ziaul [1])
ziaul[2]="ob"
print(ziaul)
ziaul.append(10)
print(ziaul)
ziaul.insert(2,"gogle")
print(ziaul)
#romeve
newlist=["one","two","three","four"]
newlist.remove("one")
print(newlist)
newlist.pop(2)
print(newlist)
#for lpp list
looplist=["a","b","c"]
for y in looplist:
    print(y)
#range()lenth
for i in range(len(looplist)):
    print(i)
#while loop
y=0
while y <len(looplist):
    print(looplist)
    y=y+1
3#comprehnsiomn
num=[1,2,3,40]
double=[i*2 for i in num]
print(double)
#lis

a1list=[1,2,3,4]
print(a1list)
a1list.reverse()
print(a1list)
a1list.pop()
print(a1list)
astr=["ziaul","zia","zi"]
print(astr [0])
print(astr[-1])
print("java"in astr)
print(astr*3)
print(len(astr))
astr.append("aps")
print(astr)
astr.insert(2,"ops")
print(astr)
num=astr.copy()
print(num)
num1=list(range(9))
print(num1)
num2=list(range(5,10))
print(num2)
num3=list(range(9,13,10))
print(num3)
#looplist
sum=0

nm=[1,2,3,4,5,6,]
for x in nm:
    print(x)
    sum=sum+x
print(sum)
#2
sum=1
n=int(input("enter the lat number"))
for x in range(1,n+1,1):
    print(x)
    sum=sum*x
print(sum)






