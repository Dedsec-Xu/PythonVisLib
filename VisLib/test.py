from numpy import *
from matplotlib.pyplot import *
from scipy import ndimage
from PIL import Image
import cv2

from VisLib import vis


# Basic Demo

def demo1():
    im1 = Image.open('1.png')
    c = vis.showimg(im1)
    # c = vis.showimg(im1,title = "cat")


# Basic Demo End

# Basic Demo2

def demo2():
    im1 = Image.open('1.png')
    im = array(im1.convert('L'))
    H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
    im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))
    c1 = vis.showimgs(im1, im2)
    # c1 = vis.showimgs(im1,im2,title = ["cat","affine transformed cat"])


# Basic Demo2 End


# Iterative Demo

def demo3():
    im1 = Image.open('1.png')
    im = array(im1.convert('L'))
    H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
    im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))

    c2 = vis.showimgs(open=False)

    for i in range(100):
        c2.addImg(im1)
    #
    # for i in range(100):
    #     c2.addImg(im1,im2)

    # for i in range(100):
    #     c2.addImg(im1,im2,title = ["cat " + str(i+1), "affine transformed cat " + str(i+1)])
    c2.show()


# Iterative Demo End


# Iterative Demo2
def demo4():
    im1 = Image.open('1.png')
    im = array(im1.convert('L'))
    H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
    im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))

    imgs = []
    titles = []
    for i in range(100):
        imgs.append(im1)
        titles.append("cat_" + str(i + 1))

    c3 = vis.showimgs(imgs=imgs, title=titles)


# Iterative Demo2 End





"""
we no longer need to use this chunk of code
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
"""
rects = vis.Rects(edgecolor='cyan', linewidth=1.5)
rects.addRect(0, [57, 90], 90, 20)
rects.addRect(0, [87, 130], 18, 18, edgecolor='m')
rects.addRect(1, [56, 63], 140, 120, linewidth=3)
rects.addRect(2, [0, 70], 350, 165, linewidth=1,edgecolor='m')
rects.addRect(3, [180, 40], 100, 114, edgecolor='m', linewidth=2)


# Rect Demo

def rect_demo1():

    im1 = Image.open('1.png')
    im = array(im1.convert('L'))
    H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
    im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))
    c = vis.showimgs(imgs=[im1, im2], title=["cat","affine cat"], rect=rects)
    # c = vis.showimgs(imgs=[im1, im2, im3, im4], title=titles, rect=rects, dot=dots, line=lines, override=setting,
    #                  open=False)

    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    rect = plt.Rectangle((57,90),90,20,fill=False, edgecolor = 'cyan',linewidth=1.5)
    ax.add_patch(rect)
    plt.imshow(im1)
    plt.show()

# rect_demo1()


# Line Demo

lines = vis.Lines(color = 'cyan')
# lines.addLine(0,[0,0],[200,200],type = 'solid', size = 3,input_style = "c")
# lines.addLine(1,[0,50],[200,50],type = 'dashdot', color = 'b', size = 3,input_style = "c")
# lines.addLine(1,[0,70],[200,70],type = [1,2,1,4], color = 'b', size = 3,input_style = "c")
# lines.addLine(1,[0,90],[200,90],type = [1,2,3,1,3,2,3,4,1,3], color = 'b', size = 2,input_style = "c")
# lines.addLine(2,[0,90],[350,90],type = 'solid',  size = 3,input_style = "c")
# lines.addLine(2,[0,110],[350,110],type = 'dotted',  size = 3,input_style = "c")
# lines.addLine(2,[0,130],[350,130],type = 'dashed',  size = 3,input_style = "c")
# lines.addLine(2,[0,150],[350,150],type = 'dashdot', color = 'black', size = 3,input_style = "c")
# lines.addLine(2,[0,170],[350,170],type = [1,2,3,4], color = 'r', size = 3,input_style = "c")
# lines.addLine(2,[0,190],[350,190],type = [0.5,2,0.5,0.1,0.5,2,3,4,1,3], color = 'cyan', size = 3,input_style = "c")
# lines.addLine(2,[0,210],[350,210],type = [1,2,3,4], color = 'm', size = 3,input_style = "c")
# lines.addLine(2,[0,230],[350,230],type = [1,2,3,4], color = 'w', size = 3,input_style = "c")

