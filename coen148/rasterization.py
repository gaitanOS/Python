from PIL import Image

radius = 100 #radius of circle
quadrantx = 0
quadranty = radius
xpts = [] #array to hold x pts
ypts = [] #array to hold y pts
img = Image.new('RGB', (1000, 1000))
pixels = img.load()
d = (5/4) - radius
x = 0
y = radius
xpts.append(x) #initial x value
ypts.append(y) #initial y value

while x < y:
    if d < 0:
        d += (2*x + 3)
        x += 1
        xpts.append(x)
        ypts.append(y)
    else:
        d += (2 * (x - y) + 5)
        x += 1
        y -= 1
        xpts.append(x)
        ypts.append(y)
#print("arrays filled by round " + str(i) + "\n")


for i in range(len(xpts)):
    print("printing point: " + "(" + str(xpts[i]) + ", " + str(ypts[i])+ ")\n")
    pixels[xpts[i] + 500 ,ypts[i] - 500] = (255,255,0)
for i in range(len(xpts)):
    print("printing reflection pts\n")
    pixels[-xpts[i]+ 500,ypts[i]- 500] = (255,255,0)
    pixels[xpts[i] + 500,-ypts[i] - 500] = (255,255,0)
    pixels[-xpts[i] + 500 ,-ypts[i] - 500] = (255,255,0)
    pixels[ypts[i] + 500 ,xpts[i] - 500] = (255,255,0)
    pixels[-ypts[i] + 500,xpts[i] - 500] = (255,255,0)
    pixels[ypts[i] + 500,-xpts[i] - 500] = (255,255,0)
    pixels[-ypts[i] + 500 ,-xpts[i] - 500] = (255,255,0)
        
img.show()
        
    




