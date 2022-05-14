import requests

class Facts:
  def __init__(self):
    '''
      This function stores the API url for cat facts
      arg: self
      return: none
    '''
    self.api_url = "https://catfact.ninja/fact?max_length=80"
    
  def get(self):
    '''
      This function pulls data about cats from the website
      arg: self
      return: req
    '''
    req = requests.get(self.api_url)
    return req

  def canvas(self):
    '''
      This function sets up the canvas for the image and text to be printed on
    arg: self
    return: none
    '''
    self.canvas= canvas
    
         
       

 