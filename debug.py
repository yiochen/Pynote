""" A module for color coding debug messages """
NONE=0
ERROR=1
WARNING=2
DEBUG=3
VERBOSE=4
__debugLevel=0
def initDebug(level):
    global __debugLevel
    __debugLevel=level or NONE

def pdebug(message):
    if __debugLevel>=DEBUG:
        print "\033[94m%s%s\033[0m"%("DEBUG".ljust(10),str(message))

def pinfo(message):
    if __debugLevel>=VERBOSE:
        print "\033[92m%s%s\033[0m"%("INFO".ljust(10),str(message))

def pwarning(message):
    if __debugLevel>=WARNING:
        print "\033[93m%s%s\033[0m"%("WARNING".ljust(10), str(message))

def perror(message):
    if __debugLevel>=ERROR:
        print "\033[91m%s%s\033[0m"%("ERROR".ljust(10),str(message))

if __name__ == "__main__":
    """test printing"""
    initDebug(VERBOSE)
    pinfo("this is a info message")
    pdebug("this is a debug message")
    pwarning("this is a warning")
    perror("this is a error")
