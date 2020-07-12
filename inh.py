a1 = [1,2,3]
a2 = [4,5,6]
a3 = [4,5,6]


a1sv = 2
a2sv = 1
a3sv = 1000

temp2D = [[a1,a1sv],[a2,a2sv],[a3,a3sv]]

a3D = sorted(temp2D,key=lambda l:l[1])


a2D = [x for x,y in a3D]
print(a2D)