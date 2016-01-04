#   Pynote - A Simple CLI Notebook

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

    $ python pynote.py -n /home/new_notebook

> **Note** -n is followed by a path to the notebook. If the notebook exist, it will add this notebook to the configuration file. Otherwise it will try to create a notebook file at the given path. You can specify absolute path like /home/yiou/MyNotebook or relative path such as ./MyNotebook. You can also use "~" to represent user's home directory in linux and OS X.

> **Note** Be careful that the notebook path cannot contain any space, if there is space, you need to use escape code **%20** to represent it

__-s --select notebook__ This will **s**elect a notebook for inserting the note  

> **Note** -s should be followed only by the name of the notebook. It will not work with any path. If the notebook is not in the configuration file, the note will not be saved.




[//]: # ( __message__ If message is given as parameter, then the message will be saved to a chosen notebook, and the program will exit. If message is empty, you will enter interactive mode, in which you can do more advanced stuff other than inserting notes.  )

> **Note** If -n and -s are not used, but __message__ is present, note will be saved in the default notebook, otherwise, it will be saved in the selected notebook.

example:  

    $ python pynote.py -s mynotebook This is my first note.



__-t --tag tags__  Tag the message, tags are separated by spaces  
example:

    $ python pynote.py This is my first note -t first "hello world" testing

__-l --list notebook__ List all the notes in the notebook. If notebook is not specified, list all the notebooks  

#### • hidden argument  
__-d --debug__ This will turn on verbose printing. It's not meant for end users.   

#### • configuration file
If the __*pynoteConfig.info*__ cannot be found under user's home directory, it will create one. If default notebook is not specified, user will be prompt to enter the path to create a notebook. Notebooks are actually sqlite3 database with predefined column names. It is not advised to edit the configuration file directly, however following is the format of it for development purpose. You can see that it is in JSON format  

    {
        "notebooks":[
            {"my_default_notebook":"/home/notebook1"},
            {"another notebook":"/home/note"},
            {"cooking_notebook":"/home/cooking/cookbook"},
        ]
    }

## How to install it as a command line tool  
### Linux  
Just execute this install script under superuser mode. For example in ubuntu

    $ sudo ./install

Then you can run it like

    $ pynote -n ./mynotebook This is my first note.
### Windows  
Installing on Windows requires a little more work. You would need to convert the python code to executable first. This is done using a program called [py2exe][py2exe]. We have done the job so you can install and use it even without python installation. You can download a zip file from our [releases][windows release], unzip it, and add the path of the unzipped folder to system/user path.  
 If you want to generate the executable on you own. You can head over to [py2exe.org][py2exe], install it and run

    python setup.py py2exe

 at project root directory. A folder called "dist" will be generated. You can go ahead and add it to path variable.

 [py2exe]:  http://www.py2exe.org/
 [windows release]: https://github.com/yiochen/Pynote/releases
