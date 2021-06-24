import cv2
import random
import string
from datetime import datetime
random.seed(datetime.now())

def random_name():
    name = ""
    for x in range(15):
        name = name+random.choice(string.ascii_letters + string.digits)
    #print (name)
    return name

h=720
w=1280
y=150
x=60

vidcap = cv2.VideoCapture('videoplayback.mp4')
length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
half = length/2.0
target_number = 300
probability = target_number/half

print('Total number of frames: ', length )
print('Target number of frames: ', target_number )
print('Probability: ', probability )
print(random.random())
print(random.random())

success,image = vidcap.read()
count = 0
min_count = 30*10
n_count = 0
while (success and count < half):
    chance = random.random()
    new_image=image[y:y+h,x:x+w]
    
    if(chance <= probability and count > min_count):
        n_count+=1
        print(str(count)+" "+str(n_count)+" "+str(chance)+" "+str(probability)+"!!!")
        #cv2.imwrite("frames/"+random_name()+".jpg", new_image)     # save frame as JPEG file
        cv2.imwrite("frames/"+random_name()+".jpg", image)     # save frame as JPEG file      
    else:
        print(str(count)+" "+str(n_count)+" "+str(chance)+" "+str(probability))
              
    success,image = vidcap.read()  
    count += 1

print('Finished all! ')
