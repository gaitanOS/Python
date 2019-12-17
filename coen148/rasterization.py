from PIL import Image

radius = 100 #radius of circle
quadrantx = [0,]
d = (5/4) - radius
x = 0
y = radius

xpts = [] #array to hold x pts
ypts = [] #array to hold y pts
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
print("arrays filled\n")

img = Image.new('RGB', (320, 240))

pixels = img.load()


for i in range(len(xpts)):
    pixels[xpts[i],ypts[i]] = (255,0,0)
    
img.show()
        
    