lines.addLine(0,[0,200],[0,200],type = 'solid', size = 3)
lines.addLine(1,[0,200],[50,50],type = 'dashdot', color = 'b', size = 3)
lines.addLine(1,[0,200],[70,70],type = 'dotted', color = 'b', size = 3)
lines.addLine(1,[0,200],[90,90],type = 'solid', color = 'r', size = 2)
lines.addLine(2,[0,350],[90,90],type = 'solid',  size = 3)
lines.addLine(2,[0,350],[110,110],type = 'dotted',  size = 3)
lines.addLine(2,[0,350],[130,130],type = 'dashed',  size = 3)
lines.addLine(2,[0,350],[150,150],type = 'dashdot', color = 'black', size = 3)
lines.addLine(2,[0,350],[170,170],type = [1,2,3,4], color = 'r', size = 3)
lines.addLine(2,[0,350],[190,190],type = [0.5,2,0.5,0.1,0.5,2,3,4,1,3], color = 'cyan', size = 3)
lines.addLine(2,[0,350],[210,210],type = [1,2,3,4], color = 'm', size = 3)
lines.addLine(2,[0,350],[230,230],type = [4,3,2,1], color = 'r', size = 3)




def line_demo():

    im1 = Image.open('1.png')
    im = array(im1.convert('L'))
    H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
    im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))

    im3 = Image.open('2.png')
    c = vis.showimgs(imgs=[im1, im2,im3], title=["cat", "affine cat", "white_board"], rect=rects, line = lines)
    # c = vis.showimgs(imgs=[im1, im2, im3, im4], title=titles, rect=rects, dot=dots, line=lines, override=setting,
    #                  open=False)

    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)
    plt.imshow(im2)
    plt.plot([0,200],[50,50], color="blue",linestyle='dashdot', linewidth=3)
    plt.plot([0,200],[70,70], color="blue",linestyle='dotted', linewidth=3)
    plt.plot([0, 200], [90, 90], color="r",linestyle='solid', linewidth=2)
    plt.show()

# line_demo()

dots = vis.Dots(color = 'cyan', size = 2)
dots.addDot(0,[66,80], type = 's', color = 'w',size = 3, font = "20px Arial", textcolor = "cyan", label = "dot1")
dots.addDot(0,[0,0], type = 's', color = 'r',size = 0.5)
dots.addDot(0,[66,20], type = 's', color = 'r', font = "Italic 20px Arial", textcolor = "cyan", size = 5, l = "dot2")
dots.addDot(0,[13,80], type = 's', color = 'g', font = "20px serif", textcolor = "m", size = 5, l = "dot3")
dots.addDot(0,[66,50], type = '.', color = 'm', textcolor = "r", l = "dot4", size = 5)
dots.addDot(1,[33,60], type = 's', color = 'w', font = "Italic 14px Arial", textcolor = "w", size = 5, l = "dot5")
dots.addDot(2,[66,20], type = 'v', color = 'r', font = "Italic 20px Arial", textcolor = "cyan", size = 5, l = "dot6")



startx = 20
step = 13
size2 = 8

for id,ch in enumerate(".,vo^<>12348sp*hH+xDd"):
    dots.addDot(2, [startx + id * step, 80], color = 'black', type=ch, size = size2)

