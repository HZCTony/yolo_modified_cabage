
# coding: utf-8

# In[7]:


import sys
import os
import argparse
from yolomod import YOLO, detect_video
from PIL import Image


# In[8]:


IN_DIR = './cabage_renew/jpg/'
OUT_DIR = './cabage_renew/infer/'

imagelist = []
imagefiles = os.listdir(IN_DIR)
imagefiles.sort()

for i in imagefiles:
    if (os.path.isdir(IN_DIR + '/')):
#         print (i)
        if (i[0] == '.' or not i[-1] == 'g'):
            pass
        else:
            imagelist.append(i)

print ('Length of crop train-val dir: ' + str(len(imagelist)))


# In[9]:


def detect_img(yolo, IN_DIR, OUT_DIR, imagelist):
    for num in range(len(imagelist)):
        img = IN_DIR + imagelist[num]
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
#             r_image.show()
            r_image.save(OUT_DIR + imagelist[num])
    yolo.close_session()


# In[12]:


detect_img(YOLO(image=True, input=None, output=''), IN_DIR, OUT_DIR, imagelist)

