from PySide6.QtCore import QRect,Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import QHBoxLayout, QWidget


class CircularBar(QWidget):
    def __init__(self,width,height):
        super().__init__()

        self.value = 0
        self.width = width
        self.height = height
        self.progress_width = 15
        self.progress_rounded_cap = True
        self.progress_color = 0x20B2AA
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x20B2AA

        self.resize(self.width,self.height)
        self.setMinimumSize(self.width,self.height)
        

    def set_value(self, value):
        self.value = value
        self.repaint()
    

    def paintEvent(self, event):
        
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.font_family,self.font_size))

        rect = QRect(0,0,self.width,self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)


        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        paint.setPen(pen)
        paint.drawArc(margin,margin,width,height,-90*16,-value*16)

        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter,f"{self.value}{self.suffix}")

        paint.end()

