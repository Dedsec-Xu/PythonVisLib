import random
import string
import imageio
import webbrowser
import json
import matplotlib
import numpy as np

import warnings

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
      self.override = kwargs['override']
      self.layout= kwargs['layout']
      self.rectlist = kwargs['rectlist']
      self.dotlist = kwargs['dotlist']
      self.linelist = kwargs['linelist']

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

class Rect():
   def __init__(self, xy, width, height, **kwargs):
      self.x = xy[0]
      self.y = xy[1]
      self.width = width
      self.height = height



      r = rectCheck(**kwargs)
      self.edgecolor = r["edgecolor"]
      self.linewidth = r["linewidth"]


      if 'edgecolor' in kwargs and 'c' in kwargs:
         raise RuntimeError("don't use edge color and c at the same time!")
      if 'edgecolor' in kwargs:
         self.edgecolor = matplotlib.colors.to_hex(kwargs['edgecolor'])
      elif 'c' in kwargs:
         self.edgecolor = matplotlib.colors.to_hex(kwargs['c'])
      else:
         self.edgecolor = matplotlib.colors.to_hex('r')

      if 'linewidth' in kwargs:
         self.linewidth = kwargs['linewidth']
      else:
         self.linewidth = "1"

   def makejson(self):
      return json.dumps(self.__dict__)

class Rects():
   def __init__(self, **kwargs):
      self.rects = []
      self.amount = 0

      d = {'edgecolor': matplotlib.colors.to_hex('r'),
           "linewidth": "1"}

      self.default = rectCheck(**kwargs,default =d)

   def addRect(self,num,xy, width, height, **kwargs):
      while self.amount <= num:
         self.rects.append([])
         self.amount += 1
      self.rects[num].append(Rect(xy, width, height, **kwargs,default = self.default).makejson())




def rectCheck(**kwargs):
   ret = {}
   defaultDict = kwargs["default"]

   if 'edgecolor' in kwargs and 'c' in kwargs:
      raise RuntimeError("don't use edge color and c at the same time!")
   if 'edgecolor' in kwargs:
      ret["edgecolor"] = matplotlib.colors.to_hex(kwargs['edgecolor'])
   elif 'c' in kwargs:
      ret["edgecolor"] = matplotlib.colors.to_hex(kwargs['c'])
   else:
      ret["edgecolor"] = defaultDict["edgecolor"]

   if 'linewidth' in kwargs:
      ret["linewidth"] = kwargs['linewidth']
   else:
      ret["linewidth"] = defaultDict["linewidth"]
      # ret["linewidth"] = "1"

   return ret

