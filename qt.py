import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w = QWidget()

    QToolTip.setFont(QFont('SansSerif', 10))
        
    w.setToolTip('This is a <b>QWidget</b> widget')
        
    btn = QPushButton('Button',w)
    btn.setToolTip('This is a <b>QPushButton</b> widget')
    btn.resize(btn.sizeHint())
    btn.move(50, 50)       
        
    w.setGeometry(300, 300, 300, 200)
    w.setWindowTitle('Tooltips')    
    w.show()
    sys.exit(app.exec_())
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('Simple')
    # w.show()
    
    # sys.exit(app.exec_())
    