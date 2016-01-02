"""A small python 2.7 application for a CLI notebook"""
import types
import os
import argparse
import json
from pynote.debug import *
from pynote.notebook import *
from pynote.notebooklist import *
from pynote.clitool import *

def initArgs():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group()
    group.add_argument("-n","--new",help="Create a new notebook at the path, filename will be used as notebook name")
    group.add_argument("-s","--select",help="Select a notebook to open by specifying notebook name")
    parser.add_argument("note",nargs="*", help="Your note content")
    parser.add_argument("-t","--tag", nargs="*", help="Tag your note, end with --")
    parser.add_argument("-l","--list",nargs="*", help="List the notes in the notebooks or list all the notebooks")
    return parser.parse_args()

# format of config
# name and value seperated by :
# each parameter in a line
if __name__ == "__main__":
    parser=initArgs()
    pdebug(parser)
    initDebug(VERBOSE)
    config = NotebookList()
    notepath=""

    if parser.new:
        (path, name)=os.path.split(parser.new)
        if config[name]:
            # the notebook already exist
            perror("the notebook %s already exist"%(name))
            choice=repeatedAsk("Do you want to use the old notebook? (Y/N)",["Y","N"])
            if choice.upper()=="Y":
                notepath=config[name]
                notebook=getNotebook(notepath)
            else:
                pinfo("exiting program")
                quit()
        else:
            notepath=formatPath(os.path.join(path,name))
            # try creating the notebook
            pdebug("creating the notebook at %s"%(notepath,))
            notebook=getNotebook(notepath)
            config[name]=notepath
            pinfo("the new notebook is called %s at %s"%(name, notepath))
            config.save()
    # #if notebooks list is empty
    # if not config["notebooks"]:
    #     # the config file doesn't contain information about the database
    #     print("Please enter the information of the default notebook")
    #     (path, name) = os.path.split(raw_input("Enter the path of your notebook: "))
    #     notepath=formatPath(os.path.join(path,name))
    #     config["notebooks"].append({"name":name,"path":notepath})
    #     pinfo("the new notebook is called %s at %s"%(name, notepath))
    #     __writeConfig(configfile, config)
    # configfile.close()
    # pinfo("Closed config file")
    if parser.select:
        notepath=config[parser.select]
        if not notepath:
            perror("The notebook named %s doesn't exist"%parser.select)
            quit()

    if parser.list is not None:
        if parser.list:
            #listing all the notes in the specified notebooks
            for tempnotebookname in parser.list:
                if config[tempnotebookname]:
                    print "-----%s-----"%(tempnotebookname,)
                else:
                    print "%s doesn't exist"%(tempnotebookname,)
                    continue

                tempnotebook=getNotebook(config[tempnotebookname])
                tempnotebook.printAllNotes()
                del tempnotebook
        else:
            #listing all the notebooks
            config.printAllNotebooks()


    if not notepath:
        # user doesn't specify which notebook to use, use the default notebook
        pinfo("using default notebook")
        defaultNotebook=config.getDefaultNotebook()
        if not defaultNotebook:
            choice=repeatedAsk("Default notebook doesn't exist, do you want to create one? (Y/N) ",["Y","N"])
            if choice=="Y":
                notepath=formatPath(raw_input("Enter the path of the notebook, the filename will be used as the notebook name: "))
                notebook=getNotebook(notepath)
                (dirpath, name)=os.path.split(notepath)
                config[name]=notepath
                config.save()
            else:
                pinfo("exiting program")
                quit()
        else:
            pdebug("default notebook is "+str(defaultNotebook))
            notepath=defaultNotebook["path"]
            notebook=getNotebook(notepath)
    if not notebook:
        # if notebook is still None, No idea what happen, quit the program
        pinfo("exiting program")
        quit()

    if parser.note:
        notebook.write(" ".join(parser.note))
    if parser.tag:
        notebook.addTag(parser.tag)
    notebook.commit()
    del notebook
