# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BinaryLabeling(object):
    def setupUi(self, BinaryLabeling):
        BinaryLabeling.setObjectName("BinaryLabeling")
        BinaryLabeling.resize(1280, 720)
        BinaryLabeling.setFixedSize(1280, 720)
        self.frame = QtWidgets.QWidget(BinaryLabeling)
        self.frame.setFocus(QtCore.Qt.NoFocusReason)
        self.frame.setGeometry(QtCore.QRect(315, 40, 610, 610))
        self.frame.setAutoFillBackground(False)
        self.frame.setObjectName("frame")
        self.img = QtWidgets.QLabel(self.frame)
        self.img.setGeometry(QtCore.QRect(5, 5, 600, 600))
        self.img.setObjectName("img")
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        
        """self.btn_yes = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_yes.setGeometry(QtCore.QRect(330, 680, 93, 28))
        self.btn_yes.setObjectName("btn_yes")
        self.btn_no = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_no.setGeometry(QtCore.QRect(830, 680, 93, 28))
        self.btn_no.setObjectName("btn_no")"""
        self.label_currnum = QtWidgets.QLabel(BinaryLabeling)
        self.label_currnum.setGeometry(QtCore.QRect(600, 690, 47, 13))
        self.label_currnum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currnum.setObjectName("label_currnum")
        """self.btn_next = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_next.setGeometry(QtCore.QRect(960, 330, 60, 60))
        self.btn_next.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_next.setObjectName("btn_next")
        self.btn_prev = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_prev.setGeometry(QtCore.QRect(230, 330, 60, 60))
        self.btn_prev.setObjectName("btn_prev")"""
        self.btn_start = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_start.setGeometry(QtCore.QRect(320, 10, 601, 28))
        self.btn_start.setObjectName("ptn_start")
        self.loading = QtWidgets.QLabel(BinaryLabeling)
        self.loading.setGeometry(QtCore.QRect(520, 660, 211, 20))
        self.loading.setAlignment(QtCore.Qt.AlignCenter)
        self.loading.setObjectName("loading")

        self.retranslateUi(BinaryLabeling)
        QtCore.QMetaObject.connectSlotsByName(BinaryLabeling)

    def retranslateUi(self, BinaryLabeling):
        _translate = QtCore.QCoreApplication.translate
        BinaryLabeling.setWindowTitle(_translate("BinaryLabeling", "BinaryLabeling"))
        self.loading.setText(_translate("BinaryLabeling", ""))
        # self.btn_yes.setText(_translate("BinaryLabeling", "Yes"))
        # self.btn_no.setText(_translate("BinaryLabeling", "No"))
        self.label_currnum.setText(_translate("BinaryLabeling", ""))
        self.img.setText(_translate("BinaryLabeling", "To start please press start button.\n Or push Return on your keyboard."))
        # self.btn_next.setText(_translate("BinaryLabeling", ">"))
        # self.btn_prev.setText(_translate("BinaryLabeling", "<"))
        self.btn_start.setText(_translate("BinaryLabeling", "Start"))

