"""A small python 2.7 application for a CLI notebook"""
import types
import os
import argparse
import json
from debug import *
from notebook import *


# constants
__CONFIG_PATH="~/pynoteConfig.info"


def __eraseFile(file):
    """erase all content in a file, move the read write head to beginning"""
    try:
        if file.closed:
            perror("file closed, cannot be opened")
        else:
            file.seek(0)
            file.truncate()
    except IOError:
        perror("Cannot erase the file content")

def __writeConfig(file,config):
    """write the config into file, the original content is erased"""
    __eraseFile(file)
    try:
        file.write(json.dumps(config))
    except IOError:
        perror("Config file writing error")

def initArgs():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group()
    group.add_argument("-n","--new",help="Create a new notebook at the path, filename will be used as notebook name")
    group.add_argument("-s","--select",help="Select a notebook to open by specifying notebook name")
    parser.add_argument("note",nargs="*", help="Your note content")
    parser.add_argument("-t","--tag", nargs="*", help="Tag your note, end with --")
    return parser.parse_args()

# format of config
# name and value seperated by :
# each parameter in a line
if __name__ == "__main__":
    """Create a new config file if not exist"""
    parser=initArgs()
    pdebug(parser)
    initDebug(VERBOSE)
    config = {"notebooks":[]}
    notepath=""
    __CONFIG_PATH=os.path.expanduser(__CONFIG_PATH)
    try:
        configfile=None
        #try open and read the config file
        configfile = open(__CONFIG_PATH, "r+")
        pdebug(configfile)
        text=configfile.read()
        pdebug(text)
        config.update(json.loads(text))
    except (IOError,ValueError):
        print "Configfile reading error, creating default config file at home directory"
        if configfile.__class__ == types.FileType and not configfile.closed:
            # if the file is already opened, close it
            configfile.close()
        # create a config file in cwd
        configfile = open(os.path.abspath(__CONFIG_PATH), "w")
        pinfo( "Configfile created at %s"%(os.path.abspath(__CONFIG_PATH),))
        config={"notebooks":[]}
    if parser.new:
        (path, name)=os.path.split(parser.new)
        notepath=os.path.abspath(os.path.join(path,name))
        config["notebooks"].append({"name":name,"path":notepath})
        pinfo("the new notebook is called %s at %s"%(name, notepath))
        __writeConfig(configfile, config)
    #if notebooks list is empty
    if not config["notebooks"]:
        # the config file doesn't contain information about the database
        print("Please enter the information of the default notebook")
        (path, name) = os.path.split(raw_input("Enter the path of your notebook: "))
        notepath=os.path.abspath(os.path.join(path,name))
        config["notebooks"].append({"name":name,"path":notepath})
        pinfo("the new notebook is called %s at %s"%(name, notepath))
        __writeConfig(configfile, config)
    configfile.close()
    pinfo("Closed config file")
    if parser.select:
        try:
            notepath=[record["path"] for record in config["notebooks"] if record["name"]==parser.select].pop()
        except IndexError:
            perror("The notebook named %s doesn't exist"%parser.select)
            quit()
    if not notepath:
        notepath=config["notebooks"][0]["path"]
        pinfo("using default notebook at %s"%(notepath,))
    notebook=Notebook(getNotebook(notepath))
    if parser.note:
        notebook.write(" ".join(parser.note))
    if parser.tag:
        notebook.addTag(parser.tag)
    notebook.commit()
    notebook.close()

    # note=raw_input("enter your note: ")
    # tag=raw_input("enter tags, seperated by space: ")
    # notebook.write(note)
    # notebook.addTag(tag.split())
    # notebook.commit()
    # notebook.close()
