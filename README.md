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

    $ python pynote.py [-n|s notebook] [message] [-t tags] [-l (notebook)]

#### • parameters  
__-n --new notebook__ This will create a **n**ew notebook in the given path. The name of the file will be used as the name of the notebook. Notebook names should be unique for all the notebooks in the system.  
example:

    $ python pynote.py -n /user/new_notebook

__-s --select notebook__ This will **s**elect a notebook for inserting the note  
> **Note** You only need to specify the name of the notebook when you use -s. But specifying the path to the notebook will work too. Error will be reported if the notebook cannot be found.  

__message__ If message is given as parameter, then the message will be saved to a chosen notebook, and the program will exit. If message is empty, you will enter interactive mode, in which you can do more advanced stuff other than inserting notes.    

> **Note** If -n and -s are not used, but __message__ is present, note will be saved in the default notebook, otherwise, it will be saved in the selected notebook.

example:  

    $ python pynote.py -n ./mynotebook This is my first note.

> **Note** Be careful that the notebook path cannot contain any space, if there is space, you need to use escape code **%20** to represent it

__-t --tag tags__  Tag the message, tags are separated by spaces  
example:

    $ python pynote.py This is my first note -t first "hello world" testing

__-l --list notebook__ List all the notes in the notebook. If notebook is not specified, list all the notebooks  

#### • configuration file
If the __*pynoteConfig.info*__ cannot be found under user's home directory, it will create one. If default notebook is not specified, user will be prompt to enter the path to create a notebook. Notebooks are actually sqlite3 database with predefined column names. It is not advised to edit the configuration file directly, however following is the format of it for development purpose. You can see that it is in JSON format  

    {
        "notebooks":[
            {"my_default_notebook":"/user/notebook1"},
            {"another notebook":"/user/note"},
            {"cooking_notebook":"/user/cooking/cookbook"},
        ]
    }

## How to use it as a custom command  
You may run the program after you pull it from this directory using

    $ python <path to pynote.py>/pynote.py [arguments]

But if you want to save some typing and run it as a custom command, it is actually very easy to do. You just need to make a alias.  
On Linux, do  

    $ echo "alias pynote='python <path_to_pynote.py>/pynote.py'"" >> ~/.bash_aliases

 you should change the <path_to_pynote> to the absolute path of the repository directory. After that, restart the terminal and you will be able to do something like

    $ pynote See, I can just run pynote -t alias "custom command"
