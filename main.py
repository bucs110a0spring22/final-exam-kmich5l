import tkinter
from tkinter import *
import facts
import image
import urllib.request
from PIL import ImageTk,Image 


def screen():
  root = tkinter.Tk()
  canvas = Canvas(root, width = 750, height = 700) 
  root.wm_title("FUN CAT FACTS")
  line= facts.Facts()
  response = line.get()
  canvas.create_text(400, 50, text= ("Fact: " + response.json()["fact"]), fill="black", font=('Helvetica 11 normal'))
  canvas.pack()  
  

  
  
  urllib.request.urlretrieve("https://cataas.com/cat","cat.png")
  img = ImageTk.PhotoImage(Image.open("cat.png"))  
  canvas.create_image(65, 80, anchor=NW, image=img) 



  root.mainloop() 
def main():
  screen()

main()