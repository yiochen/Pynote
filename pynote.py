import sqlite3
import types

# format of config
# name and value seperated by :
# each parameter in a line
if __name__ == "__main__":
    """Create a new config file if not exist"""
    config = {"path":"/notebase.db"}
    try:
        configfile = open("pynoteConfig.info", "r+")
        getKey = lambda line: line.split("#")[0] or "emptykey"
        getVal = lambda line: line.split("#")[1] or "none"
        config = config.update({getKey(line):getVal(line) for line in configfile.readlines()})
    except IOError:
        print "Configfile reading error, creating default config file at current directory"
        if configfile.__class__ == types.FileType:
            configfile.close()
        # create a config file in cwd
        configfile = open("/pynoteConfig.info", "w")
        configfile.write("\n".join(["%s#%s"%(key, str(value)) for key, value in config.items()]))

    if config["path"] is None:
        # ready to write to the file
        filename = raw_input("Enter the path of the database, will create one if not exist: ")
        configfile.seek(0,2) #move to the end of the file
        configfile.write("path#%s\n" % filename)
    # finished reading and updating the config file, closing it
    configfile.close()
