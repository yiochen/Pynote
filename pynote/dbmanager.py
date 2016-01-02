"""This module contain some low level database access"""
import sqlite3
from datetime import date, datetime
from debug import *

def openNotebook(path):
    """
    open a notebook,
    if the notebook doesn't exist,
    create a sqlite file at the path
    return the sqlite3 connection object
    """
    try:
        conn=sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    except sqlite3.OperationalError:
        perror("Error connecting the notebook database at %s"%(path,))
        quit()


    c=conn.cursor()
    # create NOTES table
    c.execute('''CREATE TABLE  IF NOT EXISTS `NOTES` (
	        `note`	TEXT NOT NULL,
	        `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            'date'  timestamp NOT NULL
            );''')
    # create TAGS table
    c.execute('''CREATE TABLE  IF NOT EXISTS `TAGS` (
	        `name`	TEXT NOT NULL,
	        `note_id`	INTEGER NOT NULL,
	        FOREIGN KEY(`note_id`) REFERENCES NOTES(id)
            );''')
    conn.commit()
    return conn


def closeNotebook(conn):
    """ commit and close the sqlite3 connection"""
    conn.commit()
    conn.close()


def saveNote(conn,note,tags=[]):
    """ Save the notes in the database
    return the id of the last inserted note
    """
    id=conn.execute("INSERT INTO 'NOTES'('note','date') VALUES (?,?);",(note,datetime.now())).lastrowid
    tags=list(set(tags)) #remove duplicate tags
    for tag in tags:
        conn.execute("INSERT INTO 'TAGS'('name','note_id') VALUES (?,?);",(tag,id))
    conn.commit()

def getTagsById(conn, id):
    return conn.execute("SELECT name from TAGS WHERE note_id=?;",(id,)).fetchall()

def getNoteById(conn, id):
    result=conn.execute("SELECT id, note, date FROM NOTES WHERE id=?",(id,)).fetchone()
    return (result[0],result[1],result[2],getTagsById(conn,result[0]))

def getAllNotes(conn):
    """return all the notes in a list"""
    results=conn.execute("SELECT note, id, date FROM NOTES;").fetchall()
    # getTags=lambda id: conn.execute("SELECT name from TAGS WHERE note_id=?;",(id,)).fetchall()
    return [(id,note, date, getTagsById(conn,id)) for note, id,date in results]

def deleteNote(conn, id):
    """delete the note specified by the id"""
    conn.execute("DELETE FROM NOTES WHERE id=?;",(id,))
    conn.execute("DELETE FROM TAGS WHERE note_id=?;",(id,))
    conn.commit()

def removeTag(conn, id, tag):
    """remove a tag of a note"""
    conn.execute("DELETE FROM TAGS WHERE note_id=? AND name=?;",(id, tag))
    conn.commit()

def getNotesByTag(conn,tag):
    """get all the notes having this tag"""
    results=conn.execute("SELECT DISTINCT note_id FROM TAGS WHERE name=?;",(tag,)).fetchall()
    return [getNoteById(conn,row[0]) for row in results]
