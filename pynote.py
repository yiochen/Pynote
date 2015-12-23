"""A small python 2.7 application for a CLI notebook"""
import sqlite3
import types
import os
import json
from debug import *


def eraseFile(file):
    """erase all content in a file, move the read write head to beginning"""
    try:
        if file.closed:
            perror("file closed, cannot be opened")
        else:
            file.seek(0)
            file.truncate()
    except IOError:
        perror("Cannot erase the file content")


# format of config
# name and value seperated by :
# each parameter in a line
if __name__ == "__main__":
    """Create a new config file if not exist"""
    initDebug(VERBOSE)
    config = {}
    try:
        configfile=None
        configfile = open("./pynoteConfig.info", "r+")
        pdebug(configfile)
        getKey = lambda line: line.split("#")[0] or "emptykey"
        getVal = lambda line: line.split("#")[1] or "none"
        pdebug(config)
        pdebug(configfile)
        text=configfile.read()
        pdebug(text)
        config=json.loads(text)
        # config.update({getKey(line):getVal(line) for line in configfile.readlines()})
        pdebug(config)
    except IOError:
        print "Configfile reading error, creating default config file at current directory"
        if configfile.__class__ == types.FileType:
            # if the file is already opened, close it
            configfile.close()
        # create a config file in cwd
        configfile = open("./pynoteConfig.info", "w")
        config={"notebooks":[]}
        configfile.write(json.dumps(config))

    #if notebooks list is empty
    if not config["notebooks"]:
        # the config file doesn't contain information about the database
        name = raw_input("Enter the name of the database")
        path = raw_input("Enter the path of the database, will create one if not exist: ")
        eraseFile(configfile)
        config["notebooks"].append({"name":name,"path":os.path.abspath(path)})
        configfile.write(json.dumps(config))

    configfile.close()
    pinfo("closed config file")
