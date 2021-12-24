elves=open('elves.txt','r')


def calculator():
    me = elves.readline()
    me = me[:-1]
    A = me.split('x')
    B = []
    l=A[0]
    w=A[1]
    h=A[2]
    l=int(l)
    w=int(w)
    h=int(h)
    a1=l*w
    a2=w*h
    a3=h*l
    B.append(a1)
    B.append(a2)
    B.append(a3)
    B.sort()
    smallest=B[0]
    present=(2*a1)+(2*a2)+(2*a3)
    all = present+smallest
    # print(A,'\n',l,w,h)
    return all

# total=0
# for i in range(0,1000):
#     total+=calculator()
# print(total)

def ribbon():
    me = elves.readline()
    me = me[:-1]
    A = me.split('x')
    B = []
    l=A[0]
    w=A[1]
    h=A[2]
    l=int(l)
    w=int(w)
    h=int(h)
    B.append(l)
    B.append(w)
    B.append(h)
    print(B)
    B.sort()
    print(B)
    ribbon=B[1]*2 + B[0]*2
    ribbon=int(ribbon)
    bow=l*w*h
    all = ribbon+bow
    # all=int(all)
    # print(A,'\n',l,w,h)
    return all

total=0
for i in range(0,1000):
    total+=ribbon()
    print(i,': ',total)
print('total is: ',total)