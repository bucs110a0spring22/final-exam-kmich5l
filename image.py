import requests
import urllib.request

class Image:
  def __init__(self):
    '''
      This function stores the API url for cat images
      arg: self
      return: none
    '''
    self.api_url= "https://cataas.com/cat"

  def get(self):
    '''
      This function pulls a random picture of a cat from the website
      arg: self
      return: req
    '''
   # req = requests.get(self.api_url)
    req= urllib.request.urlretrieve("https://cataas.com/cat","cat.png")
    return req

  def response(self):
    '''
		  prints the RAW last response from the API
		  arg: self: instance of class
	  	return: RAW last response from the API
  	'''
    r = self.get()
    response = r.json()
    return response
    
  def canvas(self):
    '''
      This function sets up the canvas for the image and text to be printed on
    arg: self
    return: none
    '''
    self.canvas= canvas
    