dots.addDot(2,[startx + len(".,vo^<>12348sp*hH+xDd") * step,80], color = 'black', type = 'c',str="♪", size = size2)#Done
dots.addDot(2,[startx + len(".,vo^<>12348sp*hH+xDd1") * step,80], color = 'black', type = 'c',str="草", size = size2)#Done
dots.addDot(2,[startx + len(".,vo^<>12348sp*hH+xDd11") * step,80], color = 'black', type = 'c',str="⊙", size = size2)#Done
dots.addDot(2,[startx + len(".,vo^<>12348sp*hH+xDd111") * step,80], color = 'black', type = 'c',str="😅", size = size2*0.75)#Done
dots.addDot(2,[startx + len(".,vo^<>12348sp*hH+xDd11") * step,80 - 15], color = 'black', type = 'c',str="leet", size = size2*0.75)#Done

# dots.addDot(2,[12,80], type = '.', color = 'g', size = 2)#Done
# dots.addDot(2,[15,80], type = 's', color = 'b', size = 2)#Done
# dots.addDot(2,[18,80], type = 'v', color = 'g', size = 2)#Done
# dots.addDot(2,[21,80], type = 'o', color = 'g', size = 2)#Done
# dots.addDot(2,[24,80], type = '<', color = 'g', size = 2)#Done
# dots.addDot(2,[27,80], type = '^')#Done
# dots.addDot(2,[30,80], type = '>')#Done
# dots.addDot(2,[33,80], type = '1')
# dots.addDot(2,[36,80], type = '2')
# dots.addDot(2,[39,80], type = '3')
# dots.addDot(2,[42,80], type = '4')
# dots.addDot(2,[45,80], type = '8')#Done
# dots.addDot(2,[48,80], type = ',')#Done
# dots.addDot(2,[51,80], type = 'p')#Done
# dots.addDot(2,[54,80], type = '*')#Done
# dots.addDot(2,[57,80], type = 'h')#Done
# dots.addDot(2,[60,80], type = 'H')#Done
# dots.addDot(2,[63,80], type = '+')#Done
# dots.addDot(2,[66,80], type = 'x')#Done
# dots.addDot(2,[69,80], type = 'D')#Done
# dots.addDot(2,[72,80], type = 'd')#Done


def dot_demo():

    im1 = Image.open('1.png')
    im = array(im1.convert('L'))
    H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
    im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))

    im3 = Image.open('2.png')
    titles = ["cat", "affine cat", "white_board" ]

    c = vis.showimgs(imgs=[im1, im2, im3], title=titles, rect=rects, dot=dots, line=lines)

# dot_demo()



def setting_demo():

    im1 = Image.open('1.png')
    im = array(im1.convert('L'))
    H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
    im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))

    im3 = Image.open('2.png')
    titles = ["cat", "affine cat", "white_board"]


    setting = vis.VisLibSetting(scalemode = "auto")
    vis.showimgs(imgs=[im1, im2, im3], title=titles, rect=rects, dot=dots, line=lines, override=setting)

    setting = vis.VisLibSetting(scalemode = "fixed",scale = 1)
    vis.showimgs(imgs=[im1, im2, im3], title=titles, rect=rects, dot=dots, line=lines, override=setting)

    setting = vis.VisLibSetting(scalemode = "autofixed")
    vis.showimgs(imgs=[im1, im2, im3], title=titles, rect=rects, dot=dots, line=lines, override=setting)

    setting = vis.VisLibSetting(scalemode = "given",scale = [3,2,1])
    vis.showimgs(imgs=[im1, im2, im3], title=titles, rect=rects, dot=dots, line=lines, override=setting)

    setting = vis.VisLibSetting(scalemode = "original")
    vis.showimgs(imgs=[im1, im2, im3], title=titles, rect=rects, dot=dots, line=lines, override=setting)

    # setting = vis.VisLibSetting(titles=False, buttons=False, borders="15px solid black")
    # vis.showimgs(imgs=[im1, im2, im3], title=titles, rect=rects, dot=dots, line=lines, override = setting)

# setting_demo()





