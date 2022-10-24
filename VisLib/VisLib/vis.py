import random
import string
import imageio
import webbrowser



def generate_random_handler(randomlength):
   str_list = random.sample(string.digits + string.ascii_letters, randomlength)
   random_str = ''.join(str_list)
   return random_str



class ImageHandler:
   def __init__(self, img):
      self.handle = generate_random_handler(20)
      imageio.imwrite("./static/image/"+self.handle+".png", img)
      webbrowser.open('http://127.0.0.1:8000/show/'+self.handle)


def func(im2):
   ImageHandler(im2)
   return