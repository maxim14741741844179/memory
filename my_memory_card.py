#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QButtonGroup
from random import shuffle, choice
class Question():
    def __init__(self, t, r, f1, f2, f3,):
        self.question = t
        self.right_answer = r
        self.wronrg_answer1 = f1
        self.wronrg_answer2 = f2
        self.wronrg_answer3 = f3
question = []
question.append(Question('хто я', 
'зубенька михаил петрович', 
'Вспомнил геометрия *****', 
'ЛЯГУШКА', 
'ты кто такой я тебя не звал иди домой '))
question.append(Question('2 + 2 * 2 =', '6', '52', '42', '8'))
question.append(Question('с кем сражались РУСЫ', 
'с ящерами', 
'с римлянями', 
'с гречкой', 
'с квадроберами'))

def show_result():
    Radiobox.hide()
    Radiobox1.show()
    push.setText('следующий')
    print('ваш результат')
    print('всего вопросов', vim.score)
    print('правильных ответов',vim.total)
    print('рейтинг',vim.score/vim.total*100,'%')
def show_question():
    Radiobox1.hide()
    Radiobox.show()
    push.setText('распили меня болгаркой')
    Radiobox2.setExclusive(False)
    bro1.setChecked(False)
    bro2.setChecked(False)
    bro3.setChecked(False)
    bro4.setChecked(False)
    Radiobox2.setExclusive(True)
def start_test():
    if push.text() == 'распили меня болгаркой':
        chekc_anc()
    elif push.text() == 'следующий':
        next_question()
def ask(q:Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wronrg_answer1)
    buttons[2].setText(q.wronrg_answer2)
    buttons[3].setText(q.wronrg_answer3)
    text.setText(q.question)
    text2.setText(q.right_answer)
    show_question()
def chekc_anc():
    if buttons[0].isChecked():
        text1.setText('НААААЙССС')
        vim.score += 1
        show_result()
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        text1.setText('фигня переделывай')
        show_result()

def next_question():
    vim.total += 1
    nextrand = choice(question)
    ask(nextrand)

app = QApplication([])
vim = QWidget()
vim.score = 0
vim.total = 0
vim.setWindowTitle('bruh')
vim.resize(1000, 900)

text = QLabel('это программа сдохни или умри')
Radiobox = QGroupBox('хто я')
bro1 = QRadioButton('зубенька михаил петрович')
bro2 = QRadioButton('Вспомнил геометрия *****')
bro3 = QRadioButton('ЛЯГУШКА')
bro4 = QRadioButton('ты кто такой я тебя не звал иди домой ')
push = QPushButton('распили меня болгаркой')

buttons = [bro1, bro2, bro3, bro4]
Radiobox2 = QButtonGroup()
Radiobox2.addButton(bro1)
Radiobox2.addButton(bro2)
Radiobox2.addButton(bro3)
Radiobox2.addButton(bro4)
text1 = QLabel('ДА-А')
Radiobox1 = QGroupBox('мда')
Radiobox1.hide()
text2 = QLabel('зубенька михаил петрович')
y4 = QVBoxLayout()
y4.addWidget(text1)
y4.addWidget(text2)
Radiobox1.setLayout(y4)

y1 = QVBoxLayout()
y2 = QVBoxLayout()
x1 = QHBoxLayout()
y1.addWidget(bro1)
y1.addWidget(bro3)
y2.addWidget(bro2)
y2.addWidget(bro4)
x1.addLayout(y1)
x1.addLayout(y2)
Radiobox.setLayout(x1)

y3 = QVBoxLayout()
x2 = QHBoxLayout()
x3 = QHBoxLayout()
x4 = QHBoxLayout()
x2.addWidget(text)
x3.addWidget(Radiobox)
x3.addWidget(Radiobox1)
x4.addWidget(push)
y3.addLayout(x2)
y3.addLayout(x3)
y3.addLayout(x4)
vim.setLayout(y3)

#ask(question[0])
next_question()
push.clicked.connect(start_test)
vim.show()
app.exec()
