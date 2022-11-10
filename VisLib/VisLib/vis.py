import random
import string
import imageio
import webbrowser
import json
import matplotlib
import numpy

import PIL



def generate_random_handler(randomlength):
   str_list = random.sample(string.digits + string.ascii_letters, randomlength)
   random_str = ''.join(str_list)
   return random_str





class PageJson():
   def __init__(self, **kwargs):
      self.imglist = kwargs['imglist']
      # self.imgcnt = kwargs['imgcnt']
      self.titlelist = kwargs['titlelist']
      self.mode = kwargs['mode']
      self.layout= kwargs['layout']

      self.rectlist = kwargs['rectlist']

   def saveJson(self,str):
      js = json.dumps(self.__dict__)
      print(js)
      fh = open(str, 'w')
      fh.write(js)
      fh.close()

class DrawJson():
   def __init__(self, **kwargs):
      self.rect = kwargs['rect']
      self.recttag = kwargs['recttag']
      self.dot = kwargs['dot']
      self.dottag = kwargs['dottag']
      self.line = kwargs['line']
      self.dottag = kwargs['dottag']
      self.style = kwargs['style']

   def saveJson(self,str):
      js = json.dumps(self.__dict__)
      print(js)
      fh = open(str, 'w')
      fh.write(js)
      fh.close()

class MakeRect():
   def __init__(self, xy, width, height, **kwargs):
      self.x = xy[0]
      self.y = xy[1]
      self.width = width
      self.height = height
      if 'label' in kwargs:
         self.label = kwargs['label']
      else:
         self.label = ''
      if 'edgecolor' in kwargs:
         self.edgecolor = matplotlib.colors.to_hex(kwargs['edgecolor'])
      else:
         self.edgecolor = matplotlib.colors.to_hex('r')

      if 'linewidth' in kwargs:
         self.linewidth = kwargs['linewidth']
      else:
         self.linewidth = "1"

   def makejson(self):
      return json.dumps(self.__dict__)

# class Rects():
#    def __init__(self):
#
#    def append(self,id:int, r:MakeRect):




class ImageHandler():
   def __init__(self, *args, **kwargs):
      self.handles = []
      self.imglist = []
      self.titlelist = []
      self.rectlist = []
      # print(kwargs)

      self.checkInput(*args, **kwargs)
      self.jsonhandle = generate_random_handler(20)
      for img in args:
         handle = generate_random_handler(20)
         imageio.imwrite("./static/image/"+handle+".png", img)
         # webbrowser.open('http://127.0.0.1:8000/show/'+handle)
         self.handles.append(handle)
         self.imglist.append(handle)
      if kwargs['caller'] == 'showimg':
         if 'title' in kwargs:
            self.titlelist.append(kwargs['title'])
         else:
            self.titlelist.append('')
      if kwargs['caller'] == 'showimgs':
         if 'title' in kwargs:
            self.titlelist = kwargs['title'][:]
         else:
            self.titlelist = [''] * len(args)
      if 'rect' in kwargs:
         self.rectlist = json.loads(json.dumps(kwargs['rect'][:]))

      PageJson(imglist = self.imglist, titlelist = self.titlelist, mode = '1', layout = '1',rectlist=self.rectlist).saveJson("./static/json/"+self.jsonhandle+".json")

      webbrowser.open('http://127.0.0.1:8000/showjs/' + self.jsonhandle)
       # 'http://127.0.0.1:8000/imagesource/json/GMJedBqSVIE5vUtgOLRu.json'


   def checkInput(self, *args, **kwargs):
      if len(args) == 0 :
         raise RuntimeError('no input')
      if kwargs['caller'] == 'showimg':
         # print('showimg')
         if 'title' in kwargs:
            if not isinstance(kwargs['title'],str):
               raise RuntimeError('title should be a string')
      elif kwargs['caller'] == 'showimgs':
         # print('showimgs')
         if 'title' in kwargs:
            if not isinstance(kwargs['title'], list):
               raise RuntimeError('title should be a list')
            elif not all(isinstance(n, str) for n in kwargs['title']):

               raise RuntimeError('title should be a list of strings')
            elif len(kwargs['title'])!=len(args):
               print('title list mismatch with images')




def showimg(img, **kwargs):
   print(kwargs)
   x = ImageHandler(img, **kwargs, caller = 'showimg')
   return x.jsonhandle


def showimgs(*args, **kwargs):
   handles = []
   x = ImageHandler(*args, **kwargs, caller = 'showimgs')
   # for img in args:
   #    x = ImageHandler(img)
   #    handles.append(x.handle)
   return x.jsonhandle

# def showimgs(**kwargs):
#    handles = []
#    for img in args:
#       x = ImageHandler(img,1)
#       handles.append(x.handle)
#    return handles