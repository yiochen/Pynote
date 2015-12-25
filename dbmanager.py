"""This module contain some low level database access"""
import sqlite3
from datetime import date, datetime

def openNotebook(path):
    """
    open a notebook,
    if the notebook doesn't exist,
    create a sqlite file at the path
    return the sqlite3 connection object
    """
    conn=sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
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
    for tag in tags:
        conn.execute("INSERT INTO 'TAGS'('name','note_id') VALUES (?,?);",(tag,id))
    conn.commit()

def getAllNotes(conn):
    """return all the notes in a list"""
    results=conn.execute("SELECT note, id, date FROM NOTES;").fetchall()
    getTags=lambda id: conn.execute("SELECT name from TAGS WHERE note_id=?;",(id,)).fetchall()
    return [(id,note, date, getTags(id)) for note, id,date in results]
