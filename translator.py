import sys
from PySide2 import QtWidgets
from ui_translator import Ui_MorseCode
#
class MainWindow(QtWidgets.QMainWindow):
    
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--'
}

    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MorseCode()
        self.ui.setupUi(self)
        self.configure_actions()

    ''' Configure Methods''' 
    
    def configure_actions(self):
        # Buttons Connection Signals
        self.ui.pushButton_dash.pressed.connect(lambda: self.dash_press())
        self.ui.pushButton_dot.pressed.connect(lambda: self.dot_press())
        self.ui.pushButton_space.pressed.connect(lambda: self.space_press())
        self.ui.pushButton_enter.pressed.connect(lambda: self.enter_press())
        self.ui.pushButton_backspace.pressed.connect(lambda: self.backspace_press())
        self.ui.pushButton_clear.pressed.connect(lambda: self.clear_press())

    ''' User Actions Methods '''    

    def translate(self, morse_code_str):
        result = ''
        morse_code = morse_code_str.split(' ')
        for code in morse_code:
            for char, morse in self.morse_dict.items():
                if morse == code:
                    result += char
        return result

    def clear_press(self):
        self.ui.output.setText("")
    def dot_press(self):
        self.ui.output.setText(f'{self.ui.output.text()}.')
    def dash_press(self):
        self.ui.output.setText(f'{self.ui.output.text()}-')
    def space_press(self):
        self.ui.output.setText(f'{self.ui.output.text()} ')
    def enter_press(self):
        self.ui.output.setText(self.translate(self.ui.output.text()))
    def backspace_press(self):
        self.ui.output.setText(self.ui.output.text().rstrip(self.ui.output.text()[-1]))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()