class Dot():
   def __init__(self, xy, **kwargs):
      self.x = xy[0]
      self.y = xy[1]
      default = kwargs["default"]

      r = dotCheck(**kwargs)
      self.type = r["type"]
      self.color = r["color"]
      self.size = r["size"]
      self.label = r["label"]
      self.font = r["font"]
      self.textcolor = r["textcolor"]
      self.nooffset = r["nooffset"]
      self.str = r["str"]

      # if 'type' in kwargs and 't' in kwargs:
      #    raise RuntimeError("don't use type and t at the same time!")
      # if 'type' in kwargs:
      #    self.type = kwargs['type']
      #    if len(self.type) != 1:
      #       raise RuntimeError('dot type must be a character')
      #    supported = "ro"
      #    if self.type not in supported:
      #       raise RuntimeError('dot type must be in [ro]')
      # elif 't' in kwargs:
      #    self.type = kwargs['t']
      #    if len(self.type) != 1:
      #       raise RuntimeError('dot type must be a character')
      #    supported = "ro"
      #    if self.type not in supported:
      #       raise RuntimeError('dot type must be in [ro]')
      # else:
      #    self.type = self.default['type']
      #
      # if 'color' in kwargs and 'c' in kwargs:
      #    raise RuntimeError("don't use edge color and c at the same time!")
      # if 'color' in kwargs:
      #    self.color = matplotlib.colors.to_hex(kwargs['color'])
      # elif 'c' in kwargs:
      #    self.color = matplotlib.colors.to_hex(kwargs['c'])
      # else:
      #    self.color = matplotlib.colors.to_hex('r')
      #
      # if 'size' in kwargs and 's' in kwargs:
      #    raise RuntimeError("don't use size and s at the same time!")
      # if 'size' in kwargs:
      #    self.size = kwargs['size']
      # elif 's' in kwargs:
      #    self.size = kwargs['s']
      # else:
      #    self.size = 1
      #
      # if 'label' in kwargs:
      #    self.label = kwargs['label']
      # elif 'l' in kwargs:
      #    self.label = kwargs['l']
      # else:
      #    self.label = ""
      #
      # if 'font' in kwargs:
      #    self.font = kwargs['font']
      # else:
      #    self.font = "12px serif"
      #
      # if 'textcolor' in kwargs:
      #    self.textcolor = matplotlib.colors.to_hex(kwargs['textcolor'])
      # else:
      #    self.textcolor = self.color
      #
      # if 'nooffset' in kwargs:
      #    if kwargs['nooffset']:
      #       self.nooffset = True
      #    else:
      #       self.nooffset = False
      # else:
      #    self.nooffset = False

   def makejson(self):
      return json.dumps(self.__dict__)

class Dots():
   def __init__(self, **kwargs):
      self.dots = []
      self.amount = 0
      d = {'type':'r',
           "color": matplotlib.colors.to_hex('r'),
           "size":1,
           "label":"",
           "font":"12px serif",
           "nooffset":False
           }
      self.default = dotCheck(**kwargs,default =d)


   def addDot(self,num,xy,**kwargs):
      while self.amount <= num:
         self.dots.append([])
         self.amount += 1
      self.dots[num].append(Dot(xy, **kwargs, default = self.default).makejson())


def dotCheck(**kwargs):
   ret = {}
   defaultDict = kwargs["default"]

   if 'type' in kwargs and 't' in kwargs:
      raise RuntimeError("don't use type and t at the same time!")
   if 'type' in kwargs:
      ret["type"] = kwargs['type']
      if len(ret["type"]) != 1:
         raise RuntimeError('dot type must be a character')
      supported = ".,vo^<>12348sp*hH+xXDdc"
      if ret["type"] not in supported:
         raise RuntimeError('dot type must be in [.,vo^<>12348sp*hH+xXDdc]')
   elif 't' in kwargs:
      ret["type"] = kwargs['t']
      if len(ret["type"]) != 1:
         raise RuntimeError('dot type must be a character')
      supported = ".,vo^<>12348sp*hH+xDdc"
      if ret["type"] not in supported:
         raise RuntimeError('dot type must be in [.,vo^<>12348sp*hH+xXDdc]')
   else:
      ret["type"] = defaultDict['type']

   ret["str"] =""
   if ret["type"] == "c":
      if 'str' not in kwargs:
         raise RuntimeError('You must determine a str if the type is set to custom')
      else:
         ret["str"] = kwargs["str"]
   if 'str' in kwargs and ret["type"] != "c":
      raise RuntimeError('You must not set str if type is not set to custom')

   if 'color' in kwargs and 'c' in kwargs:
      raise RuntimeError("don't use edge color and c at the same time!")
   if 'color' in kwargs:
      ret["color"] = matplotlib.colors.to_hex(kwargs['color'])
   elif 'c' in kwargs:
      ret["color"] = matplotlib.colors.to_hex(kwargs['c'])
   else:
      ret["color"] = defaultDict['color']
      # ret["color"] = matplotlib.colors.to_hex('r')

   if 'size' in kwargs and 's' in kwargs:
      raise RuntimeError("don't use size and s at the same time!")
   if 'size' in kwargs:
      ret["size"] = kwargs['size']
   elif 's' in kwargs:
      ret["size"] = kwargs['s']
   else:
      ret["size"] = defaultDict['size']
      # ret["size"] = 1

   if 'label' in kwargs:
      ret["label"] = kwargs['label']
   elif 'l' in kwargs:
      ret["label"] = kwargs['l']
   else:
      ret["label"] = defaultDict['label']
      # ret["label"] = ""

   if 'font' in kwargs:
      ret["font"] = kwargs['font']
   else:
      ret["font"] = defaultDict['font']
      # ret["font"] = "12px serif"

   if 'textcolor' in kwargs:
      ret["textcolor"] = matplotlib.colors.to_hex(kwargs['textcolor'])
   else:
      ret["textcolor"] = ret["color"]

   if 'nooffset' in kwargs:
      if kwargs['nooffset']:
         ret["nooffset"] = True
      else:
         ret["nooffset"] = False
   else:
      ret["nooffset"] = defaultDict['nooffset']
      # ret["nooffset"] = False
   return ret



