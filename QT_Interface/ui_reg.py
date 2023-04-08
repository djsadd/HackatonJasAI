# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_reg.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(778, 554)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(778, 554))
        Form.setMaximumSize(QSize(778, 554))
        Form.setStyleSheet(u"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-19, -9, 811, 591))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color:rgb(40, 40, 43);\n"
"border-radius:10px\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.next = QPushButton(self.frame)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(300, 340, 201, 51))
        font = QFont()
        font.setFamilies([u"Constantia"])
        font.setPointSize(14)
        self.next.setFont(font)
        self.next.setStyleSheet(u"QPushButton{\n"
"  background-color:rgb(48,186,143);\n"
"border:1px solid #717171;\n"
"border-radius:5px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.825, fx:0.5, fy:0.5, stop:0 rgba(48, 186, 143, 255), stop:1 rgba(146, 255, 150, 255))\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(48,186,143);\n"
"\n"
"}")
        self.Name = QLineEdit(self.frame)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(280, 210, 241, 41))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 190, 61, 81))
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{color:rgb(255, 255, 255);\n"
"background-color:rgba(255, 255, 255, 0);\n"
"}")
        self.photo = QPushButton(self.frame)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(300, 270, 201, 51))
        self.photo.setFont(font)
        self.photo.setStyleSheet(u"QPushButton{\n"
"  background-color:rgb(48,186,143);\n"
"border:1px solid #717171;\n"
"border-radius:5px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.825, fx:0.5, fy:0.5, stop:0 rgba(48, 186, 143, 255), stop:1 rgba(146, 255, 150, 255))\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(48,186,143);\n"
"\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.next.setText(QCoreApplication.translate("Form", u"\u0412\u043f\u0435\u0440\u0435\u0434!", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0424\u0418\u041e", None))
        self.photo.setText(QCoreApplication.translate("Form", u"\u0444\u043e\u0442\u043e", None))
    # retranslateUi

