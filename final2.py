import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class Window(QMainWindow):

	def __init__(self, parent=None):

		super(Window, self).__init__(parent)
		self.setGeometry(100,100,600,500)
		self.setWindowTitle("ROI")
		self.rubber_widget = RubberBandClass(self) 
		self.setCentralWidget(self.rubber_widget) 
		self.AddAction()
		self.AddMenu()
		self.AddToolBar()
		self.rgb = [] 		

	def AddToolBar(self):

		self.toolBar = self.addToolBar('Main')
		self.toolBar.addAction(self.openAction)
		self.toolBar.addAction(self.select)
		self.toolBar.addAction(self.printvalues)
		self.toolBar.show()


	def AddMenu(self):

		self.fileMenu = QMenu("&File", self)
		self.fileMenu.addAction(self.openAction)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.exitAction)

		self.menuBar().addMenu(self.fileMenu)

	def AddAction(self):

		self.openAction = QAction("&Open", self, shortcut="Ctrl+O", triggered=self.open_file)
		self.exitAction = QAction("&Exit", self, shortcut="Ctrl+Q", triggered=self.close)
		self.select = QAction('Select_ROI', self, triggered=self.select_roi)
		self.printvalues = QAction('Save', self, triggered=self.print_values)

	def print_values(self):

		for i in range(self.rubber_widget.xmin, self.rubber_widget.xmax):
			self.new = []
			for j in range(self.rubber_widget.ymin, self.rubber_widget.ymax):

			#	print("pixel:(" + str(i) + ","+ str(j) + ") - " + str(QColor(self.image_pix.pixel(i,j)).getRgb()) );
				self.new.append(QColor(self.image_pix.pixel(i,j)).getRgb()[:-1])
			self.rgb.append(self.new)
		print(self.rgb)


	def select_roi(self):
		
		if self.rubber_widget.image_open:
			self.rubber_widget.select_on = not self.rubber_widget.select_on
			print(self.rubber_widget.select_on)

	def open_file(self):	

		fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
		if fileName:
			image = QImage(fileName)
			if image.isNull():
				QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
				return
			self.image_pix = image
			#QPixmap.fromImage(image)
			self.rubber_widget.setPixmap(QPixmap.fromImage(image))
			self.rubber_widget.image_open = True


class RubberBandClass(QLabel):
	"""docstring for Window"""
	def __init__(self,parent):

		super(RubberBandClass, self).__init__(parent)
		#QLabel.__init__(self, parent)
		self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
		self.select_on = False
		self.image_open = False
		self.xmin = 0
		self.xmax = 0
		self.ymin = 0
		self.ymax = 0
		self.origin = QPoint()

	def mousePressEvent(self, event):

		if self.select_on:
			if event.button() == Qt.LeftButton:

				self.origin = QPoint(event.pos())
				self.rubberBand.setGeometry(QRect(self.origin, QSize()))
				self.rubberBand.show()

	def mouseMoveEvent(self, event):

		if self.select_on:
			if not self.origin.isNull():
				self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

	def mouseReleaseEvent(self, event):

		if self.select_on:
			if event.button() == Qt.LeftButton:
				self.endpoint = QPoint(event.pos())
				self.xmin, self.xmax = min(self.origin.x(), self.endpoint.x()), max(self.origin.x(), self.endpoint.x())				
				self.ymin, self.ymax = min(self.origin.y(), self.endpoint.y()), max(self.origin.y(), self.endpoint.y())				
				print(self.origin)
				print(event.pos())

				#self.rubberBand.hide()

	#def close_app(self):




if __name__ == '__main__':

    app = QApplication(sys.argv)
    # select_on = False
    window = Window()
    window.show()
    sys.exit(app.exec_())