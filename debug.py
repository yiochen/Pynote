NONE=0
ERROR=1
WARNING=2
DEBUG=3
VERBOSE=4
__debugLevel=0
def initDebug(level):
    global __debugLevel
    __debugLevel=level or NONE
    print __debugLevel

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
