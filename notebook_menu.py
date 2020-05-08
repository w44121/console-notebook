import os

class NoteBookMenu:
    def init_database(self, database):
        self.database = database

    def show_notebook_menu(self):
        os.system("clear")
        print("note book menu\n")
        if len(self.database.get_tables_names_from_database()) == 0:
            print("you have 0 notebooks")
        else:
            print("you have {} notebooks!!!".format(len(self.database.get_tables_names_from_database())))
            print("{:<3}|{}".format("id", "notebook"))
            for id, notebook in enumerate(self.database.get_tables_names_from_database()):
                print("{:<3}|{}".format(id, notebook))
            print("\n")
        self._notebook_menu()

    def _notebook_menu(self):
        print("C -> to cerate new notebook")
        print("Name -> to open notebook")
        print("D Name -> to delete notebook")
        print("E -> to exit from terminal")
        choice = input()
        if choice in ["c", "C"]:
            self._create_new_notebook()
        if choice in ["e", "E"]:
            os.system("exit")
        if choice in self.database.get_tables_names_from_database():
            self._open_notebook(choice)
        if choice.split(" ")[0] in ["d", "D"]:
            print("deleting")
            self.database.delete_notebook(choice.split(" ")[1])
            self.show_notebook_menu()

    def _open_notebook(self, notebook):
        os.system("clear")
        print("curent notebook:", notebook, "\n")
        if len(self.database.get_notes_from_table(notebook)) == 0:
            print("you have 0 notes in {}".format(notebook))
        else:
            print("{:<3}|{:<50}|{}\n".format("N", "text", "date"))
            for note in self.database.get_notes_from_table(notebook):
                print("{:<3}|{:<50}|{}".format(*note))
        print("\n")
        self._note_menu(notebook)

    def _create_new_notebook(self):
        print("select name for new notebook:")
        table_name = input()
        self.database.create_table(table_name)
        self.show_notebook_menu()

    def _note_menu(self, notebook):
        curent_notebook = notebook
        print("C -> to create new note")
        print("R id -> to redacting note")
        print("D id -> to delete note")
        print("B -> to back in notebook menu")
        print("E -> to exit from terminal")
        choice = input()
        if choice.split(" ")[0] in ["r", "R"]:
            self._edit_note(choice.split(" ")[1], curent_notebook)
        if choice.split(" ")[0] in ["d", "D"]:
            self._delete_note(choice.split(" ")[1], curent_notebook)
        if choice in ["c", "C"]:
            self._create_new_note(curent_notebook)
        if choice in ["b", "B"]:
            self.show_notebook_menu()
        if choice in ["e", "E"]:
            os.system("exit")

    def _create_new_note(self, notebook):
        print("create new note in {} notebook".format(notebook))
        note = input()
        self.database.write_note(note, notebook)
        self._open_notebook(notebook)

    def _edit_note(self, id, notebook):
        print("Write new text for this note:")
        new_text = input()
        self.database.edit_note(id, notebook, new_text)
        self._open_notebook(notebook)

    def _delete_note(self, id, notebook):
        self.database.delete_note(id, notebook)
        self._open_notebook(notebook)
