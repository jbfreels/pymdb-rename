import yaml
import json

class Config:
  #movie_format = None

  def __init__ (self, path="config.yml"):

    with open (path, 'r') as yml:
      self.yaml = yaml.load (yml, Loader=yaml.Loader)
      self.__dict__.update (self.yaml)
    
  def __str__ (self):

    return json.dumps(self.yaml)

config = Config ()