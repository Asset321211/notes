from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout

import json


app = QApplication([])

notes = {
    'Добро пожаловать!' : {
        'текст' : 'Это самое лучшее приложение для заметок в мире!',
        'теги' : ['добро', 'инструкция']
    }
}
with open('notes_data.json','w') as file:
    json.dump(notes,file)


notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900,600)




list_notes  = QListWidget()
list_notes_label = QLabel('Список заметок')

button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')




field_tag = QLineEdit(' ')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label= QLabel('Список тегов')



layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)



col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1,stretch=2)
layout_notes.addLayout(col_2,stretch=1)
notes_win.setLayout(layout_notes)




def show_note():
    key = list_notes.selectedItems()[0].txt()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])




list_notes.itemClicked.connect(show_note)



notes_win.show()

with open('notes_data.json','r') as file:
    notes = json.load(file)
list_notes.addItems(notes)

app.exec_()









