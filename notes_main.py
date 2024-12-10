from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


import json


app = QApplication([])


'''Notas in json'''
notes = {
    "Mi Primera Nota" : {
        "texto" : "Skibidi Sigma Pomni",
        "etiquetas" : ["Skibidi", "Sigma", "My Little Pony"]
    }
}
with open("notes_data.json", "w") as file:
    json.dump(notes, file, ensure_ascii=False)




'''Interfaz de aplicación'''
#parámetros de la ventana de la aplicación
notes_win = QWidget()
notes_win.setWindowTitle('Notas inteligentes')
notes_win.resize(900, 600)


#widgets de la ventana de la aplicación
list_notes = QListWidget()
list_notes_label = QLabel('Lista de notas')


button_note_create = QPushButton('Crear nota') #aparece una ventana con el campo “Ingresar nombre de nota”
button_note_del = QPushButton('Eliminar nota')
button_note_save = QPushButton('Guardar nota')


field_tag = QLineEdit('')
field_tag.setPlaceholderText('Ingresar etiqueta…')
field_text = QTextEdit()
button_add = QPushButton('Añadir a nota')
button_del = QPushButton('Remover etiqueta de nota')
button_search = QPushButton('Buscar notas por etiqueta')
list_tags = QListWidget()
list_tags_label = QLabel('Lista de etiquetas')


#organizando los widgets por diseño
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
row_3.addWidget(button_add)
row_3.addWidget(button_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)


'''Funcionalidad de la aplicación'''
def show_note():
    #obtener el texto de la nota con el título resaltado y mostrarlo en el campo de editar
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["texto"])
    list_tags.clear()
    list_tags.addItems(notes[key]["etiquetas"])


'''Ejecutar la aplicación'''
#Procesamiento de evento de conexión
list_notes.itemClicked.connect(show_note)


#ejecutar la aplicación
notes_win.show()


with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)


app.exec_()
