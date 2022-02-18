def tri(a,b,c):
    if (a+b+c) % 4 == 0:
        return ("L: "+str(int((a+b+c)/4)) + "A: " + str(int(((a+b+c)/4)**2)))
    else:
        return -1
n=int(input())
for i in range(n):
    x,y,z=int(input())
    print(tri(x,y,z))
