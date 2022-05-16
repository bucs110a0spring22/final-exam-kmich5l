import requests
import tkinter
from tkinter import *
import facts
import image
import urllib.request
from PIL import ImageTk, Image 


def funcatfacts():
  '''
    This function adds the screen window along with a random cat fact and image.
    arg: none
    return: none
  '''
  root = tkinter.Tk()
  canvas = Canvas(root, width = 750, height = 700) 
  root.wm_title("FUN CAT FACTS")
  
  line = facts.Facts()
  response = line.get()
  canvas.create_text(370, 50, text= (response ["fact"]), fill="black", font=('Helvetica 11 normal'))

  
  urllib.request.urlretrieve("https://cataas.com/cat","cat.png")
  img = ImageTk.PhotoImage(Image.open("cat.png"))  
  canvas.create_image(65, 80, anchor = NW, image = img)
  

  canvas.pack()
  root.mainloop() 
  
def main():
  '''
    This function runs the root.mainloop
    arg: none
    return: none
  '''
  funcatfacts()
  
main()