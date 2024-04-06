# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/themNV.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.employeeDAO import employeeDAO
from DTO.employeeDTO import employee
import GUI.thongbao as tb


class Ui_Dialog(object):
    def setupUi(self, Dialog, type):
        self.type=type
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 276)
        Dialog.setMinimumSize(QtCore.QSize(400, 276))
        Dialog.setMaximumSize(QtCore.QSize(400, 276))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label.setObjectName("label")
        self.label_visible = QtWidgets.QLabel(Dialog)
        self.label_visible.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label_visible.setObjectName("label_visible")
        self.label_visible.setVisible(False)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 91, 16))
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, -1, 401, 61))
        self.widget.setStyleSheet("background-color: rgb(0, 255, 244);\n"
"border:1px solid black;")
        self.widget.setObjectName("widget")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setGeometry(QtCore.QRect(100, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("border:none;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.txtName = QtWidgets.QLineEdit(Dialog)
        self.txtName.setGeometry(QtCore.QRect(170, 90, 181, 21))
        self.txtName.setObjectName("txtName")
        self.txtPhone = QtWidgets.QLineEdit(Dialog)
        self.txtPhone.setGeometry(QtCore.QRect(170, 130, 181, 21))
        self.txtPhone.setObjectName("txtPhone")
        self.txtEmail = QtWidgets.QLineEdit(Dialog)
        self.txtEmail.setGeometry(QtCore.QRect(170, 170, 181, 21))
        self.txtEmail.setObjectName("txtEmail")
        self.btnAccept = QtWidgets.QPushButton(Dialog)
        self.btnAccept.setGeometry(QtCore.QRect(80, 220, 113, 32))
        self.btnAccept.setCheckable(True)
        self.btnAccept.setObjectName("btnAccept")
        if type == 1:
            self.btnAccept.clicked.connect(self.show_dialog_insert)
        elif type == 2:
            self.btnAccept.clicked.connect(lambda: self.show_dialog_update(self.label_visible.text()))
        self.btnDeny = QtWidgets.QPushButton(Dialog)
        self.btnDeny.setGeometry(QtCore.QRect(210, 220, 113, 32))
        self.btnDeny.setCheckable(True)
        self.btnDeny.setObjectName("btnDeny")
        self.btnDeny.toggled['bool'].connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self._translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Tên nhân viên"))
        self.label_2.setText(_translate("Dialog", "Số điện thoại"))
        self.label_3.setText(_translate("Dialog", "Email"))
        self.title.setText(_translate("Dialog", "THÊM NHÂN VIÊN"))
        self.btnAccept.setText(_translate("Dialog", "Xác nhận"))
        self.btnDeny.setText(_translate("Dialog", "Huỷ"))
        
    def show_dialog_update(self,id):
        Dialog = QtWidgets.QDialog()
        ui = tb.Ui_Dialog()
        ui.setupUi(Dialog)
        ui.label.setText(self._translate("Dialog", self.update_data(id)))
        Dialog.exec_()
        
    
    def show_dialog_insert(self):
        Dialog = QtWidgets.QDialog()
        ui = tb.Ui_Dialog()
        ui.setupUi(Dialog)
        ui.label.setText(self._translate("Dialog", self.insert_data()))
        Dialog.exec_()
        
        
    def insert_data(self):
        ten=self.txtName.text()
        email=self.txtEmail.text()
        sdt=self.txtPhone.text()
        empDAO= employeeDAO()
        if ten and sdt:
            emp = employee("",ten,sdt,email)
            result = empDAO.insert(emp)
            if result == "Thêm thành công !!!!":
                self.txtName.setText("")
                self.txtEmail.setText("")
                self.txtPhone.setText("")
            return result
            
        else: 
            return 'Tên và số điện thoại không được rỗng !!!!'
        
    def update_data(self,id):
        ten=self.txtName.text()
        email=self.txtEmail.text()
        sdt=self.txtPhone.text()
        empDAO= employeeDAO()
        if ten and sdt:
            emp = employee(id,ten,sdt,email)
            return empDAO.update(emp)  
        else: 
            return 'Tên và số điện thoại không được rỗng !!!!'


