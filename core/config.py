import json
import os

import yaml


class Config:

    def __init__(self):

        try:
            path = os.path.join(
                os.path.dirname(__file__),
                "../config.yml"
            )
            if not os.path.exists(path):
                raise IOError
        except IOError as e:
            print("error locating config YML")
            exit(1)

        with open(path, 'r') as yml:
            self.yaml = yaml.load(yml, Loader=yaml.Loader)
            self.__dict__.update(self.yaml)

    def __str__(self):

        return json.dumps(self.yaml)


config = Config()