class Line():
   def __init__(self, xy, xy2, **kwargs):
      self.x = xy[0]
      self.y = xy[1]
      self.x2 = xy2[0]
      self.y2 = xy2[1]
      self.type=[]

      default = kwargs['default']
      print(default)
      print(default)
      print(default)

      r = lineCheck(**kwargs)
      self.type = r["type"]
      self.color = r["color"]
      self.size = r["size"]

      # if 'type' in kwargs and 't' in kwargs:
      #    raise RuntimeError("don't use type and t at the same time!")
      # elif 'type' in kwargs:
      #    typeindex = kwargs['type']
      # elif 't' in kwargs:
      #    typeindex = kwargs['t']
      # else:
      #    typeindex = self.default['type']
      # print(typeindex)
      #
      # if type(typeindex) == type('1'):
      #    supported = {'-':[],
      #                ':':[1,1],
      #                '--':[5,2],
      #                '-.':[8,1,1,1],
      #                'solid':[],
      #                'dotted':[1,1],
      #                'dashed':[5,2],
      #                'dashdot':[8,1,1,1]
      #                 }
      #    if typeindex not in supported:
      #       raise RuntimeError("line type must be in ['-', ':', '--', '-.', 'solid', 'dotted', 'dashed', 'dashdot'] or a list")
      #    else:
      #       self.type = supported[typeindex]
      # elif isinstance(typeindex, list) and np.array(typeindex).ndim == 1 and all((isinstance(item, int) or isinstance(item, float))for item in typeindex):
      #    self.type = typeindex
      # else:
      #    raise RuntimeError("line type must be in ['-', ':', '--', '-.', 'solid', 'dotted', 'dashed', 'dashdot'] or a list")
      #
      #
      #
      #
      #
      # if 'color' in kwargs and 'c' in kwargs:
      #    raise RuntimeError("don't use edge color and c at the same time!")
      # if 'color' in kwargs:
      #    self.color = matplotlib.colors.to_hex(kwargs['color'])
      # elif 'c' in kwargs:
      #    self.color = matplotlib.colors.to_hex(kwargs['c'])
      # else:
      #    self.color = self.default['color']
      #
      # if 'size' in kwargs and 's' in kwargs:
      #    raise RuntimeError("don't use size and s at the same time!")
      # if 'size' in kwargs:
      #    self.size = kwargs['size']
      # elif 's' in kwargs:
      #    self.size = kwargs['s']
      # else:
      #    self.size = self.default['size']

   def makejson(self):
      print(json.dumps(self.__dict__))
      return json.dumps(self.__dict__)


class Lines():
   def __init__(self, **kwargs):
      self.lines = []
      self.amount = 0
      d = {'type':'solid','size':1, "color": matplotlib.colors.to_hex("r")}
      self.default = lineCheck(**kwargs,default =d)


   def addLine(self, num, xy, xy2, **kwargs):
      while self.amount <= num:
         self.lines.append([])
         self.amount += 1
      self.lines[num].append(Line(xy, xy2, **kwargs, default = self.default).makejson())



