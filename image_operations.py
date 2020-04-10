#!/usr/bin/env python
# coding: utf-8

# In[140]:


import cv2
import numpy as np
image = cv2.imread("pic.jpeg")
img1 = cv2.resize(image,(1000,700))
img2 = img1[130:430,350:650,:]
img2 = cv2.resize(img2,(200,200))
img1[0:200,0:200,:] = img2
img1[0:200,800:1000,:] = img2
image2  = cv2.imread("pic2.jpg")
img3 = image2[10:140,200:300,:]
img3 = cv2.resize(img3,(180,220))
img3 = img3[:,:,0:1]
img1[140:360,420:600,:] = img3
cv2.imshow("mypic",img1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




