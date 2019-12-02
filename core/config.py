import yaml

with open ("config.yml", 'r') as yml:
  config = yaml.load (yml, Loader=yaml.Loader)
