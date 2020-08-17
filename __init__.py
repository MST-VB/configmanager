import json
import os

def createDirectory(name: str):
    if not os.path.exists(name): os.mkdir(name)

class Configuration:
    """
    Class for Configuration

    This class makes easier configurations to handle.

    developed by Manuel Staufer © 2020

    Methods
    ----------
    saveConfig()
    save this config

    setValue(key, value)
    set value from key

    getValue(key)
    return value from key

    getKey(value)
    return key from value

    getConfig()
    return the dictionary from config

    isExist(key)
    return True when exist or False when not exist

    """

    def __init__(self, name: str):
        self.config = {}
        self.name = name
        try:
            with open(self.name, "r") as file:
                self.config = json.load(file)
        except:
            self.saveConfig()

    def saveConfig(self):
        with open(self.name, "w") as file:
            json.dump(self.config, file)
            file.close()

    def setValue(self, key, value):
        self.config[key] = value

    def getValue(self, key):
        try:
            return self.config[key] if self.config[key] else False
        except KeyError:
            return False

    def getKey(self, value):
        try:
            for keys in self.config.keys():
                if value is self.getValue(keys):
                    return keys
        except KeyError:
            return False

    def getConfig(self):
        return self.config

    def isExist(self, key):
        try:
            return True if self.config[key] else False
        except KeyError:
            return False