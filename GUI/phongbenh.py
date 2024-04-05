# Form implementation generated from reading ui file 'nhanvien.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QTableView,QMessageBox,QWidget

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import GUI.TacvuNV as tv
import GUI.thongbao as tb
from  DAO.phongbenhDAO import phongbenhDAO

        
class Ui_Form(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(800, 500)
                Form.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.gridLayout_3 = QtWidgets.QGridLayout(Form)
                self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
                self.gridLayout_3.setVerticalSpacing(0)
                self.gridLayout_3.setObjectName("gridLayout_3")
                self.widget = QtWidgets.QWidget(parent=Form)
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
                self.label = QtWidgets.QLabel(parent=self.widget)
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
                self.widget_3 = QtWidgets.QWidget(parent=Form)
                self.widget_3.setObjectName("widget_3")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setObjectName("horizontalLayout")
                spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                self.horizontalLayout.addItem(spacerItem)
                self.btnAccept = QtWidgets.QPushButton(parent=self.widget_3)
                self.btnAccept.setStyleSheet("background-color: rgb(159, 255, 153);\n"
        "")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnAccept.setIcon(icon)
                self.btnAccept.setIconSize(QtCore.QSize(20, 20))
                self.btnAccept.setObjectName("btnAccept")
                self.btnAccept.clicked.connect(self.TacVu_NV)
                self.horizontalLayout.addWidget(self.btnAccept)
                self.pushButton = QtWidgets.QPushButton(parent=self.widget_3)
                self.pushButton.setStyleSheet("background-color: rgb(255, 124, 125);\n"
        "\n"
        "")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("img/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.pushButton.setIcon(icon1)
                self.pushButton.setIconSize(QtCore.QSize(20, 20))
                self.pushButton.setObjectName("pushButton")
                self.horizontalLayout.addWidget(self.pushButton)
                self.btnUpdate = QtWidgets.QPushButton(parent=self.widget_3)
                self.btnUpdate.setStyleSheet("background-color: rgb(188, 202, 255);")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("img/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnUpdate.setIcon(icon2)
                self.btnUpdate.setIconSize(QtCore.QSize(20, 20))
                self.btnUpdate.setObjectName("btnUpdate")
                self.btnUpdate.clicked.connect(self.update_NV)
                self.horizontalLayout.addWidget(self.btnUpdate)
                self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
                self.gridLayout_3.addWidget(self.widget_3, 2, 0, 1, 1)
                self.widget_2 = QtWidgets.QWidget(parent=Form)
                self.widget_2.setObjectName("widget_2")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
                self.label_2.setStyleSheet("border:none;")
                self.label_2.setObjectName("label_2")
                self.horizontalLayout_2.addWidget(self.label_2)
                self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_2)
                self.lineEdit.setObjectName("lineEdit")
                self.horizontalLayout_2.addWidget(self.lineEdit)
                self.comboBox = QtWidgets.QComboBox(parent=self.widget_2)
                self.comboBox.setObjectName("comboBox")
                self.comboBox.setMinimumSize(150,20)
                self.horizontalLayout_2.addWidget(self.comboBox)
                self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget_2)
                self.pushButton_4.setStyleSheet("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("img/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.pushButton_4.setIcon(icon3)
                self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_4.setMinimumSize(80,20)
                self.horizontalLayout_2.addWidget(self.pushButton_4)
                spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                self.horizontalLayout_2.addItem(spacerItem1)
                self.verticalLayout_2.addLayout(self.horizontalLayout_2)
                self.tableWidget = QtWidgets.QTableWidget(parent=self.widget_2)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
                self.tableWidget.setSizePolicy(sizePolicy)
                self.tableWidget.setWordWrap(False)
                self.tableWidget.setColumnCount(4)
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
                self.label.setText(_translate("Form", "Quản lý phòng bệnh"))
                self.btnAccept.setText(_translate("Form", "Thêm"))
                self.btnAccept.setMinimumSize(100, 30)
                self.pushButton.setText(_translate("Form", "Xoá"))
                self.pushButton.setMinimumSize(100, 30)
                self.pushButton.clicked.connect(self.on_button_clicked)
                self.btnUpdate.setText(_translate("Form", "Sửa"))
                self.btnUpdate.setMinimumSize(100, 30)
                self.label_2.setText(_translate("Form", "Tìm kiếm "))
                self.pushButton_4.setText(_translate("Form", "Tìm"))
                
                
                self.tableWidget.setSortingEnabled(False)
                self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
                self.tableWidget.setSelectionBehavior(QTableView.SelectRows)
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText(_translate("Form", "Mã phòng bệnh"))
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText(_translate("Form", "Tên phòng bệnh"))
                item = self.tableWidget.horizontalHeaderItem(2)
                item.setText(_translate("Form", "Tình trạng"))
                item = self.tableWidget.horizontalHeaderItem(3)
                item.setText(_translate("Form", "Thú nuôi"))
                self.upload_list()
                
        def upload_list(self):
                pbDAO = phongbenhDAO()
                phongbenh_list=pbDAO.find_All()
                self.tableWidget.setRowCount(0)
                for emp in phongbenh_list:
                        data = None
                        pet = emp.thunuoi
                        if pet is not None:
                                data = [emp.mapb,emp.tenpb,emp.tinhtrang,pet.get_tentn()]
                        else:
                                data = [emp.mapb,emp.tenpb,emp.tinhtrang,'<Rỗng>']
                        self.add_row_to_table(data)
                        
        def add_row_to_table(self, data):
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                for column, item in enumerate(data):
                        self.tableWidget.setItem(rowPosition, column, QTableWidgetItem(str(item)))
                        
        def TacVu_NV(self):
                Dialog = QtWidgets.QDialog()
                ui = tv.Ui_Dialog()
                ui.setupUi(Dialog,1)
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
                        ui.label.setText(self._translate("Dialog", self.delete_PB(value)))
                else:
                        ui.label.setText(self._translate("Dialog", "Vui lòng hãy chọn dòng muốn xoá"))
                Dialog.exec_()
                self.upload_list()

                
        def delete_PB(self,value):
                pbDAO = phongbenhDAO()
                return pbDAO.delete(value)
                
        
        def update_NV(self):
                Dialog = QtWidgets.QDialog()
                ui = tv.Ui_Dialog()
                ui.setupUi(Dialog,2)    
                ui.title.setText(self._translate("Dialog", "Sửa thông tin"))
                selected_row = self.tableWidget.currentRow()
                if selected_row  >= 0:
                        selected_items = self.tableWidget.selectedItems()
                        row_data = [item.text() for item in selected_items]
                        ui.label_visible.setText(self._translate("Dialog",row_data[0]))
                        ui.txtName.setText(self._translate("Dialog",row_data[1]))
                        ui.txtPhone.setText(self._translate("Dialog",row_data[2]))
                        ui.txtEmail.setText(self._translate("Dialog",row_data[3]))
                        # ui.label.setText(self._translate("Dialog", self.update_NV()))
                Dialog.exec_()
                self.upload_list()
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
