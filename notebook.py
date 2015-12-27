"""Provide functionalities for high level notebook access"""

from dbmanager import *

def getNotebook(path):
    """Open or create a notebook at the given path"""
    pass #for now

def notebookExist(path):
    """check if the notebook exist in the file system"""
    pass #for now

class Notebook:
    """Class that encapsulates sqlite database for a notebook,
    providing high level functionalities for notebook access.
    The database should be created already.\n
    You shouldn't call the constructor to create a Notebook instance directly.
    Instead, you should use getNotebook function which will check the existance
    of the notebook file in the system.
    """
    def __init__(self, conn):
        self.dbconn=conn
        self.buffer=""
        self.tagBuff=[]

    def write(self, line):
        self.buffer+=(str(line)+"\n")

    def addTag(self, tag):
        """add tags to the current note, you can pass in a single string or a list of strings"""
        pass

    def commit(self):
        """flush the note into notebook"""
        pass

    def __rep__(self):
        pass