def setting_demo2():

    im1 = Image.open('1.png')
    im = array(im1.convert('L'))
    H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
    im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))

    im3 = Image.open('2.png')
    titles = ["cat", "affine cat", "white_board"]


    setting = vis.VisLibSetting(allowDrag= False, boxsize = (600,600),
                                titles=False, buttons=False, borders="4px solid cyan")


    vis.showimgs(im1, im2, im3, title=titles, rect=rects, dot=dots, line=lines, override = setting)

setting_demo2()


def cutomize_demo():

    im1 = Image.open('1.png')
    im = array(im1.convert('L'))
    H = array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
    im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))

    im3 = Image.open('2.png')
    im4 = Image.open('3.png')
    titles = ["cat", "affine cat", "white_board","dog"]





    vis.showimgs(im1, im2, im3, im4, title=titles, rect=rects, dot=dots, line=lines)

cutomize_demo()




vis.recycleall()








# im1 = Image.open('1.png')
# im = array(im1.convert('L'))
# H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
# im2 = ndimage.affine_transform(im, H[:2,:2],(H[0,2],H[1,2]))
#
# im3 = Image.open('2.png')
#
# im = array(im3.convert('L'))
# im4 = ndimage.affine_transform(im, H[:2,:2],(H[0,2],H[1,2]))
# #
# # c = vis.showimgs(im1,im2)
#
# """
# we no longer need to use this chunk of code
# rect1 = vis.MakeRect([67,40],147,14)
# rect2 = vis.MakeRect([87,130],93,18,edgecolor = 'w')
# rect3 = vis.MakeRect([56,63],189,188,edgecolor = 'g',linewidth = 3)
# rect4 = vis.MakeRect([120,27],66,55,edgecolor = 'cyan',linewidth = 1)
# rect5 = vis.MakeRect([62,49],152,114,edgecolor = 'm',linewidth = 5)
# rects1 = []
# rects1.append(rect1)
# rects1.append(rect2)
# rects2 = []
# rects2.append(rect3)
# rects3 = []
# rects3.append(rect4)
# rects4 = []
# rects4.append(rect5)
# rectss=[]
# rectss.append(rects1)
# rectss.append(rects2)
# rectss.append(rects3)
# rectss.append(rects4)
# """
#
#
# rects = vis.Rects()
# rects.addRect(0,[67,40],147,14)
# rects.addRect(0,[87,130],93,18,edgecolor = 'w')
# rects.addRect(1,[56,63],189,188,edgecolor = 'g',linewidth = 3)
# rects.addRect(2,[120,27],66,55,linewidth = 1)
# rects.addRect(3,[62,49],152,114,edgecolor = 'm',linewidth = 5)
#
#
#
#
# dots = vis.Dots(color = 'cyan', size = 2)
# dots.addDot(0,[66,80], type = 's', color = 'w',size = 3, font = "2px Arial", textcolor = "cyan", label = "xld")
# dots.addDot(0,[0,0], type = 's', color = 'r',size = 0.5)
# dots.addDot(0,[66,20], type = 's', color = 'r', font = "Italic 20px Arial", textcolor = "cyan", size = 5, l = "2333")
# dots.addDot(0,[13,80], type = 's', color = 'g', font = "20px serif", textcolor = "m", size = 5, l = "23333")
# dots.addDot(0,[66,50], type = '.', color = 'm', textcolor = "r", l = "2333", size = 5)
# dots.addDot(1,[66,80], type = 's', color = 'w', font = "Italic 14px Arial", textcolor = "w", size = 5, l = "233")
# dots.addDot(2,[66,20], type = 'v', color = 'r', font = "Italic 20px Arial", textcolor = "cyan", size = 5, l = "2333")
#
# dots.addDot(2,[12,80], type = '.', color = 'g', size = 2)#Done
# dots.addDot(2,[15,80], type = 's', color = 'b', size = 2)#Done
# dots.addDot(2,[18,80], type = 'v', color = 'g', size = 2)#Done
# dots.addDot(2,[21,80], type = 'o', color = 'g', size = 2)#Done
# dots.addDot(2,[24,80], type = '<', color = 'g', size = 2)#Done
#
#
# dots.addDot(2,[27,80], type = '^')#Done
# dots.addDot(2,[30,80], type = '>')#Done
# dots.addDot(2,[33,80], type = '1')
# dots.addDot(2,[36,80], type = '2')
# dots.addDot(2,[39,80], type = '3')
# dots.addDot(2,[42,80], type = '4')
# dots.addDot(2,[45,80], type = '8')#Done
# dots.addDot(2,[48,80], type = ',')#Done
# dots.addDot(2,[51,80], type = 'p')#Done
# dots.addDot(2,[54,80], type = '*')#Done
# dots.addDot(2,[57,80], type = 'h')#Done
# dots.addDot(2,[60,80], type = 'H')#Done
# dots.addDot(2,[63,80], type = '+')#Done
# dots.addDot(2,[66,80], type = 'x')#Done
# dots.addDot(2,[69,80], type = 'D')#Done
# dots.addDot(2,[72,80], type = 'd')#Done
# dots.addDot(2,[75,80], type = 'c',str="♪")#Done
#
# #
# lines = vis.Lines(color = 'cyan')
# lines.addLine(0,[0,90],[200,90],type = 'solid', size = 3)
# lines.addLine(0,[0,100],[200,100],type = 'dotted', color = 'b', size = 3)
# lines.addLine(0,[0,110],[200,110],type = 'dashed', color = 'b', size = 3)
# lines.addLine(1,[0,120],[200,120],type = 'dashdot', color = 'b', size = 3)
# lines.addLine(1,[0,130],[200,130],type = [1,2,1,4], color = 'b', size = 3)
# lines.addLine(1,[0,140],[200,140],type = [1,2,3,1,3,2,3,4,1,3], color = 'b', size = 2)
# lines.addLine(2,[0,90],[200,90],type = 'solid', color = 'b', size = 3)
# lines.addLine(2,[0,100],[200,100],type = 'dotted', color = 'b', size = 3)
# lines.addLine(2,[0,110],[200,110],type = 'dashed', color = 'b', size = 1)
# lines.addLine(2,[0,120],[200,120],type = 'dashdot', color = 'b', size = 2.5)
# lines.addLine(2,[0,130],[200,130],type = [1,2,3,4], color = 'b', size = 3)
# lines.addLine(2,[0,140],[200,140],type = [0.5,2,0.5,0.1,0.5,2,3,4,1,3], color = 'cyan', size = 3)
# lines.addLine(0,[0,140],[200,140],type = [1,2,3,4], color = 'w', size = 3)
# lines.addLine(4,[0,140],[200,140],type = [1,2,3,4], color = 'w', size = 3)
#
# setting = vis.VisLibSetting( titles = False, buttons = False, borders = "15px solid black")
#
# titles = ['cat1','cat2','dog','dog2']
# vis.showimgs(im1,im2,im3,im4,title = titles,  rect = rects,dot = dots,line = lines)
# vis.showimgs(im1,im2,im3,im4, title = titles, rect = rects, dot = dots,line = lines, override = setting)
# c = vis.showimgs(imgs = [im1,im2,im3,im4], title = titles, rect = rects, dot = dots,line = lines, override = setting, open = False)
#
# # c = vis.showimgs( title = titles, rect = rects, dot = dots,line = lines, override = setting, open = False)
# c = vis.showimg(im1, title = 'cat1', rect = rects, dot = dots,line = lines, override = setting, open = False)


