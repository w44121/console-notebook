import sqlite3
import logging
import datetime
import os
import time

logging.basicConfig(format="%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s",
                     level=logging.DEBUG)

class DataBase:
    def __init__(self):
        self.PATH = "mydatabase.db"

    def _id(self, table_name):
        connect = sqlite3.connect(self.PATH)
        cursor = connect.cursor()
        request = "SELECT * FROM {}".format(table_name)
        cursor.execute(request)
        all_data = cursor.fetchall()
        count = len(all_data)
        connect.close()
        return count

    def create_table(self, name):
        connect = sqlite3.connect(self.PATH)
        cursor = connect.cursor()
        request = """CREATE TABLE IF NOT EXISTS {}
        (id INTEGER NOT NULL PRIMARY KEY,
        notetext TEXT,
        datetimetext TEXT)""".format(name)
        cursor.execute(request)
        connect.close()

    def write_note(self, note, table_name):
        connect = sqlite3.connect(self.PATH)
        cursor = connect.cursor()
        logging.info('write to table <{}> message: {}'.format(table_name, note))
        data_tuple = (table_name, self._id(table_name), note, str(datetime.datetime.now())[:19])
        request = "INSERT INTO {} VALUES({}, '{}', '{}')".format(*data_tuple)
        cursor.execute(request)
        connect.commit()
        connect.close()

    def edit_note(self, note_id, notebook, new_text):
        connect = sqlite3.connect(self.PATH)
        cursor = connect.cursor()
        request = "UPDATE '{}' SET notetext = '{}' WHERE id = {}".format(notebook, new_text, note_id)
        cursor.execute(request)
        request = "UPDATE '{}' SET datetimetext = '{}' WHERE id = {}".format(notebook, str(datetime.datetime.now())[:19], note_id)
        cursor.execute(request)
        connect.commit()
        connect.close()

    def delete_note(self, note_id, notebook):
        connect = sqlite3.connect(self.PATH)
        cursor = connect.cursor()
        request = "DELETE FROM '{}' WHERE id = {}".format(notebook, note_id)
        cursor.execute(request)
        connect.commit()
        connect.close()

    def delete_notebook(self, notebook):
        connect = sqlite3.connect(self.PATH)
        cursor = connect.cursor()
        request = "DROP TABLE IF EXISTS '{}'".format(notebook)
        cursor.execute(request)
        connect.commit()
        connect.close()

    def get_tables_names_from_database(self):
        connect = sqlite3.connect(self.PATH)
        cursor = connect.cursor()
        res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        names = []
        for name in res:
            names.append(name[0])
        return names

    def get_notes_from_table(self, table_name):
        connect = sqlite3.connect(self.PATH)
        cursor = connect.cursor()
        request = "SELECT * FROM '{}'".format(table_name)
        cursor.execute(request)
        notes = cursor.fetchall()
        connect.close()
        return notes
