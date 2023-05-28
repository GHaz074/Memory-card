#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QMessageBox,QRadioButton,QGroupBox,QButtonGroup
from random import shuffle

class InfoQuestion():
    def __init__(self,q_text,right,not_right1,not_right2,not_right3):
        self.q_text = q_text #str
        self.right = right #bool
        self.not_right1 = not_right1
        self.not_right2 = not_right2
        self.not_right3 = not_right3
questions = list()

q1 =  InfoQuestion('Вопрос№1', 'Правильный ответ', 'Ложь1', 'Ложь2', 'Ложь3')
questions.append(q1)

q2 =  InfoQuestion('Вопрос№2', 'Правильный ответ', 'Ложь1', 'Ложь2', 'Ложь3')
questions.append(q2)

q3 =  InfoQuestion('Вопрос№3', 'Правильный ответ', 'Ложь1', 'Ложь2', 'Ложь3')
questions.append(q3)


app = QApplication([])
mw = QWidget()

mw.setWindowTitle('MemoCard')
mw.move(0,0)
mw.resize(500,500)
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов:')

qrbutton1= QRadioButton('1')
qrbutton2= QRadioButton('2')
qrbutton3= QRadioButton('3')
qrbutton4= QRadioButton('4')

vq_line1 = QVBoxLayout()
vq_line2 = QVBoxLayout()
hq_line = QHBoxLayout()  
vq_line1.addWidget(qrbutton1) # два ответа в первый столбец
vq_line1.addWidget(qrbutton2)
vq_line2.addWidget(qrbutton3) # два ответа во второй столбец
vq_line2.addWidget(qrbutton4)

hq_line.addLayout(vq_line1)
hq_line.addLayout(vq_line2)

RadioGroupBox.setLayout(hq_line)


AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('прав ты или нет?')
lb_correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct)
AnsGroupBox.setLayout(layout_res)
button_ok = QPushButton('Ответить?')

layout_l1 = QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()
layout_l4 = QVBoxLayout()

layout_l1.addWidget(lb_Question)

layout_l2.addWidget(RadioGroupBox)  
layout_l2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()

layout_l3.addWidget(button_ok)

layout_l4.addLayout(layout_l1)
layout_l4.addLayout(layout_l2)
layout_l4.addLayout(layout_l3)
mw.setLayout(layout_l4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button_ok.setText('Следующий вопрос')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button_ok.setText('Ответить')
    SwitchersGroup = QButtonGroup()
    SwitchersGroup.addButton(qrbutton1)
    SwitchersGroup.addButton(qrbutton2)
    SwitchersGroup.addButton(qrbutton3)
    SwitchersGroup.addButton(qrbutton4)

    SwitchersGroup.setExclusive(False)
    qrbutton1.setChecked(False)
    qrbutton2.setChecked(False)
    qrbutton3.setChecked(False)
    qrbutton4.setChecked(False)
    SwitchersGroup.setExclusive(True)
buttons = [qrbutton1, qrbutton2, qrbutton3, qrbutton4]
score = 0
q_count = 0
def ask():
    global q_count
    q_count += 1
    shuffle(questions)
    act_q =  questions[0]

    shuffle(buttons)
    buttons[0].setText(act_q.right)
    buttons[1].setText(act_q.not_right1)
    buttons[2].setText(act_q.not_right2)
    buttons[3].setText(act_q.not_right3)

    lb_Question.setText(act_q.q_text)
    lb_correct.setText(act_q.right)


    show_question()
def check_result():
    if buttons[0].isChecked():
        lb_result.setText('Правильно')
        show_result()

    if buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        lb_result.setText('Неверно')
    show_result()
    button_ok.setText('Следующий вопрос')
def click_ok():
    if button_ok.text == 'Ответить?':
        check_result()
        global score
        score += 1
    
    else:
        ask()
ask()
button_ok.clicked.connect(click_ok)

mw.show()
app.exec()