# c = vis.showimgs(open=False)
# c.addImg(im1)
# c.show()
# c.addImg(im2)
# c.show()


#
#

#
# # vis.showimg(im1)
# # vis.showimg(im1,title = '12')
#
# # vis.showimgs(im1,im2,im1,im2)
# titles = ['cat1','cat2','dog','dog2']

# #use this instead:
# rects = vis.Rects()
# rects.addRect(0,[67,40],147,14)
# rects.addRect(0,[87,130],93,18,edgecolor = 'w')
# rects.addRect(1,[56,63],189,188,edgecolor = 'g',linewidth = 3)
# rects.addRect(2,[120,27],66,55,linewidth = 1)
# rects.addRect(3,[62,49],152,114,edgecolor = 'm',linewidth = 5)
#
# # vis.showimgs(im1,im2,im1,im2, title = titles)
# dots = vis.Dots(color = 'g', size = 2)
# dots.addDot(0,[66,80], type = 's', color = 'w',size = 0.5, font = "2px Arial", textcolor = "b", l = "233")
# dots.addDot(0,[0,0], type = 's', color = 'r',size = 0.5)
# dots.addDot(0,[66,20], type = 's', color = 'r', font = "Italic 20px Arial", textcolor = "cyan", size = 5, l = "2333")
# dots.addDot(0,[13,80], type = 's', color = 'g', font = "20px serif", textcolor = "m", size = 5, l = "23333")
# dots.addDot(0,[66,50], type = '.', color = 'm', textcolor = "r", l = "2333", size = 5)
# dots.addDot(1,[66,80], type = 's', color = 'w', font = "Italic 14px Arial", textcolor = "w", size = 5, l = "233")
# dots.addDot(2,[66,20], type = 'v', color = 'r', font = "Italic 20px Arial", textcolor = "cyan", size = 5, l = "2333")
#
# dots.addDot(2,[12,80], type = '.', color = 'g', size = 2)#Done
# dots.addDot(2,[15,80], type = 's', color = 'b', size = 2)#Done
# dots.addDot(2,[18,80], type = 'v', color = 'g', size = 2)#Done
# dots.addDot(2,[21,80], type = 'o', color = 'g', size = 2)#Done
# dots.addDot(2,[24,80], type = '<', color = 'g', size = 2)#Done
#
#
# dots.addDot(2,[27,80], type = '^')#Done
# dots.addDot(2,[30,80], type = '>')#Done
# dots.addDot(2,[33,80], type = '1')
# dots.addDot(2,[36,80], type = '2')
# dots.addDot(2,[39,80], type = '3')
# dots.addDot(2,[42,80], type = '4')
# dots.addDot(2,[45,80], type = '8')#Done
# dots.addDot(2,[48,80], type = ',')#Done
# dots.addDot(2,[51,80], type = 'p')#Done
# dots.addDot(2,[54,80], type = '*')#Done
# dots.addDot(2,[57,80], type = 'h')#Done
# dots.addDot(2,[60,80], type = 'H')#Done
# dots.addDot(2,[63,80], type = '+')#Done
# dots.addDot(2,[66,80], type = 'x')#Done
# dots.addDot(2,[69,80], type = 'D')#Done
# dots.addDot(2,[72,80], type = 'd')#Done
#
#
#
# # dots.addDot(2,[18,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[24,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[27,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[30,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[33,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[36,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[39,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[42,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[45,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[48,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[51,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[54,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[57,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[60,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[63,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[66,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[69,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[72,80], type = 'o', color = "cyan", size = 2)
# # dots.addDot(2,[75,80], type = 'o', color = "cyan", size = 2)
#
# # dots.addDot(3,[13,80], type = 'r', color = 'cyan', size = 2)
# dots.addDot(3,[16,180], type = 's', color = 'cyan', size = 2)
# dots.addDot(3,[63,180], color = 'g', size = 0, font = "Bold 34px Arial", textcolor = "m", l = "text here", nooffset = True)
#
#
#
# lines = vis.Lines(color = 'cyan')
# lines.addLine(0,[0,90],[200,90],type = 'solid', size = 3)
# lines.addLine(0,[0,100],[200,100],type = 'dotted', color = 'b', size = 3)
# lines.addLine(0,[0,110],[200,110],type = 'dashed', color = 'b', size = 3)
# lines.addLine(1,[0,120],[200,120],type = 'dashdot', color = 'b', size = 3)
# lines.addLine(1,[0,130],[200,130],type = [1,2,3,4], color = 'b', size = 3)
# lines.addLine(1,[0,140],[200,140],type = [1,2,3,4,8,2,3,4,1,3], color = 'b', size = 2)
# lines.addLine(2,[0,90],[200,90],type = 'solid', color = 'b', size = 3)
# lines.addLine(2,[0,100],[200,100],type = 'dotted', color = 'b', size = 3)
# lines.addLine(2,[0,110],[200,110],type = 'dashed', color = 'b', size = 1)
# lines.addLine(2,[0,120],[200,120],type = 'dashdot', color = 'b', size = 2.5)
# lines.addLine(2,[0,130],[200,130],type = [1,2,3,4], color = 'b', size = 3)
# lines.addLine(2,[0,140],[200,140],type = [0.5,2,0.5,0.1,0.5,2,3,4,1,3], color = 'cyan', size = 3)
# lines.addLine(0,[0,140],[200,140],type = [1,2,3,4], color = 'w', size = 3)
# lines.addLine(4,[0,140],[200,140],type = [1,2,3,4], color = 'w', size = 3)
#
# # setting = vis.VisLibSetting(scalemode = "auto",scale = 1)
# setting = vis.VisLibSetting(scalemode = "fixed",scale = 1, allowDrag = True, boxsize = (600,600), titles = True, buttons = True, borders = "1px solid cyan")
#
# # vis.showimgs(im1,im2,im3,im4, title = titles, rect = rects, dot = dots,line = lines, override = setting)
# # c = vis.showimgs(imgs = [im1,im2,im3,im4], title = titles, rect = rects, dot = dots,line = lines, override = setting, open = False)
#
# # c = vis.showimgs( title = titles, rect = rects, dot = dots,line = lines, override = setting, open = False)
# c = vis.showimg(im1, title = 'cat1', rect = rects, dot = dots,line = lines, override = setting, open = False)
#
# # c.show()
#
# c.addImg(im1,im2,title = ["2","3"])
# c.addImg(im1,title = "3")
#
# c.dot.addDot(2,[75,80], type = 'c',str = "😅", size = 12)#Done
# c.dot.addDot(4,[75,80], type = 'c',str = "😅", size = 12)#Done
# # c.show()
# c.dot.addDot(0,[75,80], type = 'c',str = "😅", size = 12)#Done
# # c.show()
# c.dot.addDot(1,[75,80], type = 'c',str = "😅", size = 12)#Done
#
# # c.show()
# c.dot.addDot(1,[99,80], type = 'c',str = "😅", size = 12)#Done
# c.show()
#
# # vis.showimgs(im1,im2,im3,im4, title = titles, rect = rects, dot = dots,line = lines, override = setting)
# # vis.showimgs(im1,im2,im3,im4, title = titles, rect = rects, dot = dots,line = lines)
#
#
#
# # vis.showimgs(im1,im2,im3,im4, title = titles, dot = dots,line = lines)
#
#
# titles2 = titles + titles + titles + titles
# # titles3 = titles2+titles2+titles2+titles2+titles2+titles2+titles2+titles2+titles2+titles2
# # vis.showimgs(im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4,im1,im2,im3,im4, title = titles3)
#
# # vis.showimgs(im1,im2,im2,im2)
#
# # vis.showimg(im1)
# # vis.showimg(im1,title = 'cat')
#
# # vis.showimgs(im1,im2,im3,im4, title = titles)
#
#
#
#
# # im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
# im5 = Image.open('4.png')
#
#
# im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)
# subplot(121)
# imshow(im1)
# subplot(122)
# imshow(im5)
# show()

# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# rect = plt.Rectangle((67,40),147,14,fill=False, edgecolor = 'red',linewidth=1)
# ax.add_patch(rect)
# plt.imshow(im1) # 图像数组
# plt.show()



