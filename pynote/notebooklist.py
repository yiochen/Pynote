"""Module for managing notebooks"""

from notebook import *
from clitool import *
from debug import *
import os
import json



class NotebookList:
    """Class that contain information of list of all the notebooks in the system"""
    # constants
    __CONFIG_PATH="~/pynoteConfig.info"

    def __init__(self):
        self.__configfilepath=formatPath(NotebookList._NotebookList__CONFIG_PATH)
        pdebug("config file path is %s"%(self.__configfilepath,))
        self.configfile=None
        self.config={"notebooks":[],}
        try:
            self.configfile=open(self.__configfilepath,"r+")
            pdebug("opened config file for for readwrite")
        except IOError:
            self.configfile=open(self.__configfilepath,"w")
            pdebug("created config file")
            self.configfile.close()
            self.configfile=open(self.__configfilepath,"r+")
            pdebug("opened the created config file for readwrite")
        finally:
            try:
                text=self.configfile.read()
                self.config.update(json.loads(text))
            except IOError:
                perror("Cannot read config file, terminating program")
                self.configfile.close()
                quit()
            except ValueError:
                pinfo("config file might be empty or contain invalid information, rewrite configfile")
                self.save()
            except AttributeError:
                perror("AttributeError")
                quit()

    def getDefaultNotebook(self):
        if len(self.config["notebooks"])>0:
            return self.config["notebooks"][0]
        else:
            return None

    def save(self):
        """erase all content in a file, move the read write head to beginning"""
        file=self.configfile
        try:
            if file.closed:
                perror("file closed, cannot be opened")
            else:
                file.seek(0)
                file.truncate()
                file.write(json.dumps(self.config))
                pdebug("finished writing config file")
        except (IOError, ValueError):
            perror("Cannot erase the file content")

    def printAllNotebooks(self):
        if self.config["notebooks"]:
            print "\n".join(["%s %s"%(item["name"].ljust(10),item["path"]) for item in self.config["notebooks"]])
        else:
            print "There is no notebooks"

    def __getitem__(self, key):
        result=[item for item in self.config["notebooks"] if item["name"]==key]
        if len(result)>0:
            return result[0]["path"]
        else:
            return None

    def __setitem__(self, key, value):
        if self[key]:
            self[key]["path"]=value
        else:
            self.config["notebooks"].append({"name":key,"path":value})

    def __del__(self):
        if self.configfile is not None and not self.configfile.closed:
            self.configfile.close()
