# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# Qt.WindowStaysOnTopHint()
from PyQt5.QtCore import Qt
from Widget_Location import Widget_Location

class Ui_BinaryLabeling(object):
    def setupUi(self, BinaryLabeling):
        BinaryLabeling.setObjectName("BinaryLabeling")
        BinaryLabeling.resize(800, 600)
        self.frame = QtWidgets.QLabel(BinaryLabeling)
        self.frame.setGeometry(QtCore.QRect(180, 60, 450, 450))
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setObjectName("frame")
        self.img = Widget_Location(self.frame)#QtWidgets.QLabel(self.frame)
        self.img.setGeometry(QtCore.QRect(10, 10, 430, 430))
        self.img.setObjectName("img")
        self.img.setAlignment(QtCore.Qt.AlignCenter)

        self.loading = QtWidgets.QLabel(BinaryLabeling)
        self.loading.setGeometry(QtCore.QRect(300, 530, 210, 20))
        self.loading.setAlignment(QtCore.Qt.AlignCenter)
        self.loading.setObjectName("loading")
        
        """self.btn_yes = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_yes.setGeometry(QtCore.QRect(200, 530, 93, 28))
        self.btn_yes.setObjectName("btn_yes")
        self.btn_no = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_no.setGeometry(QtCore.QRect(200, 530, 420, 28))
        self.btn_no.setObjectName("btn_no")"""
        self.label_currnum = QtWidgets.QLabel(BinaryLabeling)
        self.label_currnum.setGeometry(QtCore.QRect(380, 570, 47, 13))
        self.label_currnum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currnum.setObjectName("label_currnum")
        self.btn_next = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_next.setGeometry(QtCore.QRect(640, 250, 60, 60))
        self.btn_next.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_next.setObjectName("btn_next")
        self.btn_next.setEnabled(False)

        self.btn_prev = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_prev.setGeometry(QtCore.QRect(110, 250, 60, 60))
        self.btn_prev.setObjectName("btn_prev")
        self.btn_prev.setEnabled(False)

        self.btn_start = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_start.setGeometry(QtCore.QRect(180, 15, 450, 28))
        self.btn_start.setObjectName("btn_start")

        self.retranslateUi(BinaryLabeling)
        QtCore.QMetaObject.connectSlotsByName(BinaryLabeling)

    def retranslateUi(self, BinaryLabeling):
        _translate = QtCore.QCoreApplication.translate
        BinaryLabeling.setWindowTitle(_translate("BinaryLabeling", "BinaryLabeling"))
        self.loading.setText(_translate("BinaryLabeling", ""))
        # self.btn_yes.setText(_translate("BinaryLabeling", "Yes"))
        # self.btn_no.setText(_translate("BinaryLabeling", "Image does not contain any virus."))
        self.label_currnum.setText(_translate("BinaryLabeling", ""))
        self.img.setText(_translate("BinaryLabeling", "To start please press start button.\n Or push Return on your keyboard."))
        self.btn_next.setText(_translate("BinaryLabeling", ">"))
        self.btn_prev.setText(_translate("BinaryLabeling", "<"))
        self.btn_start.setText(_translate("BinaryLabeling", "Start"))

