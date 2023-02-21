# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BinaryLabeling(object):
    def setupUi(self, BinaryLabeling):
        BinaryLabeling.setObjectName("BinaryLabeling")
        BinaryLabeling.resize(800, 600)
        self.frame = QtWidgets.QWidget(BinaryLabeling)
        self.frame.setGeometry(QtCore.QRect(180, 20, 450, 450))
        self.frame.setAutoFillBackground(True)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color: yellow;")
        self.img = QtWidgets.QLabel(self.frame)
        self.img.setGeometry(QtCore.QRect(15, 11, 421, 431))
        self.img.setObjectName("img")
        self.btn_yes = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_yes.setGeometry(QtCore.QRect(200, 490, 93, 28))
        self.btn_yes.setObjectName("btn_yes")
        self.btn_no = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_no.setGeometry(QtCore.QRect(520, 490, 93, 28))
        self.btn_no.setObjectName("btn_no")
        self.btn_next = QtWidgets.QPushButton(BinaryLabeling)
        self.btn_next.setGeometry(QtCore.QRect(200, 530, 411, 28))
        self.btn_next.setObjectName("btn_next")
        self.label_currnum = QtWidgets.QLabel(BinaryLabeling)
        self.label_currnum.setGeometry(QtCore.QRect(380, 570, 47, 13))
        self.label_currnum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currnum.setObjectName("label_currnum")

        self.retranslateUi(BinaryLabeling)
        QtCore.QMetaObject.connectSlotsByName(BinaryLabeling)

    def retranslateUi(self, BinaryLabeling):
        _translate = QtCore.QCoreApplication.translate
        BinaryLabeling.setWindowTitle(_translate("BinaryLabeling", "BinaryLabeling"))
        self.btn_yes.setText(_translate("BinaryLabeling", "Yes"))
        self.btn_no.setText(_translate("BinaryLabeling", "No"))
        self.btn_next.setText(_translate("BinaryLabeling", "Next"))
        self.label_currnum.setText(_translate("BinaryLabeling", "1/x"))