def lineCheck(**kwargs):
   ret = {}
   defaultDict = kwargs["default"]

   typeindex = 'soild'
   if 'type' in kwargs and 't' in kwargs:
      raise RuntimeError("don't use type and t at the same time!")
   elif 'type' in kwargs:
      typeindex = kwargs['type']
   elif 't' in kwargs:
      typeindex = kwargs['t']
   else:
      typeindex = defaultDict['type']
      print("typeindex = defaultDict['type']")
   print(typeindex)

   if type(typeindex) == type('1'):
      supported = {'-': [],
                   ':': [1, 1],
                   '--': [5, 2],
                   '-.': [8, 1, 1, 1],
                   'solid': [],
                   'dotted': [1, 1],
                   'dashed': [5, 2],
                   'dashdot': [8, 1, 1, 1]
                   }
      if typeindex not in supported:
         raise RuntimeError(
            "line type must be in ['-', ':', '--', '-.', 'solid', 'dotted', 'dashed', 'dashdot'] or a list")
      else:
         ret["type"] = supported[typeindex]
   elif isinstance(typeindex, list) and np.array(typeindex).ndim == 1 and all(
           (isinstance(item, int) or isinstance(item, float)) for item in typeindex):
      ret["type"] = typeindex
   else:
      raise RuntimeError(
         "line type must be in ['-', ':', '--', '-.', 'solid', 'dotted', 'dashed', 'dashdot'] or a list")

   if 'color' in kwargs and 'c' in kwargs:
      raise RuntimeError("don't use edge color and c at the same time!")
   if 'color' in kwargs:
      ret["color"] = matplotlib.colors.to_hex(kwargs['color'])
   elif 'c' in kwargs:
      ret["color"] = matplotlib.colors.to_hex(kwargs['c'])
   else:
      ret["color"] = defaultDict['color']

   if 'size' in kwargs and 's' in kwargs:
      raise RuntimeError("don't use size and s at the same time!")
   if 'size' in kwargs:
      ret["size"] = kwargs['size']
   elif 's' in kwargs:
      ret["size"] = kwargs['s']
   else:
      ret["size"] = defaultDict['size']

   return ret


class VisLibSetting():
   def __init__(self, **kwargs):
      if 'scalemode' in kwargs:
         supported = ["auto","autofixed","given","fixed","original","a","af","g","f","o"]
         d = {"a":"auto",
              "af": "autofixed",
              "g": "given",
              "f": "fixed",
              "o":"original"
              }
         self.scalemode = kwargs['scalemode']
         if self.scalemode not in supported:
            raise RuntimeError('scalemode must be in ["auto","autofixed","given","fixed","original","a","af","g","f","o"]')
         if self.scalemode in d:
            self.scalemode = d[self.scalemode]
      else:
         self.scalemode = "auto"

      if 'scale' in kwargs:
         if self.scalemode in ["auto","autofixed", "original"]:
            raise RuntimeError('you can not determine imgscale if scalemode is auto, autofixed, or original')
         self.scale = kwargs['scale']
      else:
         if self.scalemode == "fixed":
            raise RuntimeError('you must specify a scale if scalemode is fixed')
         if self.scalemode == "given":
            raise RuntimeError('you must specify a scale if scalemode is given')
         self.scale = 1

      if self.scalemode == "original":
         self.scale = 1
         self.scalemode = "fixed"

      if 'allowDrag' in kwargs:
         self.allowDrag = kwargs['allowDrag']
      else:
         self.allowDrag = True

      if 'buttons' in kwargs:
         self.buttons = kwargs['buttons']
      else:
         self.buttons = True

      if 'titles' in kwargs:
         self.titles = kwargs['titles']
      else:
         self.titles = True

      if 'boxsize' in kwargs:
         self.boxsize = kwargs['boxsize']
      else:
         self.boxsize = (300,300)

      if 'borders' in kwargs:
         self.borders = kwargs['borders']
         if not isinstance(self.borders, type("1px solid black")):
            if isinstance(self.borders,int) or isinstance(self.borders,float):
               self.borders = "{}px solid black".format(self.borders)

      else:
         self.borders = "1px solid black"



      # if 'allowButton' in kwargs:
      #    self.allowButton = kwargs['allowButton']
      # else:
      #    self.allowButton = True

   def makejson(self):
      return json.dumps(self.__dict__)




