import requests


class Image:
  def __init__(self):
    '''
      This function stores the API url for cat images
      arg: self
      return: none
    '''
    self.api_url = "https://cataas.com/cat"

  def get(self):
    '''
      This function pulls a random picture of a cat from the website
      arg: self
      return: req
    '''
    r = requests.get(self.api_url)
    data = r.json()
    return data
    
  def canvas(self):
    '''
      This function sets up the canvas for the image and text to be printed on
      arg: self
      return: none
    '''
    self.canvas = canvas
  