import dbcontroler
import notebook_menu

def main():
    DB = dbcontroler.DataBase()
    note_viewer = notebook_menu.NoteBookMenu()
    note_viewer.init_database(DB)
    note_viewer.show_notebook_menu()


if __name__ == "__main__":
    main()
