# Form implementation generated from reading ui file 'ui/themhd.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QTableView
from datetime import datetime

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.serviceDAO import serviceDAO
from DAO.customerDAO import customerDAO
from DAO.billDAO import billDAO
from DTO.billDTO import bill
from DAO.cthdDAO import cthdDAO
from DTO.cthdDTO import CTHD
import GUI.thongbao as tb


class Ui_Dialog(object):
    def setupUi(self, Dialog, makh, manv):
        self.hdDAO = billDAO()
        self.makh = makh
        self.manv = manv
        self.tb= tb.Ui_Dialog()
        self.svDAO = serviceDAO()
        self.khDAO = customerDAO()
        self.kh = self.khDAO.findByid(makh)
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 520)
        Dialog.setMinimumSize(QtCore.QSize(740, 520))
        Dialog.setMaximumSize(QtCore.QSize(740, 520))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_5.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.btnAdd = QtWidgets.QPushButton(parent=self.widget_4)
        self.btnAdd.setMinimumSize(QtCore.QSize(90, 30))
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnAdd.setStyleSheet("background-color: #9FC899;\n"
"border: none;\n"
"border-radius: 5px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAdd.setIcon(icon)
        self.btnAdd.setIconSize(QtCore.QSize(20, 20))
        self.btnAdd.setFlat(False)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.addService)
        self.verticalLayout_4.addWidget(self.btnAdd)
        
        self.btnSua = QtWidgets.QPushButton(self.widget_4)
        self.btnSua.setStyleSheet("background-color: rgb(188, 202, 255);"
                                  "border: none;\n"
"border-radius: 5px;")
        self.btnSua.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        # self.btnSua.clicked.connect(self.update_PB)
        self.btnSua.setMinimumSize(90,30)
        self.btnSua.setText("Sửa")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSua.setIcon(icon2)
        self.btnSua.setIconSize(QtCore.QSize(20, 20))
        self.btnSua.setObjectName("btnSua")
        self.btnSua.setFlat(False)
        self.verticalLayout_4.addWidget(self.btnSua)
        self.btnSua.clicked.connect(self.update)
        
        self.btnXoa = QtWidgets.QPushButton(parent=self.widget_4)
        self.btnXoa.setMinimumSize(QtCore.QSize(90, 30))
        self.btnXoa.setStyleSheet("background-color: rgb(255, 11, 96);\n"
"border-radius: 5px;\n"
"border: none;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnXoa.setIcon(icon1)
        self.btnXoa.setObjectName("btnXoa")
        self.btnXoa.clicked.connect(self.delete_row)
        self.verticalLayout_4.addWidget(self.btnXoa)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.txtid = QtWidgets.QLineEdit(parent=self.widget_4)
        self.txtid.setMinimumSize(QtCore.QSize(100, 0))
        self.txtid.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txtid.setDragEnabled(False)
        self.txtid.setReadOnly(True)
        self.txtid.setObjectName("txtid")
        self.txtid.setText(makh)
        self.txtid.setAlignment(QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.txtid)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.txtName = QtWidgets.QLineEdit(parent=self.widget_4)
        self.txtName.setMinimumSize(QtCore.QSize(100, 0))
        self.txtName.setReadOnly(True)
        self.txtName.setObjectName("txtName")
        self.txtName.setText(self.kh.get_tenkh())
        self.txtName.setAlignment(QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addWidget(self.txtName)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.comboBox = QtWidgets.QComboBox(parent=self.widget_4)
        self.comboBox.setMinimumSize(QtCore.QSize(160, 0))
        self.comboBox.setObjectName("comboBox")
        dv_list = self.svDAO.getAllServices()
        for dv in dv_list:
                self.comboBox.addItem(f'{dv.getMaDV()} - {dv.getTen()}')
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.widget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        for i in range(1,11):
                self.comboBox_2.addItem(str(i))
        self.horizontalLayout_5.addWidget(self.comboBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.table_phieunhap = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.table_phieunhap.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_phieunhap.setObjectName("table_phieunhap")
        self.table_phieunhap.setColumnCount(5)
        self.table_phieunhap.setRowCount(0)
        
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_phieunhap.setHorizontalHeaderItem(0, item)
        

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_phieunhap.setHorizontalHeaderItem(1, item)
        
        
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_phieunhap.setHorizontalHeaderItem(2, item)
        
        
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_phieunhap.setHorizontalHeaderItem(3, item)
        
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_phieunhap.setHorizontalHeaderItem(4, item)
        
        
        self.table_phieunhap.horizontalHeader().setStretchLastSection(True)
        self.table_phieunhap.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.table_phieunhap)
        self.table_phieunhap.horizontalHeader().setCascadingSectionResizes(False)
        self.table_phieunhap.horizontalHeader().setSortIndicatorShown(False)
        self.table_phieunhap.horizontalHeader().setStretchLastSection(True)
        self.table_phieunhap.verticalHeader().setVisible(True)
        self.table_phieunhap.verticalHeader().setCascadingSectionResizes(False)
        self.table_phieunhap.cellDoubleClicked.connect(self.on_cell_double_clicked)
        self.widget_5 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 65))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.btnAdd_2 = QtWidgets.QPushButton(parent=self.widget_5)
        self.btnAdd_2.setMinimumSize(QtCore.QSize(90, 30))
        self.btnAdd_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnAdd_2.setStyleSheet("background-color: #9FC899;\n"
"border: none;\n"
"border-radius: 5px;")
        self.btnAdd_2.setIcon(icon)
        self.btnAdd_2.setIconSize(QtCore.QSize(20, 20))
        self.btnAdd_2.setFlat(False)
        self.btnAdd_2.setObjectName("btnAdd_2")
        self.btnAdd_2.clicked.connect(self.createBill)
        self.horizontalLayout_7.addWidget(self.btnAdd_2)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton.setStyleSheet("background-color: #BDD5D7;\n"
"border-radius: 5px;\n"
"border: none;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tạo hoá đơn"))
        self.groupBox_2.setTitle(_translate("Dialog", "THÔNG TIN KHÁCH HÀNG"))
        self.btnAdd.setText(_translate("Dialog", "Thêm"))
        self.label_5.setText(_translate("Dialog", "Mã khách hàng"))
        self.label_6.setText(_translate("Dialog", "Tên khách hàng"))
        self.label_3.setText(_translate("Dialog", "Dịch vụ"))
        self.label_2.setText(_translate("Dialog", "Số lượng"))
        item = self.table_phieunhap.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Mã dịch vụ"))
        item = self.table_phieunhap.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tên dịch vụ"))
        item = self.table_phieunhap.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Giá"))
        item = self.table_phieunhap.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Số lượng"))
        item = self.table_phieunhap.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Tổng giá"))
        self.btnAdd_2.setText(_translate("Dialog", "Tạo hoá đơn"))
        self.btnXoa.setText(_translate("Dialog", "Xóa"))
        self.pushButton.setText(_translate("Dialog", "Reset"))

    def addService(self):
        dv = self.svDAO.getServiceById(self.comboBox.currentIndex()+1)
        soluong = self.comboBox_2.currentIndex()+1
        tong = dv.getGia()*soluong
        data = [dv.getMaDV(),dv.getTen(),dv.getGia(),soluong,tong]
        self.add_row_to_table(data)
        self.tb.thongBao("Thêm thành công!")
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)

    def update(self):
        dv = self.svDAO.getServiceById(self.comboBox.currentIndex()+1)
        soluong = self.comboBox_2.currentIndex()+1
        tong = dv.getGia()*soluong
        data = [dv.getMaDV(),dv.getTen(),dv.getGia(),soluong,tong]
        self.update_row(data)
        self.tb.thongBao("Cập nhật thành công!")

    def update_row(self,data):
            for row in range(self.table_phieunhap.rowCount()):
                    if self.table_phieunhap.item(row, 0).text() == str(data[0]):
                        self.table_phieunhap.setItem(row, 3, QTableWidgetItem(str(data[3])))
                        self.table_phieunhap.setItem(row, 4, QTableWidgetItem(str(data[4])))
                        self.comboBox.setCurrentIndex(0)
                        self.comboBox_2.setCurrentIndex(0)
            
    def add_row_to_table(self, data):
                for row in range(self.table_phieunhap.rowCount()):
                    if self.table_phieunhap.item(row, 0).text() == str(data[0]):
                        old_value = int(self.table_phieunhap.item(row, 3).text())
                        old_price = int(self.table_phieunhap.item(row, 4).text())
                        self.table_phieunhap.setItem(row, 3, QTableWidgetItem(str(data[3]+old_value)))
                        self.table_phieunhap.setItem(row, 4, QTableWidgetItem(str(data[4]+old_price)))
                        return
                rowPosition = self.table_phieunhap.rowCount()
                self.table_phieunhap.insertRow(rowPosition)
                for column, item in enumerate(data):
                        self.table_phieunhap.setItem(rowPosition, column, QTableWidgetItem(str(item)))

    def delete_row(self):
        selected_row = self.table_phieunhap.currentRow()
        if selected_row >= 0:
                self.table_phieunhap.removeRow(selected_row)
                self.tb.thongBao('Xoá thành công!')
        else:
                self.tb.thongBao('Vui lòng chọn 1 dòng để xoá!')


    def on_cell_double_clicked(self, row, column):
        # Lấy dữ liệu từ dòng và cột được chọn
        dv = int(self.table_phieunhap.item(row, 0).text())
        sl = int(self.table_phieunhap.item(row, 3).text())
        if dv and sl:
            self.comboBox.setCurrentIndex(dv-1)
            self.comboBox_2.setCurrentIndex(sl-1)

    def refesh(self):
            self.table_phieunhap.setRowCount(0)
        
    def createBill(self):
            if self.table_phieunhap.rowCount() != 0:
                current_time = datetime.now()
                ngaytao = current_time.strftime("%Y/%m/%d")
                
                hd = bill("",ngaytao,0,self.manv,self.makh)
                self.hdDAO.insert(hd)
                num_rows = self.table_phieunhap.rowCount()

                for row in range(num_rows):
                        list=[]
                        for column in range(self.table_phieunhap.columnCount()):
                                list.append(self.table_phieunhap.item(row, column).text())
                        cthd = CTHD("",'',list[0],list[3],list[4])
                        ctDAO= cthdDAO()
                        ctDAO.insertCTHD2(cthd)
                        self.hdDAO.updateTotalPrice2(list[4])
                self.tb.thongBao("Tạo hoá đơn thành công")
                self.table_phieunhap.setRowCount(0)
            else:
                    self.tb.thongBao("Vui lòng chọn dịch vụ trước khi tạo hoá đơn!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog,1,2)
    Dialog.show()
    sys.exit(app.exec())
