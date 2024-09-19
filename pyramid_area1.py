cubeLength = int(input('Enter the side length in meters: '))
pyramidHeight = int(input('Enter the number of layers: '))
i = 1
sideArea = 0
while i<=pyramidHeight:
    sideArea+=i*cubeLength**2
    i+=1
sideArea*=4
j = 1
k = 1
topArea = 1
while j<pyramidHeight:
    j+=1
    topArea += (cubeLength**2)*(pyramidHeight+1)
    k+2
print(topArea+sideArea)