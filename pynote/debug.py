""" A module for color coding debug messages """

from pynote import SYSTEM

NONE=0
ERROR=1
WARNING=2
DEBUG=3
VERBOSE=4


COLOR_BLUE="\033[94m"
COLOR_GREEN="\033[92m"
COLOR_YELLOW="\033[93m"
COLOR_ORANGE="\033[91m"
COLOR_RESET="\033[0m"

CINFO=""
CDEBUG=""
CWARNING=""
CERROR=""
CRESET=""

__debugLevel=0
def initDebug(level):
    global __debugLevel
    __debugLevel=level or NONE
    if SYSTEM=="Linux":
        # sorry mac and windows user. No color for you.
        global CINFO, CDEBUG, CWARNING, CERROR,CRESET
        CINFO=COLOR_GREEN
        CDEBUG=COLOR_BLUE
        CWARNING=COLOR_YELLOW
        CERROR=COLOR_ORANGE
        CRESET=COLOR_RESET


def pdebug(message):
    if __debugLevel>=DEBUG:
        print CDEBUG+"%s%s"%("DEBUG".ljust(10),str(message))+CRESET

def pinfo(message):
    if __debugLevel>=VERBOSE:
        print CINFO+"%s%s\033[0m"%("INFO".ljust(10),str(message))+CRESET

def pwarning(message):
    if __debugLevel>=WARNING:
        print CWARNING+"%s%s\033[0m"%("WARNING".ljust(10), str(message))+CRESET

def perror(message):
    if __debugLevel>=ERROR:
        print CERROR+"%s%s\033[0m"%("ERROR".ljust(10),str(message))+CRESET

if __name__ == "__main__":
    """test printing"""
    initDebug(VERBOSE)
    pinfo("this is a info message")
    pdebug("this is a debug message")
    pwarning("this is a warning")
    perror("this is a error")
