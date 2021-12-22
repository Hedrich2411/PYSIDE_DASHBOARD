import sys
from PySide6.QtCore import QIODevice, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QHBoxLayout,QMainWindow
from PySide6.QtSerialPort import QSerialPort
from circular_bar import CircularBar
from ui_interface import Ui_MainWindow
import pyqtgraph as pg



class Interface(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #preconfig
        self.setupUi(self)
        self.setWindowIcon(QIcon("img/micro.png"))
        self.setWindowTitle("AVR-PYSIDE")
        self.create_widget()

        #Serial init
        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)
        self.serial.setPortName("COM1")

        #Slots
        self.btn_connect.clicked.connect(self.start_connection)
        self.btn_disconnect.clicked.connect(self.stop_connection)
        self.serial.readyRead.connect(self.update_widgets)
        self.slider_velocidad.sliderReleased.connect(self.change_velocidad)
        self.btn_left.clicked.connect(self.left_direction)
        self.btn_right.clicked.connect(self.right_direction)
        self.btn_on.clicked.connect(self.button_on)
        self.btn_on_2.clicked.connect(self.button_off)

    def create_widget(self):

        #Create graphic 
        self.w_temp.setBackground(background = None)
        self.listX = [x for x in range(100)]
        self.listY = [y for y in range(100)]
        self.w_temp.setTitle("<pan style=\"color:#000000;font: 11pt 'Bell MT'\">Monitoreo de Humedad</span>")
        self.w_temp.setLabel("left","<pan style=\"color:#000000;font: 11pt 'Bell MT'\">Grados (ºC)</span>")
        self.w_temp.setLabel("bottom","<pan style=\"color:#000000;font: 11pt 'Bell MT'\">Muestreo</span>")

        #create circular progress bar
        self.circular_progress_bar = CircularBar(200,200)
        self.circular_layout = QHBoxLayout()
        self.circular_layout.setAlignment(Qt.AlignCenter)
        self.circular_layout.addWidget(self.circular_progress_bar)
        self.circular_progress.setLayout(self.circular_layout)

        #Init widgets
        self.btn_disconnect.setDisabled(True)


    def start_connection(self):
        self.serial.open(QIODevice.ReadWrite)
        self.btn_connect.setDisabled(True)
        self.btn_disconnect.setDisabled(False)

    def stop_connection(self):
        self.serial.close()
        self.btn_connect.setDisabled(False)
        self.btn_disconnect.setDisabled(True)

    def update_widgets(self):
        if not self.serial.canReadLine(): return

        #recieve data
        rx = str(self.serial.readLine(),'utf-8').replace('\n','')
        data = rx.split('-')

        #update_graph
        self.listY = self.listY[1:]
        self.listY.append(int(float(data[0])))
        self.w_temp.clear()
        self.w_temp.plot(self.listX,self.listY,pen = pg.mkPen("#20B2AA",width = 3))

        #update_progress_bar

        self.progressBar.setValue(int(float(data[1])))

        self.circular_progress_bar.set_value(int(float(data[0])))

    def change_velocidad(self):
        value = self.slider_velocidad.value()
        self.lcd_velocidad.display(value)
        self.serial.write((str(value)+'\r').encode())

    def left_direction(self):
        self.serial.write("IZQUIERDA\r".encode())

    def right_direction(self):
        self.serial.write("DERECHA\r".encode())

    def button_on(self):
        self.serial.write("ON\r".encode())

    def button_off(self):
        self.serial.write("OFF\r".encode())



if __name__ == "__main__":
    app = QApplication([])
    interface = Interface()
    interface.show()
    sys.exit(app.exec())