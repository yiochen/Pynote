"""A small python 2.7 application for a CLI notebook"""
import sqlite3
import types
import os
from debug import *

# format of config
# name and value seperated by :
# each parameter in a line
if __name__ == "__main__":
    """Create a new config file if not exist"""
    initDebug(VERBOSE)
    config = {"path":"./notebase.db"}
    try:
        configfile=None
        configfile = open("./pynoteConfig.info", "r+")
        getKey = lambda line: line.split("#")[0] or "emptykey"
        getVal = lambda line: line.split("#")[1] or "none"
        pdebug(config)
        config.update({getKey(line):getVal(line) for line in configfile.readlines()})
        pdebug(config)
    except IOError:
        print "Configfile reading error, creating default config file at current directory"
        if configfile.__class__ == types.FileType:
            # if the file is already opened, close it
            configfile.close()
        # create a config file in cwd
        configfile = open("./pynoteConfig.info", "w")
        configfile.write("\n".join(["%s#%s"%(key, str(value)) for key, value in config.items()]))

    if config["path"] is None:
        # the config file doesn't contain information about the database
        path = raw_input("Enter the path of the database, will create one if not exist: ")
        configfile.seek(0,2) #move to the end of the file
        configfile.write("path#%s\n" % path)
        config["path"]=path
    # finished reading and updating the config file, closing it
    configfile.close()
    pinfo("closed config file, the path is %s"%(config["path"],))
