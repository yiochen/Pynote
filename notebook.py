"""Provide functionalities for high level notebook access"""
import os
from dbmanager import *
from debug import *
from clitool import *

def getNotebook(path):
    """Open or create a notebook at the given path"""
    return Notebook(openNotebook(formatPath(path)))

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
        if type(tag) is str:
            self.tagBuff+=[tag]
        else:
            if type(tag) is list:
                self.tagBuff+=tag
            else:
                perror("Error processing tag, the argument must be a string or a list of strings")

    def commit(self):
        """flush the note into notebook"""
        if self.buffer:
            saveNote(self.dbconn, self.buffer, self.tagBuff)
            pinfo("Successfully saved note")
        self.buffer=""
        self.tagBuff=[]

    def printAllNotes(self):
        results=getAllNotes(self.dbconn)
        if results:
            print "\n\n".join([
            "%s\n%s\n%s"%(str(item[2]),str(item[1])," ".join([str(tag[0]) for tag in item[3]]))
             for item in results])
        else:
            print "No notes saved in this notebook"

    def __close(self):
        self.dbconn.close()

    def __rep__(self):
        results=getAllNotes(conn)
        return "\n".join(results)

    def __del__(self):
        self.__close()
