from numpy import *
from matplotlib.pyplot import *
from scipy import ndimage
from PIL import Image
import cv2
from VisLib import vis

im1 = Image.open('1.png')
im = array(im1.convert('L'))
H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
im2 = ndimage.affine_transform(im, H[:2,:2],(H[0,2],H[1,2]))

im3 = Image.open('2.png')
H = array([[2,0.05,-100],[0.03,1.5,-100],[0,0,2]])

im = array(im3.convert('L'))
im4 = ndimage.affine_transform(im, H[:2,:2],(H[0,2],H[1,2]))
# vis.showimg(im1)
# vis.showimg(im1,title = '12')

# vis.showimgs(im1,im2,im1,im2)
titles = ['cat1','cat2','dog','dog2']
# rectss.addRect(0,[67,40],147,14)
rect1 = vis.MakeRect([67,40],147,14)
rect2 = vis.MakeRect([87,130],93,18,edgecolor = 'w')
rect3 = vis.MakeRect([56,63],189,188,edgecolor = 'g',linewidth = 3)
rect4 = vis.MakeRect([120,27],66,55,edgecolor = 'cyan',linewidth = 1)
rect5 = vis.MakeRect([62,49],152,114,edgecolor = 'm',linewidth = 5)
rects1 = []
rects1.append(rect1)
rects1.append(rect2)
rects2 = []
rects2.append(rect3)
rects3 = []
rects3.append(rect4)
rects4 = []
rects4.append(rect5)
rectss=[]
rectss.append(rects1)
rectss.append(rects2)
rectss.append(rects3)
rectss.append(rects4)
# print(rectss)

rects = vis.Rects()
rects.addRect(0,[67,40],147,14)
rects.addRect(0,[87,130],93,18,edgecolor = 'w')
rects.addRect(1,[56,63],189,188,edgecolor = 'g',linewidth = 3)
rects.addRect(2,[120,27],66,55,edgecolor = 'cyan',linewidth = 1)
rects.addRect(3,[62,49],152,114,edgecolor = 'm',linewidth = 5)

# vis.showimgs(im1,im2,im1,im2, title = titles)
vis.showimgs(im1,im2,im3,im4, title = titles, rect = rects)


titles2 = titles + titles + titles + titles
# titles3 = titles2+titles2+titles2+titles2+titles2+titles2+titles2+titles2+titles2+titles2
# vis.showimgs(im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4, title = titles3)

# vis.showimgs(im1,im2,im2,im2)

# vis.showimg(im1)
# vis.showimg(im1,title = 'cat')

# vis.showimgs(im1,im2,im3,im4, title = titles)




im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)


# subplot(121)
# imshow(im)
# subplot(122)
# imshow(im2)
# show()

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rect = plt.Rectangle((67,40),147,14,fill=False, edgecolor = 'red',linewidth=1)
ax.add_patch(rect)
plt.imshow(im1) # 图像数组
plt.show()
