#   Pynote - A Simple CLI Notebook
This project is in the inital stage of development, it is not usable yet  
##  Overview  
This is a simple python application for taking some quick note in terminal.
Once called, it will look for a configuration file called __*pynoteConfig.info*__ under
current user's home directory. If the configuration file doesn't exist. It will
create one in the user's home directory. Configuration file should contain
absolute path for the notebooks in the system, the first one being the directory
of the default notebook.  
## Usage  

    python pynote.py [-n|s notebook] [message]

#### • parameters  
__-n notebook__ This will create a **n**ew notebook in the given path. The name of the file will be used as the name of the notebook. Notebook names should be unique for all the notebooks in the system.  
example:

    python pynote.py -n /user/new_notebook

__-s notebook__ This will **s**elect a notebook for inserting the note  
> **Note** You only need to specify the name of the notebook when you use -s. But specifying the path to the notebook will work too. Error will be reported if the notebook cannot be found.  

__message__ If message is given as parameter, then the message will be saved to a chosen notebook, and the program will exit. If message is empty, you will enter interactive mode, in which you can do more advanced stuff other than inserting notes.    

> **Note** If -n and -s are not used, but __message__ is present, note will be saved in the default notebook, otherwise, it will be saved in the selected notebook.

example:  

    python pynote.py -n ./mynotebook This is my first note.

> **Note** Be careful that the notebook path cannot contain any space, if there is space, you need to use escape code **%20** to represent it

#### • configuration file
If the __*pynoteConfig.info*__ cannot be found under user's home directory, it will create one. If default notebook is not specified, user will be prompt to enter the path to create a notebook. Notebooks are actually sqlite3 database with predefined column names. It is not advised to edit the configuration file directly, however following is the format of it for development purpose. You can see that it is in JSON format  

    {
        "notebooks":[
            {"my_default_notebook":"/user/notebook1"},
            {"another notebook":"/user/note"},
            {"cooking_notebook":"/user/cooking/cookbook"},
        ]
    }
