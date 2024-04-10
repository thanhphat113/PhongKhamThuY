# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/phieunhap.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from DAO.ctpnDAO import ctpnDAO
from DAO.phieunhapDAO import phieunhapDAO
from DAO.employeeDAO import employeeDAO
from DAO.supplierDAO import supplierDAO
from DAO.medicineDAO import medicineDAO
from DTO.phieunhapDTO import PhieuNhap
from DTO.ctpnDTO import CTPN
from GUI.phieunhap_dialog import Ui_phieunhap_dialog
from GUI.ctpn_dialog import Ui_ctpn_dialog
import GUI.mesage_box as msg
from datetime import datetime

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(875, 561)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.txtSearchPN = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtSearchPN.setMinimumSize(QtCore.QSize(0, 32))
        self.txtSearchPN.setObjectName("txtSearchPN")
        self.horizontalLayout_5.addWidget(self.txtSearchPN)
        self.cbSearchPN = QtWidgets.QComboBox(self.groupBox_2)
        self.cbSearchPN.setMinimumSize(QtCore.QSize(0, 32))
        self.cbSearchPN.setObjectName("cbSearchPN")
        self.cbSearchPN.addItem("")
        self.cbSearchPN.addItem("")
        self.cbSearchPN.addItem("")
        self.horizontalLayout_5.addWidget(self.cbSearchPN)
        self.btnSearchPN = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSearchPN.setMinimumSize(QtCore.QSize(40, 40))
        self.btnSearchPN.setStyleSheet("background-color: #BDD5D7;")
        self.btnSearchPN.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../../PhongKhamThuY-master/img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearchPN.setIcon(icon)
        self.btnSearchPN.setObjectName("btnSearchPN")
        self.horizontalLayout_5.addWidget(self.btnSearchPN)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.table_phieunhap = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_phieunhap.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_phieunhap.setObjectName("table_phieunhap")
        self.table_phieunhap.setColumnCount(5)
        self.table_phieunhap.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(4, item)
        self.table_phieunhap.horizontalHeader().setStretchLastSection(True)
        self.table_phieunhap.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.table_phieunhap)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.btnAddCTNP = QtWidgets.QPushButton(self.groupBox)
        self.btnAddCTNP.setMinimumSize(QtCore.QSize(40, 40))
        self.btnAddCTNP.setStyleSheet("background-color: rgb(159, 255, 153);\n"
"")
        self.btnAddCTNP.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddCTNP.setIcon(icon2)
        self.btnAddCTNP.setObjectName("btnAddCTNP")
        self.horizontalLayout_6.addWidget(self.btnAddCTNP)
        self.btnEditCTPN = QtWidgets.QPushButton(self.groupBox)
        self.btnEditCTPN.setMinimumSize(QtCore.QSize(40, 40))
        self.btnEditCTPN.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"")
        self.btnEditCTPN.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/edit_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditCTPN.setIcon(icon3)
        self.btnEditCTPN.setObjectName("btnEditCTPN")
        self.horizontalLayout_6.addWidget(self.btnEditCTPN)
        self.btnDeleteCTPN = QtWidgets.QPushButton(self.groupBox)
        self.btnDeleteCTPN.setMinimumSize(QtCore.QSize(40, 40))
        self.btnDeleteCTPN.setStyleSheet("background-color: rgb(255, 124, 125);\n"
"\n"
"")
        self.btnDeleteCTPN.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeleteCTPN.setIcon(icon4)
        self.btnDeleteCTPN.setObjectName("btnDeleteCTPN")
        self.horizontalLayout_6.addWidget(self.btnDeleteCTPN)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.table_ctpn = QtWidgets.QTableWidget(self.groupBox)
        self.table_ctpn.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_ctpn.setObjectName("table_ctpn")
        self.table_ctpn.setColumnCount(5)
        self.table_ctpn.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(4, item)
        self.table_ctpn.horizontalHeader().setStretchLastSection(True)
        self.table_ctpn.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.table_ctpn)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setStyleSheet("QWidget{\n"
"background-color: rgb(133, 255, 246);    border:1px solid black\n"
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
        self.label.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(11, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(8, 5, 8, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnAdd = QtWidgets.QPushButton(self.widget_3)
        self.btnAdd.setMinimumSize(QtCore.QSize(100, 30))
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setStyleSheet("background-color: rgb(159, 255, 153);")
        self.btnAdd.setIcon(icon1)
        self.btnAdd.setIconSize(QtCore.QSize(20, 20))
        self.btnAdd.setFlat(False)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnEdit = QtWidgets.QPushButton(self.widget_3)
        self.btnEdit.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"")
        self.btnEdit.setIcon(icon2)
        self.btnEdit.setObjectName("btnEdit")
        self.horizontalLayout.addWidget(self.btnEdit)
        self.btnDelete = QtWidgets.QPushButton(self.widget_3)
        self.btnDelete.setStyleSheet("background-color: rgb(255, 124, 125);\n"
"\n"
"")
        self.btnDelete.setIcon(icon3)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnReset = QtWidgets.QPushButton(self.widget_3)
        self.btnReset.setMinimumSize(QtCore.QSize(100, 30))
        self.btnReset.setStyleSheet("background-color: #BDD5D7;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReset.setIcon(icon5)
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout.addWidget(self.btnReset)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_3, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "THÔNG TIN PHIẾU NHẬP"))
        self.cbSearchPN.setItemText(0, _translate("Form", "Mã phiếu nhập"))
        self.cbSearchPN.setItemText(1, _translate("Form", "Mã nhân viên"))
        self.cbSearchPN.setItemText(2, _translate("Form", "Mã nhà cung cấp"))
        item = self.table_phieunhap.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã phiếu nhập"))
        item = self.table_phieunhap.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mã nhân viên"))
        item = self.table_phieunhap.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mã nhà cung cấp"))
        item = self.table_phieunhap.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Ngày lập"))
        item = self.table_phieunhap.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tổng tiền"))
        self.groupBox.setTitle(_translate("Form", "CHI TIẾT PHIẾU NHẬP"))
        item = self.table_ctpn.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã phiếu nhập"))
        item = self.table_ctpn.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mã dược phẩm"))
        item = self.table_ctpn.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Số lượng"))
        item = self.table_ctpn.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Đơn giá"))
        item = self.table_ctpn.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Thành tiền"))
        self.label.setText(_translate("Form", "Quản lý phiếu nhập"))
        self.btnAdd.setText(_translate("Form", "Thêm"))
        self.btnEdit.setText(_translate("Form", "Sửa"))
        self.btnDelete.setText(_translate("Form", "Xóa"))
        self.btnReset.setText(_translate("Form", "Reset"))
        self.loadPhieuNhapData()
        self.table_phieunhap.itemClicked.connect(self.on_table_phieunhap_clicked)
        self.btnAdd.clicked.connect(self.show_add_pn_dialog)
        self.btnAddCTNP.clicked.connect(self.show_add_ctpn_dialog)
        self.btnEdit.clicked.connect(self.show_update_pn_dialog)
        self.btnEditCTPN.clicked.connect(self.show_update_ctpn_dialog)
        self.btnDelete.clicked.connect(self.deletePhieuNhap)
        self.btnDeleteCTPN.clicked.connect(self.deleteCTPN)
        self.btnSearchPN.clicked.connect(self.searchPhieuNhap)
        self.btnReset.clicked.connect(self.loadPhieuNhapData)

    def fillTablePhieuNhap(self, pn_list):
        row = 0
        self.table_phieunhap.setRowCount(len(pn_list))
        for pn in pn_list:
            self.table_phieunhap.setItem(row, 0, QtWidgets.QTableWidgetItem(str(pn.getMaPN())))
            self.table_phieunhap.setItem(row, 1, QtWidgets.QTableWidgetItem(str(pn.getMaNV())))
            self.table_phieunhap.setItem(row, 2, QtWidgets.QTableWidgetItem(str(pn.getMaNCC())))
            self.table_phieunhap.setItem(row, 3, QtWidgets.QTableWidgetItem(str(pn.getNgayTao())))
            self.table_phieunhap.setItem(row, 4, QtWidgets.QTableWidgetItem(str(pn.getTongTien())))
            row = row +1

    def fillTableCTPN(self, ctpn_list):
        row = 0
        self.table_ctpn.setRowCount(len(ctpn_list))
        dao = medicineDAO()
        for ctpn in ctpn_list:
            medicine = dao.getMedicineById(ctpn.getMaDP())
            self.table_ctpn.setItem(row, 0, QtWidgets.QTableWidgetItem(str(ctpn.getMaPN())))
            self.table_ctpn.setItem(row, 1, QtWidgets.QTableWidgetItem(str(medicine.getTenDP())))
            self.table_ctpn.setItem(row, 2, QtWidgets.QTableWidgetItem(str(ctpn.getSoLuong())))
            self.table_ctpn.setItem(row, 3, QtWidgets.QTableWidgetItem(str(ctpn.getGia())))
            self.table_ctpn.setItem(row, 4, QtWidgets.QTableWidgetItem(str(ctpn.getThanhTien())))
            row = row +1

    def loadPhieuNhapData(self):
        dao = phieunhapDAO()
        pn_list = dao.getAllPhieuNhap()
        self.fillTablePhieuNhap(pn_list)

    def on_table_phieunhap_clicked(self):
        selected_items = self.table_phieunhap.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            mapn = self.table_phieunhap.item(selected_row, 0).text()
            ctdao = ctpnDAO()
            ctpn_list = ctdao.getCTPNById(mapn)
            self.fillTableCTPN(ctpn_list)

    def show_add_pn_dialog(self):
        dialog = QtWidgets.QDialog()
        self.phieunhap_dialog = Ui_phieunhap_dialog()
        self.phieunhap_dialog.setupUi(dialog)
        self.loadComboboxMaNV()
        self.loadComboboxMaNCC()
        self.phieunhap_dialog.txtTotalPrice.setEnabled(False)
        self.phieunhap_dialog.dateNgayTao.setEnabled(False)
        self.phieunhap_dialog.btnAccept.clicked.connect(self.addPhieuNhap)
        dialog.exec_()
        dialog.show()

    def show_update_pn_dialog(self):
        dialog = QtWidgets.QDialog()
        self.phieunhap_dialog = Ui_phieunhap_dialog()
        self.phieunhap_dialog.setupUi(dialog)
        self.phieunhap_dialog.label_4.setText("SỬA PHIẾU NHẬP")
        self.loadComboboxMaNV()
        self.loadComboboxMaNCC()

        selected_row = self.table_phieunhap.currentRow()
        if selected_row < 0:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng phiếu nhập")
            return

        selected_items = self.table_phieunhap.selectedItems()
        row_data = [item.text() for item in selected_items]
        mapn = row_data[0]
        manv = row_data[1]
        mancc = row_data[2]
        ngaytao = QtCore.QDate.fromString(row_data[3], "yyyy-M-d")   
        tongtien = row_data[4]   
        cbNV = self.phieunhap_dialog.cbMaNV
        cbNCC = self.phieunhap_dialog.cbMaNCC  
        for count in range(cbNV.count()):
            if manv in cbNV.itemText(count):
                indexNV = count

        for count in range(cbNCC.count()):
            if mancc in cbNCC.itemText(count):
                indexNCC = count

        self.phieunhap_dialog.cbMaNV.setCurrentIndex(indexNV)
        self.phieunhap_dialog.cbMaNCC.setCurrentIndex(indexNCC)
        self.phieunhap_dialog.txtTotalPrice.setText(tongtien)
        self.phieunhap_dialog.dateNgayTao.setDate(ngaytao)
        pn = PhieuNhap(mapn, manv, mancc, ngaytao, tongtien)

        self.phieunhap_dialog.btnAccept.clicked.connect(lambda: self.updatePhieuNhap(pn))
        dialog.exec_()
        dialog.show()

    def show_add_ctpn_dialog(self):
        dialog = QtWidgets.QDialog()
        self.ctpn_dialog = Ui_ctpn_dialog()
        self.ctpn_dialog.setupUi(dialog)
        self.loadComboboxMaDP()

        selected_items = self.table_phieunhap.selectedItems()
        if not selected_items:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng phiếu nhập")
            return
        
        selected_row = selected_items[0].row()
        id = self.table_phieunhap.item(selected_row, 0).text()
        totalprice = self.table_phieunhap.item(selected_row, 4).text()
        
        self.ctpn_dialog.cbMaDP.currentIndexChanged.connect(self.loadPriceOfMedicine)
        self.ctpn_dialog.btnAccept.clicked.connect(lambda: self.addCTPN(id, int(totalprice)))
        dialog.exec_()
        dialog.show()

    def show_update_ctpn_dialog(self):
        dialog = QtWidgets.QDialog()
        self.ctpn_dialog = Ui_ctpn_dialog()
        self.ctpn_dialog.setupUi(dialog)
        self.ctpn_dialog.label_4.setText("SỬA CHI TIẾT PHIẾU NHẬP")
        self.loadComboboxMaDP()

        selected_pn = self.table_phieunhap.selectedItems()
        if not selected_pn:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng phiếu nhập")
            return
        
        items_ctpn = self.table_ctpn.selectedItems()
        if not items_ctpn:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng chi tiết phiếu nhập")
            return
        
        selected_row = items_ctpn[0].row()
        mapn = self.table_ctpn.item(selected_row, 0).text()
        madp = self.table_ctpn.item(selected_row, 1).text()
        sl = self.table_ctpn.item(selected_row, 2).text()
        gia = self.table_ctpn.item(selected_row, 3).text()
        cbDP = self.ctpn_dialog.cbMaDP
        for count in range(cbDP.count()):
            if madp in cbDP.itemText(count):
                index = count
        self.ctpn_dialog.cbMaDP.setCurrentIndex(index)
        self.ctpn_dialog.txtQty.setText(sl)
        self.ctpn_dialog.txtPrice.setText(gia)
        
        self.ctpn_dialog.cbMaDP.currentIndexChanged.connect(self.loadPriceOfMedicine)
        self.ctpn_dialog.btnAccept.clicked.connect(lambda: self.updateCTPN(mapn))
        dialog.exec_()
        dialog.show()

    def loadPriceOfMedicine(self):
        madp = self.ctpn_dialog.cbMaDP.currentText().split("-")[0]
        dao = medicineDAO()
        medicine = dao.getMedicineById(madp)
        self.ctpn_dialog.txtPrice.setText(str(medicine.getGia()))

    def loadComboboxMaNV(self):
        dao = employeeDAO()
        employees = dao.find_All()

        for emp in employees:
            self.phieunhap_dialog.cbMaNV.addItem(f"{emp.manv} - {emp.tennv}")

    def loadComboboxMaNCC(self):
        dao = supplierDAO()
        suppliers = dao.getAllSuppliers()

        for supplier in suppliers:
            self.phieunhap_dialog.cbMaNCC.addItem(f"{supplier.getMaNCC()} - {supplier.getTenNCC()}")

    def loadComboboxMaDP(self):
        dao = medicineDAO()
        medicines = dao.getAllMedicines()

        for m in medicines:
            self.ctpn_dialog.cbMaDP.addItem(f"{m.getMaDP()} - {m.getTenDP()}")


    def addPhieuNhap(self):
        manv = self.phieunhap_dialog.cbMaNV.currentText().split("-")[0]
        mancc = self.phieunhap_dialog.cbMaNCC.currentText().split("-")[0]
        ngaytao = datetime.today().strftime('%Y-%m-%d')

        dao = phieunhapDAO()
        dao.insertPhieuNhap(PhieuNhap(None, manv, mancc, ngaytao, 0))
        msg.show_info_messagebox("Thêm phiếu nhập thành công")
        self.loadPhieuNhapData()

    def addCTPN(self, mapn, totalprice):
        madp = self.ctpn_dialog.cbMaDP.currentText().split("-")[0]
        gia = self.ctpn_dialog.txtPrice.text()
        sl = self.ctpn_dialog.txtQty.text()
        thanhtien = int(gia) * int(sl)
        totalprice += thanhtien

        if not sl:
            msg.show_warning_messagebox("Vui lòng nhập đầy đủ dữ liệu")
            return
    
        ctdao = ctpnDAO()
        pndao = phieunhapDAO()
        ctdao.insertCTPN(CTPN(mapn, madp, sl, gia, thanhtien))
        pndao.updateTotalPrice(mapn, totalprice)
        msg.show_info_messagebox("Thêm phiếu nhập thành công")
        self.on_table_phieunhap_clicked()
        self.loadPhieuNhapData()

    def updatePhieuNhap(self, pn):
        manv = self.phieunhap_dialog.cbMaNV.currentText().split("-")[0]
        mancc = self.phieunhap_dialog.cbMaNCC.currentText().split("-")[0]
        ngaytao = self.phieunhap_dialog.dateNgayTao.date().toString('MM-dd-yyyy')
        tongtien = self.phieunhap_dialog.txtTotalPrice.text()

        if not tongtien:
            msg.show_warning_messagebox("Vui lòng nhập đầy đủ dữ liệu")
            return
        
        dao = phieunhapDAO()
        dao.updatePhieuNhap(PhieuNhap(pn.getMaPN(), manv, mancc, ngaytao, tongtien))
        msg.show_info_messagebox("Sửa phiếu nhập thành công")
        self.on_table_phieunhap_clicked()

    def updateCTPN(self, mapn):
        madp = self.ctpn_dialog.cbMaDP.currentText().split("-")[0]
        gia = self.ctpn_dialog.txtPrice.text()
        sl = self.ctpn_dialog.txtQty.text()
        thanhtien = int(gia) * int(sl)

        if not sl:
            msg.show_warning_messagebox("Vui lòng nhập đầy đủ dữ liệu")
            return
        
        dao = ctpnDAO()
        dao.updateCTPN(CTPN(mapn, madp, sl, gia, thanhtien))
        msg.show_info_messagebox("Sửa phiếu nhập thành công")
        self.on_table_phieunhap_clicked()

    def deletePhieuNhap(self):
        selected_items = self.table_phieunhap.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            id = self.table_phieunhap.item(selected_row, 0).text()
            dao = phieunhapDAO()
            dao.deletePhieuNhap(id)
            msg.show_warning_messagebox("Xóa phiếu nhập đã chọn thành công")
            self.loadPhieuNhapData()
            self.on_table_phieunhap_clicked()
        else:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng phiếu nhập")

    def deleteCTPN(self):
        items_pn = self.table_phieunhap.selectedItems()
        if not items_pn:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng phiếu nhập")
            return
        
        items_ctpn = self.table_ctpn.selectedItems()
        if items_ctpn:
            selected_row = items_ctpn[0].row()
            mapn = self.table_ctpn.item(selected_row, 0).text()
            madp = self.table_ctpn.item(selected_row, 1).text()
            dao = ctpnDAO()
            dao.deleteCTPN(mapn, madp)
            msg.show_warning_messagebox("Xóa chi tiết phiếu nhập đã chọn thành công")
            self.on_table_phieunhap_clicked()
        else:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng chi tiết phiếu nhập")

    def searchPhieuNhap(self):
        dao = phieunhapDAO()
        search = self.txtSearchPN.text()
        choice = self.cbSearchPN.currentIndex()
        pn = dao.searchPhieuNhap(search, choice)
        self.fillTablePhieuNhap(pn)

   
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