class ImageHandler():
   def __init__(self, *args, **kwargs):
      self.handles = []
      self.imglist = []
      self.titlelist = []
      self.rectlist = []

      self.dotlist = []

      self.linelist = []

      self.hasRect = False
      self.hasTitle = False
      self.hasDot = False
      self.hasLine = False
      self.imgs =[]
      self.dot = Dots()
      # print(kwargs)

      self.checkInput(*args, **kwargs)

      if not args and 'imgs' not in kwargs:
         if "open" not in kwargs:
            raise RuntimeError("You can not show page if there are no images")
         else:
            if kwargs["open"]:
               raise RuntimeError("You can not show page if there are no images")
         self.imgs = []
      else:
         self.imgs = list(args)
         if 'imgs' in kwargs:
            self.imgs = kwargs['imgs']



      if 'title' in kwargs:
         self.hasTitle = True
         self.titlelist = kwargs['title'][:]
      else:
         self.titlelist = [''] * len(self.imgs)
      if 'rect' in kwargs:
         self.hasRect = True
         self.rect = kwargs['rect']
      else:
         self.rect = Rects()
      if 'dot' in kwargs:
         self.hasDot = True
         self.dot = kwargs['dot']
      else:
         self.dot = Dots()
      if 'line' in kwargs:
         self.hasLine = True
         self.line = kwargs['line']
      else:
         self.line = Lines()

      open = True
      if "open" in kwargs:
         open = kwargs['open']

      self.inputscale = -1
      if 'override' in kwargs:
         o = kwargs['override']
         if isinstance(o.scale,list):
            self.inputscale = -1
            if len(o.scale)!=len(self.imgs):
               print("if len(o.scale)!=len(self.imglist)")
               print(len(self.imgs))
               raise RuntimeError('input override scale is not same length as the image array')
         else:
            self.inputscale = o.scale
            if self.inputscale <= 0:
               raise RuntimeError('inputscale must be a valid number')
            o.scale=[o.scale] * len(self.imgs)
         self.override = o
      else:
         o = VisLibSetting()
         self.inputscale = o.scale

         if self.inputscale <= 0:
            raise RuntimeError('inputscale must be a valid number')
         o.scale = [o.scale] * len(self.imglist)
         self.override = o

      for img in self.imgs:
         handle = generate_random_handler(20)
         imageio.imwrite("./static/image/"+handle+".png", img)
         # webbrowser.open('http://127.0.0.1:8000/show/'+handle)
         self.handles.append(handle)
         self.imglist.append(handle)

      if open:
         self.show()




       # 'http://127.0.0.1:8000/imagesource/json/GMJedBqSVIE5vUtgOLRu.json'

   def addImg(self, *args, **kwargs):
      argss = args

      if len(args) == 0 and 'imgs' not in kwargs:
         raise RuntimeError('no input')
      if 'imgs' in kwargs:
         argss = kwargs['imgs']
         if len(args):
            raise RuntimeError("do not input arg if you are using array mode")


      img_cnt = len(argss)
      for img in argss:
         handle = generate_random_handler(20)
         imageio.imwrite("./static/image/" + handle + ".png", img)
         # webbrowser.open('http://127.0.0.1:8000/show/'+handle)
         self.imgs.append(img)
         self.handles.append(handle)
         self.imglist.append(handle)

      if "title" in kwargs:
         if isinstance(kwargs["title"], list):
            if len(kwargs["title"]) != img_cnt:
               raise RuntimeError("Title amount mismatch with images")

      if "title" in kwargs:
         if img_cnt == 1:
            if isinstance(kwargs["title"],list):
               self.titlelist.append(kwargs["title"][0])
            else:
               if isinstance(kwargs["title"], str):
                  self.titlelist.append(kwargs["title"])
               else:
                  raise RuntimeError("The title you input is not string")
         else:
            if isinstance(kwargs["title"], list): #have title input
               for t in kwargs["title"]:
                  self.titlelist.append(t)
            else: #not array
               raise RuntimeError("The title argument should be an array if you want to input multiple images")

      else:
         warnings.warn("You did not input any titles")
         for i in range(img_cnt):
            self.titlelist.append("")

      if self.inputscale == -1:
         if "scale" not in kwargs:
            raise RuntimeError("You must input scale if the scale for each image is set seperately")
         if isinstance(kwargs["scale"], list):
            if len(kwargs["scale"]) != img_cnt:
               raise RuntimeError("scale amount mismatch with images")
            else:
               for i in kwargs["scale"]:
                  self.override.scale.append(i)
         else:
            for i in range(img_cnt):
               self.override.scale.append(kwargs["scale"])
      else:
         if "scale" in kwargs:
            raise RuntimeError("You must not input scale if the scale for each image is not set seperately")

         for i in range(img_cnt):
            self.override.scale.append(self.inputscale)







   def show(self):
      if not self.imgs:
         raise RuntimeError("You can not show page if there are no images")
      if len(self.rect.rects)>len(self.imgs):
         warnings.warn("You have more rects than images")


      if len(self.dot.dots)>len(self.imgs):
         warnings.warn("You have more dots than images")

      if len(self.line.lines)>len(self.imgs):
         warnings.warn("You have more lines than images")

      self.rectlist = json.loads(json.dumps(self.rect.rects[:]))
      self.dotlist = json.loads(json.dumps(self.dot.dots[:]))
      self.linelist = json.loads(json.dumps(self.line.lines[:]))

      self.jsonhandle = generate_random_handler(20)
      PageJson(imglist=self.imglist, titlelist=self.titlelist, override=self.override.makejson(), mode='1', layout='1',
               rectlist=self.rectlist, dotlist=self.dotlist, linelist=self.linelist).saveJson(
         "./static/json/" + self.jsonhandle + ".json")
      webbrowser.open('http://127.0.0.1:8000/showjs/' + self.jsonhandle)


   def checkInput(self, *args, **kwargs):
      argss = args
      if len(args) == 0 and 'imgs' not in kwargs:
         warnings.warn("noinput")
      if 'imgs' in kwargs:
         argss = kwargs['imgs']
         if len(args):
            raise RuntimeError("do not input arg if you are using array mode")

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
            elif len(kwargs['title'])!=len(argss):
               print('title list mismatch with images')
         # if 'rect' in kwargs:
         #    if len(kwargs['rect'].rects) > len(argss):
         #       raise RuntimeError('too many rectangles')
         # if 'dot' in kwargs:
         #    if len(kwargs['dot'].dots) > len(argss):
         #       raise RuntimeError('too many dots')
         # if 'line' in kwargs:
         #    if len(kwargs['line'].lines) > len(argss):
         #       raise RuntimeError('too many lines')



def showimg(img, **kwargs):
   print(kwargs)
   if "title" in kwargs:
      kwargs["title"] = [kwargs["title"]]

   return showimgs(img,  **kwargs)


def showimgs(*args, **kwargs):
   handles = []

   x = ImageHandler(*args, **kwargs, caller = 'showimgs')
   # for img in args:
   #    x = ImageHandler(img)
   #    handles.append(x.handle)
   return x



# def showimg(**kwargs):
#    handles = []
#    for img in args:
#       x = ImageHandler(img,1)
#       handles.append(x.handle)
#    return handles