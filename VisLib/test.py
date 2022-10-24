from numpy import *
from matplotlib.pyplot import *
from scipy import ndimage
from PIL import Image
import cv2
from VisLib import vis

im = array(Image.open('1.png').convert('L'))
H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
im2 = ndimage.affine_transform(im, H[:2,:2],(H[0,2],H[1,2]))

vis.func(im)
vis.func(im2)




# im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)
# im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)


subplot(121)
imshow(im)
subplot(122)
imshow(im2)
show()