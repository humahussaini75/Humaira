from PyQt4 import QtGui
import sys
#===============================================================================
# MyEditableTextBox-  
#===============================================================================
class MyEditableTextBox(QtGui.QLineEdit):
#|-----------------------------------------------------------------------------|
# Constructor  
#|-----------------------------------------------------------------------------|

    def __init__(self,*args):
        #*args to set parent
        QtGui.QLineEdit.__init__(self,*args)

#|-----------------------------------------------------------------------------|
# focusOutEvent :- 
#|-----------------------------------------------------------------------------|
    def focusOutEvent(self, *args, **kwargs):
        text = self.text()
        self.setText(text.upper())
        return QtGui.QLineEdit.focusOutEvent(self, *args, **kwargs)
        
        
#|--------------------------End of focusOutEvent--------------------------------|
#|-----------------------------------------------------------------------------| 
# keyPressEvent
#|-----------------------------------------------------------------------------|
    def keyPressEvent(self, event):
        if not self.hasSelectedText():
            pretext = self.text()
            self.setText(pretext.upper())
        return QtGui.QLineEdit.keyPressEvent(self, event)

#|--------------------End of keyPressEvent-------------------------------------|

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    lay = QtGui.QHBoxLayout()
    w.setLayout(lay)
    le1 = MyEditableTextBox()
    lay.addWidget(le1)
    le2 = MyEditableTextBox()
    lay.addWidget(le2)
    w.show()
    sys.exit(app.exec_())