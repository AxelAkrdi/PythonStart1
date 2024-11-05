from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)


app = QApplication([])


# Crear panel de preguntas
btn_OK = QPushButton('Responder')
lb_Question = QLabel('¡La pregunta más difícil del mundo!')


RadioGroupBox = QGroupBox("Opciones de respuesta")


rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # dos respuestas en la primera columna
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # dos respuestas en la segunda columna
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


# Crear un panel de resultados
AnsGroupBox = QGroupBox("Resultado de prueba")
lb_Result = QLabel('¿Es correcto o no?') # El texto de “Correcto” o “Incorrecto” estará aquí
lb_Correct = QLabel('¡Aquí estará la respuesta!') # el texto de respuesta correcta estará aquí 


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# Colocar todos los widgets en la ventana:
layout_line1 = QHBoxLayout() # pregunta
layout_line2 = QHBoxLayout() # opciones de respuesta o resultado de prueba
layout_line3 = QHBoxLayout() # botón de “Responder”


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Colocar ambos paneles en la misma línea; uno estará escondido y el otro será mostrado:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide() # Ya hemos visto este panel; vamos a esconderlo y ver cómo quedó el panel de respuestas 


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # el botón debería ser grande
layout_line3.addStretch(1)


# Ahora vamos a colocar las líneas que hemos creado una debajo de la otra:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # los espacios entre el contenido


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Tarjeta de memoria')
window.show()


app.exec()
