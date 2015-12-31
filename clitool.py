""" Some utility codes for easy command line interface development"""
import os

def repeatedAsk(question, answers, upper=True, limited=True, default=None):
    """repeatedly ask a user question, until user answer something in the [answers]
    question: A string of question to ask user.
    answers: A list of all the possible answers.
    upper: If true, the user's input will be converted to uppercase before comparing,
    limited: If set to true, the returned answer will always be in the [answers],
            If set to false, it will return the default answer if user answer something not in [answers].
    default: The default answer."""
    answer=default

    userin=raw_input(question)
    if upper:
        userin=userin.upper()
    while userin not in answers:
        if not limited:
            return answer
        userin=raw_input(question)
        if upper:
            userin=userin.upper()
    return userin

def formatPath(path):
    """expanduser and abspath a path string"""
    result=path
    if "~" in path:
        result=os.path.expanduser(path)
    return os.path.abspath(result)
