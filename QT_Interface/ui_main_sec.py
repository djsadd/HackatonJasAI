# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_photo.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QPushButton, QSizePolicy, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(836, 525)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(836, 525))
        MainWindow.setMaximumSize(QSize(836, 525))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
                                 "border-radius:10px;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setStyleSheet(u"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(-9, -9, 851, 541))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame{\n"
                                 "background-color:rgb(40, 40, 43);\n"
                                 "border-radius:10px\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.New = QPushButton(self.frame)
        self.New.setObjectName(u"New")
        self.New.setGeometry(QRect(70, 190, 231, 51))
        font = QFont()
        font.setFamilies([u"Constantia"])
        font.setPointSize(14)
        self.New.setFont(font)
        self.New.setStyleSheet(u"QPushButton{\n"
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
        self.Find = QPushButton(self.frame)
        self.Find.setObjectName(u"Find")
        self.Find.setGeometry(QRect(70, 280, 231, 51))
        self.Find.setFont(font)
        self.Find.setStyleSheet(u"QPushButton{\n"
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
        self.picture = QLabel(self.frame)
        self.picture.setObjectName(u"picture")
        self.picture.setEnabled(True)
        self.picture.setGeometry(QRect(360, 60, 431, 381))
        palette = QPalette()
        brush = QBrush(QColor(40, 40, 43, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.picture.setPalette(palette)
        self.picture.setStyleSheet(u"QLabel{\n"
                                   "background-color:rgb(40, 40, 43);\n"
                                   "border: 2px solid;\n"
                                   "}")
        self.picture.setScaledContents(False)
        self.picture.raise_()
        self.New.raise_()
        self.Find.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.New.setText(QCoreApplication.translate("MainWindow",
                                                    u"\u043d\u043e\u0432\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c",
                                                    None))
        self.Find.setText(QCoreApplication.translate("MainWindow",
                                                     u"\u043d\u0430\u0439\u0442\u0438 \u043f\u043e \u0444\u043e\u0442\u043e",
                                                     None))
        self.picture.setText("")
    # retranslateUi
