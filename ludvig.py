n = int(input('enter n'))
l1 =tuple( int(input("enter value for l1: ")) for i in range(n) )
l2 =tuple( int(input("enter value for l2: ")) for i in range(n) )
print(l1)
print(l2)
print(sum(l1[i]*l2[i] for i in range(n)))