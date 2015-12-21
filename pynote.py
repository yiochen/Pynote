import sqlite3

# format of config
# name and value seperated by :
# each parameter in a line
if __name__ == "__main__":
    """Create a new config file if not exist"""
    configfile = open("pynoteConfig", "r+")
    config = configfile.readlines()
    filename = ""
    if len(config) == 0:
        # ready to write to the file
        filename = raw_input("Enter the path of the database, will create one if not exist: ")
        configfile.write("path:%s\n" % filename)
        configfile.close()
    else:
        # read filename

