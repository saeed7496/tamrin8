
import os
import imageio
myfile=os.listdir('test')
images=[]
print(myfile)
for i in range(len(myfile)):
    image=imageio.imread(myfile[i])
    images.append(image)
imageio.mimsave('saeed.gif',images)





