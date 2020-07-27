import random
from matplotlib import pyplot as plt
n=20
ring=[]
ring.append([0,200])
ring.append([200,0])
for i in range(n-2):
  x=random.randrange(1,201,1)
  y=200-x
  ring.append([x,y])
first=[]
print("List of bowls and their respective number of white and black balls before")
print("")
print(ring)
print("")
for i in range(2,20):
  first.append(ring[i][0]/ring[i][1])
for i in range(200):
  z=i%n
  c=random.randrange(0,2,1)
  ring[(z+1)%n][c]+=1
  ring[z][c]-=1
second=[]
print("List of bowls and their respective number of white and black balls after process")
print("")
print(ring)
print("")
for i in range(2,20):
  second.append(ring[i][0]/ring[i][1])
fig=plt.figure()
x=[i for i in range(2,20)]
plt.plot(x,first,label="first")
plt.plot(x,second,label="second")
plt.legend()
plt.show()
fig.savefig('plot.png')
