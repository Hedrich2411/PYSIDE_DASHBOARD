# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_xdUDSnEd.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLCDNumber,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1209, 761)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"")
        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 130, 1191, 621))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.gridLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border-radius:20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_on = QPushButton(self.frame_3)
        self.btn_on.setObjectName(u"btn_on")
        self.btn_on.setGeometry(QRect(40, 110, 131, 141))
        sizePolicy.setHeightForWidth(self.btn_on.sizePolicy().hasHeightForWidth())
        self.btn_on.setSizePolicy(sizePolicy)
        self.btn_on.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_on.setStyleSheet(u"QPushButton{\n"
"	background-color:#20B2AA;\n"
"	border-radius: 60%;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(37, 207, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(202, 202, 202);\n"
"}\n"
"")
        self.btn_on_2 = QPushButton(self.frame_3)
        self.btn_on_2.setObjectName(u"btn_on_2")
        self.btn_on_2.setGeometry(QRect(220, 110, 131, 141))
        sizePolicy.setHeightForWidth(self.btn_on_2.sizePolicy().hasHeightForWidth())
        self.btn_on_2.setSizePolicy(sizePolicy)
        self.btn_on_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_on_2.setStyleSheet(u"QPushButton{\n"
"	background-color:#20B2AA;\n"
"	border-radius: 60%;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(37, 207, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(202, 202, 202);\n"
"}\n"
"")
        self.lbl_encender = QLabel(self.frame_3)
        self.lbl_encender.setObjectName(u"lbl_encender")
        self.lbl_encender.setGeometry(QRect(80, 70, 71, 16))
        font = QFont()
        font.setFamilies([u"Bell MT"])
        font.setPointSize(11)
        self.lbl_encender.setFont(font)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 70, 49, 16))
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.gridLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	border-radius:20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.slider_velocidad = QSlider(self.frame_2)
        self.slider_velocidad.setObjectName(u"slider_velocidad")
        self.slider_velocidad.setGeometry(QRect(90, 150, 231, 51))
        sizePolicy.setHeightForWidth(self.slider_velocidad.sizePolicy().hasHeightForWidth())
        self.slider_velocidad.setSizePolicy(sizePolicy)
        self.slider_velocidad.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_velocidad.setStyleSheet(u"QSlider{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #20B2AA;\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    \n"
"	background-color: rgb(39, 216, 204);\n"
"}\n"
"")
        self.slider_velocidad.setMaximum(100)
        self.slider_velocidad.setOrientation(Qt.Horizontal)
        self.lcd_velocidad = QLCDNumber(self.frame_2)
        self.lcd_velocidad.setObjectName(u"lcd_velocidad")
        self.lcd_velocidad.setEnabled(True)
        self.lcd_velocidad.setGeometry(QRect(150, 50, 91, 71))
        sizePolicy.setHeightForWidth(self.lcd_velocidad.sizePolicy().hasHeightForWidth())
        self.lcd_velocidad.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.lcd_velocidad.setFont(font1)
        self.lcd_velocidad.setFocusPolicy(Qt.NoFocus)
        self.lcd_velocidad.setLayoutDirection(Qt.LeftToRight)
        self.lcd_velocidad.setStyleSheet(u"QLCDNumber{\n"
"background-color: rgb(235, 235, 235);\n"
"\n"
"color: #20B2AA;\n"
"\n"
"}")
        self.lcd_velocidad.setFrameShape(QFrame.Box)
        self.lcd_velocidad.setFrameShadow(QFrame.Raised)
        self.lcd_velocidad.setMidLineWidth(0)
        self.lcd_velocidad.setSmallDecimalPoint(False)
        self.lcd_velocidad.setDigitCount(3)
        self.lcd_velocidad.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_velocidad.setProperty("value", 100.000000000000000)
        self.lcd_velocidad.setProperty("intValue", 100)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 220, 51, 41))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QPixmap(u"img/Motor.png"))
        self.label.setScaledContents(True)
        self.btn_right = QPushButton(self.frame_2)
        self.btn_right.setObjectName(u"btn_right")
        self.btn_right.setGeometry(QRect(260, 220, 61, 41))
        sizePolicy.setHeightForWidth(self.btn_right.sizePolicy().hasHeightForWidth())
        self.btn_right.setSizePolicy(sizePolicy)
        self.btn_right.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_right.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"	background-color: rgb(223, 223, 223);\n"
