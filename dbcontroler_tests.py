import dbcontroler
from random import choice

# idea
# id | text | data-time

text_list = [
"drink water",
"watch films",
"play video games",
"learn python",
"work on site",
"some sport" ]

def gen_data(count):
    data_list = []
    for i in range(count):
        text = choice(text_list)
        note = text
        data_list.append(note)
    return data_list

# config
table_name = "job"

DB = dbcontroler.DataBase()
DB.create_table(table_name)
for note in gen_data(10):
    DB.write_note(note, table_name)

print(DB.get_tables_names_in_database())

print(DB.get_notes_from_table(table_name))
