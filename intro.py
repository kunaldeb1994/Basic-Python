import numpy as np
l=np.arange(10) #it shows a range
print(l)
print(type(l))
l2=np.zeros(5)#it shows a float
print(l2)
l3=np.ones(4,dtype='i4')
print(l3) #it shows without dot(float)
l4=np.ndarray((6,3)) #used for neural network6, it also gives the random values
print(l4)
print(l.shape)
print(l2.shape)
# l5=l4.reshape(3,3)
# print(l5)
# l5=l4.reshape(2,4)
# print(l5)
# l6=l4.reshape(2,2)
# print(l6)
l7=l4.reshape(1,-1) #negative means it doesnt take that value, it only takes positive value,
print(l7) #first 5 values are 0,if the row is made -1
l8=l4.reshape(3,2,3)
print(l8)
#linespace
A=np.linspace(10,25 ,7,endpoint=False) #only 4 no. will come at result. max point,min point and total no. of dividers is set.
print(A)

start=10
end=25
step=7
a=(end-start)/step
print(a)
t=start
while (t<25):
    print(t)
    t+=a
A1=np.ones(5,dtype=int)
print(A1)
A2=np.ones((2,2), dtype=int)
print(A2)

S=np.arange(18).reshape(2,9)
S1=np.arange(18).reshape(2,9,1)
S2=np.arange(18).reshape(3,3,2)
print(S)
print(S1)
print(S2)