"}")
        icon = QIcon()
        icon.addFile(u"img/Right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_right.setIcon(icon)
        self.btn_right.setIconSize(QSize(26, 50))
        self.btn_left = QPushButton(self.frame_2)
        self.btn_left.setObjectName(u"btn_left")
        self.btn_left.setGeometry(QRect(90, 220, 61, 41))
        sizePolicy.setHeightForWidth(self.btn_left.sizePolicy().hasHeightForWidth())
        self.btn_left.setSizePolicy(sizePolicy)
        self.btn_left.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_left.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"	background-color: rgb(223, 223, 223);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"img/Left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_left.setIcon(icon1)
        self.btn_left.setIconSize(QSize(26, 50))
        self.lbl_velmotor = QLabel(self.frame_2)
        self.lbl_velmotor.setObjectName(u"lbl_velmotor")
        self.lbl_velmotor.setGeometry(QRect(140, 140, 121, 16))
        self.lbl_velmotor.setFont(font)

        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-radius:20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(140, 70, 121, 201))
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.progressBar.setFont(font2)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(235, 235, 235);\n"
"border-radius:1px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"\n"
"background-color: #20B2AA;\n"
"\n"
"\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setOrientation(Qt.Vertical)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 20, 81, 16))
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.w_temp = PlotWidget(self.gridLayoutWidget)
        self.w_temp.setObjectName(u"w_temp")
        self.w_temp.setEnabled(True)
        sizePolicy.setHeightForWidth(self.w_temp.sizePolicy().hasHeightForWidth())
        self.w_temp.setSizePolicy(sizePolicy)
        self.w_temp.setStyleSheet(u"QWidget{\n"
"	border-radius:20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"")

        self.gridLayout.addWidget(self.w_temp, 1, 1, 1, 2)

        self.circular_progress = QWidget(self.gridLayoutWidget)
        self.circular_progress.setObjectName(u"circular_progress")
        sizePolicy.setHeightForWidth(self.circular_progress.sizePolicy().hasHeightForWidth())
        self.circular_progress.setSizePolicy(sizePolicy)
        self.circular_progress.setLayoutDirection(Qt.LeftToRight)
        self.circular_progress.setStyleSheet(u"QWidget{\n"
"	border-radius:20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.lbl_humedad = QLabel(self.circular_progress)
        self.lbl_humedad.setObjectName(u"lbl_humedad")
        self.lbl_humedad.setGeometry(QRect(170, 20, 61, 16))
        self.lbl_humedad.setFont(font)

        self.gridLayout.addWidget(self.circular_progress, 0, 1, 1, 1)

        self.btn_connect = QPushButton(self.widget)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setGeometry(QRect(850, 40, 141, 51))
        sizePolicy.setHeightForWidth(self.btn_connect.sizePolicy().hasHeightForWidth())
        self.btn_connect.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(11)
        self.btn_connect.setFont(font3)
        self.btn_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#20B2AA;\n"
"	border-radius: 12%;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(37, 207, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(202, 202, 202);\n"
"}\n"
"")
        self.btn_disconnect = QPushButton(self.widget)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setGeometry(QRect(1030, 40, 141, 51))
        sizePolicy.setHeightForWidth(self.btn_disconnect.sizePolicy().hasHeightForWidth())
        self.btn_disconnect.setSizePolicy(sizePolicy)
        self.btn_disconnect.setFont(font3)
        self.btn_disconnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#20B2AA;\n"
"	border-radius: 12%;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(37, 207, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(202, 202, 202);\n"
"}\n"
"")
        self.lbl_img = QLabel(self.widget)
        self.lbl_img.setObjectName(u"lbl_img")
        self.lbl_img.setGeometry(QRect(10, 10, 521, 101))
        self.lbl_img.setPixmap(QPixmap(u"F:/CODIGOS PYTHON/PYQT-AVR/img/logo.png"))
        self.lbl_img.setScaledContents(False)

        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_on.setText("")
        self.btn_on_2.setText("")
        self.lbl_encender.setText(QCoreApplication.translate("MainWindow", u"Encender", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.label.setText("")
        self.btn_right.setText("")
        self.btn_left.setText("")
        self.lbl_velmotor.setText(QCoreApplication.translate("MainWindow", u"Velocidad del motor", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p\u00baC", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.lbl_humedad.setText(QCoreApplication.translate("MainWindow", u"Humedad", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.btn_disconnect.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.lbl_img.setText("")
    # retranslateUi

