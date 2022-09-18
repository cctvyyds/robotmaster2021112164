#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np


# In[ ]:


img=cv2.imread('1.jpg')


# In[ ]:


def cv_show(name,img):
    cv2.imshow(name,img) 
    cv2.waitKey(10000) 
    cv2.destroyAllWindows()


# In[ ]:


b,g,r=cv2.split(img)


# In[ ]:


ret1, blue = cv2.threshold(b, 240, 255, cv2.THRESH_BINARY_INV)


# In[ ]:


ret2, red = cv2.threshold(r, 240, 255, cv2.THRESH_BINARY_INV)


# In[ ]:


res = cv2.add(red,blue)


# In[ ]:


image = cv2.bitwise_not(src=res)


# In[ ]:


contours, hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)


# In[ ]:


draw_img = img.copy()
cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
draw_img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
cv_show("res",draw_img)


# In[ ]:




