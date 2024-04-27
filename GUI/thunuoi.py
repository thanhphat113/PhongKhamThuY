# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thunuoi.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QTableView

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import GUI.TacvuTN as tv
import GUI.thongbao as tb
import GUI.camTN as cam
from  DAO.petDAO import petDAO
from  DAO.customerDAO import customerDAO
import GUI.camera as cmr

class Ui_Form(object):
    def setupUi(self, Form):
        self.camTN = cam.Ui_Form()
        self.tb = tb.Ui_Dialog()
        Form.setObjectName("Form")
        Form.resize(800, 500)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(65, 255, 245);\n"
"    border:1px solid black\n"
"}\n"
"QLabel{\n"
"    border:none\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setStyleSheet("background-color: rgb(159, 255, 153);\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setStyleSheet("background-color: rgb(255, 124, 125);")
                                
        self.btnCamera = QtWidgets.QPushButton(self.widget_3)
        self.btnCamera.setStyleSheet("background-color: rgb(35, 124, 125);")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCamera.setIcon(icon10)
        self.btnCamera.setIconSize(QtCore.QSize(20, 20))
        self.btnCamera.setObjectName("btnCamera")
        self.btnCamera.setMinimumSize(100,30)
        self.horizontalLayout.addWidget(self.btnCamera)
        self.btnCamera.clicked.connect(self.openCamera) 
        
        self.btnNhanDien = QtWidgets.QPushButton(self.widget_3)
        self.btnNhanDien.setStyleSheet("background-color: rgb(100, 124, 125);")
        self.btnNhanDien.setIcon(icon10)
        self.btnNhanDien.setIconSize(QtCore.QSize(20, 20))
        self.btnNhanDien.setObjectName("btnNhanDien")
        self.btnNhanDien.setMinimumSize(100,30)
        self.btnNhanDien.clicked.connect(self.showCam)
        self.horizontalLayout.addWidget(self.btnNhanDien)
        # self.btnNhanDien.clicked.connect(self.openCamera)                   
                                
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setStyleSheet("background-color: rgb(188, 202, 255);")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_3, 2, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setStyleSheet("border:none;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(135, 5))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Tất cả")
        self.comboBox.addItem("Mã thú nuôi")
        self.comboBox.addItem("Tên thú nuôi")
        self.comboBox.addItem("Màu lông")
        self.comboBox.addItem("Khách hàng")
        self.comboBox.currentIndexChanged.connect(self.changeEnable)
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.findByCondition)
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self._translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Quản lý thú nuôi"))
        self.pushButton_3.setText(_translate("Form", "Thêm"))
        self.btnCamera.setText(_translate("Form", "Camera"))
        self.pushButton_3.setMinimumSize(100, 30)
        self.pushButton_3.clicked.connect(self.TacVu_TN)
        self.pushButton.setText(_translate("Form", "Xoá"))
        self.pushButton.setMinimumSize(100, 30)
        self.btnNhanDien.setText(_translate("Form", "Nhận diện"))
        self.btnNhanDien.setMinimumSize(100, 30)
        self.pushButton.clicked.connect(self.on_button_clicked)
        self.pushButton_2.setText(_translate("Form", "Sửa"))
        self.pushButton_2.setMinimumSize(100, 30)
        self.pushButton_2.clicked.connect(self.update_TN)
        self.label_2.setText(_translate("Form", "Tìm kiếm "))

        self.pushButton_4.setText(_translate("Form", "Tìm"))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableView.SelectRows)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã thú nuôi"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tên thú nuôi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Màu lông"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Cân nặng"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Khách hàng"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Tình trạng"))
        self.upload_list()
    

    def upload_list(self):
        dao = petDAO()
        pet_list = dao.ReadFromDatabase()
        cus_list = customerDAO().ReadFromDatabase()
        self.tableWidget.setRowCount(0)
        data_dir = 'data/thunuoi'
        list_directory = os.listdir(data_dir)
        for pet in pet_list:
            tt = '<Chưa có dữ liệu>'
            if str(pet.get_matn()) in list_directory:
                tt = '<Có dữ liệu>'
            for cus in cus_list:
                if cus.get_makh() == pet.get_makh():
                    data = [pet.get_matn(), pet.get_tentn(), pet.get_maulong(), pet.get_cannang(), cus.get_tenkh(), tt]
                    self.add_row_to_table(data)
                    break
                
    def showCam(self):
        Form = QtWidgets.QDialog()
        self.camTN.setupUi(Form)
        Form.exec_()
                
    

    def add_row_to_table(self, data):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for column, item in enumerate(data):
            self.tableWidget.setItem(rowPosition, column, QTableWidgetItem(str(item)))
    
        

    def TacVu_TN(self):
        Dialog = QtWidgets.QDialog()
        ui = tv.Ui_Dialog()
        ui.setupUi(Dialog,1)
        dao = customerDAO()
        customer = dao.ReadFromDatabase()
        for cus in customer:
            ui.cbMaKH.addItem(f"{cus.get_tenkh()}")
        Dialog.exec_()
        self.upload_list()
    

    def on_button_clicked(self):
        Dialog = QtWidgets.QDialog()
        ui = tb.Ui_Dialog()
        ui.setupUi(Dialog)
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            value = self.tableWidget.item(selected_row, 0).text()
            ui.label.setText(self._translate("Dialog", self.delete_TN(value)))
        else:
            ui.label.setText(self._translate("Dialog", "Vui lòng hãy chọn dòng muốn xoá"))
        Dialog.exec_()
        self.upload_list()

                
    def delete_TN(self, value):
        dao = petDAO()
        return dao.delete(value)
                
        
    def update_TN(self):
        Dialog = QtWidgets.QDialog()
        ui = tv.Ui_Dialog()
        ui.setupUi(Dialog,2)    
        ui.title.setText(self._translate("Dialog", "Sửa thông tin"))
        dao = customerDAO()
        customer = dao.ReadFromDatabase()
        for cus in customer:
            ui.cbMaKH.addItem(f"{cus.get_tenkh()}")
        selected_row = self.tableWidget.currentRow()
        if selected_row  >= 0:
            selected_items = self.tableWidget.selectedItems()
            row_data = [item.text() for item in selected_items]
            ui.label_visible.setText(self._translate("Dialog",row_data[0]))
            ui.txtName.setText(self._translate("Dialog",row_data[1]))
            ui.txtColor.setText(self._translate("Dialog",row_data[2]))
            ui.txtWeight.setText(self._translate("Dialog",row_data[3]))
            temp = petDAO().findByCustomer(row_data[4])
            for pet in temp:
                ui.cbMaKH.setCurrentText(pet.get_khachhang().get_tenkh())
        else: 
            tb.Ui_Dialog.thongBao("Vui lòng chọn 1 dòng để thực hiện sửa")
        Dialog.exec_()
        self.upload_list()

    
    def changeEnable(self):
        type = self.comboBox.currentIndex()
        if type == 0:
            self.lineEdit.setEnabled(False)
            self.upload_list()
        if type == 1:
            self.lineEdit.setEnabled(True)
        if type == 2:
            self.lineEdit.setEnabled(True)
        if type == 3:
            self.lineEdit.setEnabled(True)
        if type == 4:
            self.lineEdit.setEnabled(True)


    def findByCondition(self):
        type = self.comboBox.currentIndex()
        condition = self.lineEdit.text()
        customer = customerDAO().ReadFromDatabase()
        result = None

        if type == 1:
            self.lineEdit.setEnabled(True)
            result = petDAO().findById(condition)
        elif type == 2:
            self.lineEdit.setEnabled(True)
            result = petDAO().findByName(condition)
        elif type == 3:
            self.lineEdit.setEnabled(True)
            result = petDAO().findByColor(condition)
        elif type == 4:
            self.lineEdit.setEnabled(True)
            result = petDAO().findByCustomer(condition)

        if type != 0 and result is not None:
            self.tableWidget.setRowCount(0)
            for subPet in result:
                for cus in customer:
                    if cus.get_makh() == subPet.get_makh():
                        data = [subPet.get_matn(), subPet.get_tentn(), subPet.get_maulong(), subPet.get_cannang(), cus.get_tenkh()]
                        self.add_row_to_table(data)
                        break
        else:
            self.upload_list()
        self.lineEdit.setText("")

    def openCamera(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row  >= 0:
            selected_items = self.tableWidget.selectedItems()
            row_data = [item.text() for item in selected_items]
            id = self._translate("Dialog",row_data[0])
            name = self._translate("Dialog",row_data[1])
            camera = QtWidgets.QDialog()
            ui = cmr.Ui_Form()
            ui.setupUi(camera,id,2)
            camera.exec_()
        else: self.tb.thongBao("Vui lòng chọn 1 dòng để thực hiện tác vụ !")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
