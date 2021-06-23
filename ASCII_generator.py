from PIL import Image
import numpy as np
import math


with Image.open("ascii-pineapple.jpg") as im:
    (width, height) = (im.width//2, im.height//2)
    im_resized = im.resize((width, height))

print(im.format, im.size, im.mode)

imArray = np.array(im)

#brightnessArray = np.zeros((len(imArray), len(imArray[0])))
brightnessArray = []
print(imArray.shape)
#print(brightnessArray.shape)

ascii_char = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # 65 chars
len_ascii_char = len(ascii_char)

for x in range(len(imArray)):
    innerlist = []
    for y in range(len(imArray[0])):
        color = (imArray[x][y][0] + imArray[x][y][1] + imArray[x][y][2]) / 3
        colorscaled = color / 255
        innerlist.append(ascii_char[math.floor(len_ascii_char * colorscaled)])    
    brightnessArray.append(innerlist)





#print(brightnessArray)
# print(imArray[5][5])
#arr2im = Image.fromarray(im2arr)