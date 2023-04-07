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
        Form.resize(826, 592)
        Form.setStyleSheet(u"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 30, 811, 551))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(57, 106, 136, 255), stop:1 rgba(255, 187, 187, 255));\n"
"border-radius:10px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.next = QPushButton(self.frame)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(270, 330, 201, 51))
        self.next.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"color: white\n"
"}")
        self.Name = QLineEdit(self.frame)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(300, 220, 151, 31))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 190, 31, 81))
        self.label.setStyleSheet(u"QLabel{\n"
"background-color:rgba(175, 255, 246, 0)\n"
"}")
        self.photo = QPushButton(self.frame)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(270, 270, 201, 51))
        self.photo.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"color: white\n"
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

