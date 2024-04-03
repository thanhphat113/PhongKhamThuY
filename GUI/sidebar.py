# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from GUI.add_service_dialog import Ui_add_service_dialog
from GUI import nhanvien as nv ,dichvu as dv, thunuoi as tn, home ,khachhang as kh, hoadon,phieunhap as pn,duocpham as dp


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 638)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"background-color: rgb(248, 255, 243);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_menu_widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(133, 255, 246);\n"
"}\n"
"\n"
"QPushButton{\n"
"    height:30px;\n"
"    border:none;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(255, 255, 255);\n"
"    font-weight:bold;\n"
"}")
        self.icon_menu_widget.setObjectName("icon_menu_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_menu_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.icon_menu_widget)
        self.label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/house-chimney-window-solid.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 15, -1, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.iconHome = QtWidgets.QPushButton(self.icon_menu_widget)
        self.iconHome.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconHome.setIcon(icon)
        self.iconHome.setIconSize(QtCore.QSize(20, 20))
        self.iconHome.setCheckable(True)
        self.iconHome.setAutoExclusive(True)
        self.iconHome.setObjectName("iconHome")
        self.verticalLayout.addWidget(self.iconHome)
        self.iconCustomer = QtWidgets.QPushButton(self.icon_menu_widget)
        self.iconCustomer.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/user-group-solid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconCustomer.setIcon(icon1)
        self.iconCustomer.setIconSize(QtCore.QSize(20, 20))
        self.iconCustomer.setCheckable(True)
        self.iconCustomer.setAutoExclusive(True)
        self.iconCustomer.setObjectName("iconCustomer")
        self.verticalLayout.addWidget(self.iconCustomer)
        self.iconPets = QtWidgets.QPushButton(self.icon_menu_widget)
        self.iconPets.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/pets.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconPets.setIcon(icon2)
        self.iconPets.setIconSize(QtCore.QSize(20, 20))
        self.iconPets.setCheckable(True)
        self.iconPets.setAutoExclusive(True)
        self.iconPets.setObjectName("iconPets")
        self.verticalLayout.addWidget(self.iconPets)
        self.iconEmployee = QtWidgets.QPushButton(self.icon_menu_widget)
        self.iconEmployee.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/employee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconEmployee.setIcon(icon3)
        self.iconEmployee.setIconSize(QtCore.QSize(20, 20))
        self.iconEmployee.setCheckable(True)
        self.iconEmployee.setAutoExclusive(True)
        self.iconEmployee.setObjectName("iconEmployee")
        self.verticalLayout.addWidget(self.iconEmployee)
        self.iconPhieuNhap = QtWidgets.QPushButton(self.icon_menu_widget)
        self.iconPhieuNhap.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/note_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconPhieuNhap.setIcon(icon4)
        self.iconPhieuNhap.setIconSize(QtCore.QSize(20, 20))
        self.iconPhieuNhap.setCheckable(True)
        self.iconPhieuNhap.setAutoExclusive(True)
        self.iconPhieuNhap.setObjectName("iconPhieuNhap")
        self.verticalLayout.addWidget(self.iconPhieuNhap)
        self.iconMedicine = QtWidgets.QPushButton(self.icon_menu_widget)
        self.iconMedicine.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/medical_bag_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconMedicine.setIcon(icon5)
        self.iconMedicine.setIconSize(QtCore.QSize(20, 20))
        self.iconMedicine.setCheckable(True)
        self.iconMedicine.setAutoExclusive(True)
        self.iconMedicine.setObjectName("iconMedicine")
        self.verticalLayout.addWidget(self.iconMedicine)
        self.iconService = QtWidgets.QPushButton(self.icon_menu_widget)
        self.iconService.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/service.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconService.setIcon(icon6)
        self.iconService.setIconSize(QtCore.QSize(20, 20))
        self.iconService.setCheckable(True)
        self.iconService.setAutoExclusive(True)
        self.iconService.setObjectName("iconService")
        self.verticalLayout.addWidget(self.iconService)
        self.iconChart = QtWidgets.QPushButton(self.icon_menu_widget)
        self.iconChart.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconChart.setIcon(icon7)
        self.iconChart.setIconSize(QtCore.QSize(20, 20))
        self.iconChart.setCheckable(True)
        self.iconChart.setAutoExclusive(True)
        self.iconChart.setObjectName("iconChart")
        self.verticalLayout.addWidget(self.iconChart)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 133, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushButton_5 = QtWidgets.QPushButton(self.icon_menu_widget)
        self.pushButton_5.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.gridLayout.addWidget(self.icon_menu_widget, 0, 0, 1, 1)
        self.menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.menu_widget.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.menu_widget.setFont(font)
        self.menu_widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(133, 255, 246);\n"
"}\n"
"\n"
"QPushButton{\n"
"    height:30px;\n"
"    border:none;\n"
"    text-align:left;\n"
"    padding-left:5px;\n"
"    padding-right:5px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(255, 255, 255);\n"
"    font-weight:bold;\n"
"}\n"
"")
        self.menu_widget.setObjectName("menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu_widget)
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.menu_widget)
        self.label_3.setMinimumSize(QtCore.QSize(40, 40))
        self.label_3.setMaximumSize(QtCore.QSize(40, 40))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/house-chimney-window-solid.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 15, -1, -1)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnHome = QtWidgets.QPushButton(self.menu_widget)
        self.btnHome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnHome.setAutoFillBackground(False)
        self.btnHome.setIcon(icon)
        self.btnHome.setIconSize(QtCore.QSize(20, 20))
        self.btnHome.setCheckable(True)
        self.btnHome.setAutoExclusive(True)
        self.btnHome.setObjectName("btnHome")
        self.verticalLayout_2.addWidget(self.btnHome)
        self.btnCustomer = QtWidgets.QPushButton(self.menu_widget)
        self.btnCustomer.setIcon(icon1)
        self.btnCustomer.setIconSize(QtCore.QSize(20, 20))
        self.btnCustomer.setCheckable(True)
        self.btnCustomer.setAutoExclusive(True)
        self.btnCustomer.setObjectName("btnCustomer")
        self.verticalLayout_2.addWidget(self.btnCustomer)
        self.btnPets = QtWidgets.QPushButton(self.menu_widget)
        self.btnPets.setIcon(icon2)
        self.btnPets.setIconSize(QtCore.QSize(20, 20))
        self.btnPets.setCheckable(True)
        self.btnPets.setAutoExclusive(True)
        self.btnPets.setObjectName("btnPets")
        self.verticalLayout_2.addWidget(self.btnPets)
        self.btnEmployee = QtWidgets.QPushButton(self.menu_widget)
        self.btnEmployee.setIcon(icon3)
        self.btnEmployee.setIconSize(QtCore.QSize(20, 20))
        self.btnEmployee.setCheckable(True)
        self.btnEmployee.setAutoExclusive(True)
        self.btnEmployee.setObjectName("btnEmployee")
        self.verticalLayout_2.addWidget(self.btnEmployee)
        self.btnPhieuNhap = QtWidgets.QPushButton(self.menu_widget)
        self.btnPhieuNhap.setIcon(icon4)
        self.btnPhieuNhap.setIconSize(QtCore.QSize(20, 20))
        self.btnPhieuNhap.setCheckable(True)
        self.btnPhieuNhap.setAutoExclusive(True)
        self.btnPhieuNhap.setObjectName("btnPhieuNhap")
        self.verticalLayout_2.addWidget(self.btnPhieuNhap)
        self.btnMedicine = QtWidgets.QPushButton(self.menu_widget)
        self.btnMedicine.setIcon(icon5)
        self.btnMedicine.setIconSize(QtCore.QSize(20, 20))
        self.btnMedicine.setCheckable(True)
        self.btnMedicine.setAutoExclusive(True)
        self.btnMedicine.setObjectName("btnMedicine")
        self.verticalLayout_2.addWidget(self.btnMedicine)
        self.btnService = QtWidgets.QPushButton(self.menu_widget)
        self.btnService.setIcon(icon6)
        self.btnService.setIconSize(QtCore.QSize(20, 20))
        self.btnService.setCheckable(True)
        self.btnService.setAutoExclusive(True)
        self.btnService.setObjectName("btnService")
        self.verticalLayout_2.addWidget(self.btnService)
        self.btnChart = QtWidgets.QPushButton(self.menu_widget)
        self.btnChart.setIcon(icon7)
        self.btnChart.setIconSize(QtCore.QSize(20, 20))
        self.btnChart.setCheckable(True)
        self.btnChart.setAutoExclusive(True)
        self.btnChart.setObjectName("btnChart")
        self.verticalLayout_2.addWidget(self.btnChart)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 129, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.pushButton_12 = QtWidgets.QPushButton(self.menu_widget)
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_4.addWidget(self.pushButton_12)
        self.gridLayout.addWidget(self.menu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnMenu = QtWidgets.QPushButton(self.widget_4)
        self.btnMenu.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu.setIcon(icon9)
        self.btnMenu.setIconSize(QtCore.QSize(20, 20))
        self.btnMenu.setCheckable(True)
        self.btnMenu.setChecked(False)
        self.btnMenu.setObjectName("btnMenu")
        self.horizontalLayout_2.addWidget(self.btnMenu)
        spacerItem3 = QtWidgets.QSpacerItem(451, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.btnAccount = QtWidgets.QPushButton(self.widget_4)
        self.btnAccount.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/customer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAccount.setIcon(icon10)
        self.btnAccount.setIconSize(QtCore.QSize(20, 20))
        self.btnAccount.setObjectName("btnAccount")
        self.horizontalLayout_2.addWidget(self.btnAccount)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid black;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_Page = QtWidgets.QWidget()
        self.home_Page.setObjectName("home_Page")
        self.label_4 = QtWidgets.QLabel(self.home_Page)
        self.label_4.setGeometry(QtCore.QRect(160, 80, 60, 16))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.home_Page)
        self.customer_Page = QtWidgets.QWidget()
        self.customer_Page.setObjectName("customer_Page")
        self.label_5 = QtWidgets.QLabel(self.customer_Page)
        self.label_5.setGeometry(QtCore.QRect(240, 110, 60, 16))
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.customer_Page)
        self.pets_Page = QtWidgets.QWidget()
        self.pets_Page.setObjectName("pets_Page")
        self.label_6 = QtWidgets.QLabel(self.pets_Page)
        self.label_6.setGeometry(QtCore.QRect(280, 160, 60, 16))
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.pets_Page)
        self.employee_page = QtWidgets.QWidget()
        self.employee_page.setObjectName("employee_page")
        self.stackedWidget.addWidget(self.employee_page)
        self.phieunhap_page = QtWidgets.QWidget()
        self.phieunhap_page.setObjectName("phieunhap_page")
        self.stackedWidget.addWidget(self.phieunhap_page)
        self.medicine_page = QtWidgets.QWidget()
        self.medicine_page.setObjectName("medicine_page")
        self.stackedWidget.addWidget(self.medicine_page)
        self.service_Page = QtWidgets.QWidget()
        self.service_Page.setObjectName("service_Page")
        self.stackedWidget.addWidget(self.service_Page)
        self.chart_Page = QtWidgets.QWidget()
        self.chart_Page.setObjectName("chart_Page")
        self.label_8 = QtWidgets.QLabel(self.chart_Page)
        self.label_8.setGeometry(QtCore.QRect(260, 150, 60, 16))
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.chart_Page)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.btnMenu.toggled['bool'].connect(self.menu_widget.setVisible) # type: ignore
        self.btnMenu.toggled['bool'].connect(self.icon_menu_widget.setHidden) # type: ignore
        self.pushButton_5.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.pushButton_12.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.btnCustomer.toggled['bool'].connect(self.iconCustomer.setChecked)
        self.iconCustomer.toggled['bool'].connect(self.btnCustomer.setChecked)
        self.btnEmployee.toggled['bool'].connect(self.iconEmployee.setChecked)
        self.iconEmployee.toggled['bool'].connect(self.btnEmployee.setChecked)
        self.btnPets.toggled['bool'].connect(self.iconPets.setChecked)
        self.iconPets.toggled['bool'].connect(self.btnPets.setChecked)
        self.btnChart.toggled['bool'].connect(self.iconChart.setChecked)
        self.iconChart.toggled['bool'].connect(self.btnChart.setChecked)
        self.btnHome.toggled['bool'].connect(self.iconHome.setChecked)
        self.iconHome.toggled['bool'].connect(self.btnHome.setChecked)
        self.btnService.toggled['bool'].connect(self.iconService.setChecked)
        self.iconService.toggled['bool'].connect(self.btnService.setChecked)
        self.btnMedicine.toggled['bool'].connect(self.iconMedicine.setChecked)
        self.iconMedicine.toggled['bool'].connect(self.btnMedicine.setChecked)
        self.btnPhieuNhap.toggled['bool'].connect(self.iconPhieuNhap.setChecked)
        self.iconPhieuNhap.toggled['bool'].connect(self.btnPhieuNhap.setChecked)
        
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phòng khám thú y"))
        self.label.setText(_translate("MainWindow", "SideBar"))
        self.btnHome.setText(_translate("MainWindow", "Trang chủ"))
        self.btnCustomer.setText(_translate("MainWindow", "Khách hàng"))
        self.btnPets.setText(_translate("MainWindow", "Thú nuôi"))
        self.btnEmployee.setText(_translate("MainWindow", "Nhân viên"))
        self.btnPhieuNhap.setText(_translate("MainWindow", "Phiếu nhập"))
        self.btnMedicine.setText(_translate("MainWindow", "Dược phẩm"))
        self.btnService.setText(_translate("MainWindow", "Dịch vụ"))
        self.btnChart.setText(_translate("MainWindow", "Doanh thu"))
        self.pushButton_12.setText(_translate("MainWindow", "Thoát"))
        self.label_4.setText(_translate("MainWindow", "Home"))
        self.label_5.setText(_translate("MainWindow", "Customer"))
        self.label_6.setText(_translate("MainWindow", "Pets"))
        self.label_8.setText(_translate("MainWindow", "Chart"))
        self.icon_menu_widget.hide()
        
        self.home_form = home.Ui_Form()
        self.home_form.setupUi(self.home_Page)

        self.nv_form = nv.Ui_Form()
        self.nv_form.setupUi(self.employee_page)

        self.dv_form = dv.Ui_Form()
        self.dv_form.setupUi(self.service_Page)

        self.pn_form = pn.Ui_Form()
        self.pn_form.setupUi(self.phieunhap_page)

        self.dp_form = dp.Ui_Form()
        self.dp_form.setupUi(self.medicine_page)

        self.kh_form = kh.Ui_Form()
        self.kh_form.setupUi(self.customer_Page)

        self.tn_form = tn.Ui_Form()
        self.tn_form.setupUi(self.pets_Page)

        self.eventHandling()
        self.dv_form.btnAdd.clicked.connect(self.show_add_dialog)

    def showHome_Pages(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def showCustomer_Pages(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def showPets_Pages(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def showEmployee_Pages(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def showPhieuNhap_Pages(self):
        self.stackedWidget.setCurrentIndex(4)

    def showMedicine_Pages(self):
        self.stackedWidget.setCurrentIndex(5)

    def showService_Pages(self):
        self.stackedWidget.setCurrentIndex(6)

    def showChart_Pages(self):
        self.stackedWidget.setCurrentIndex(7)
    
    def show_add_dialog(self):
        dialog = QtWidgets.QDialog()
        add_dialog_ui = Ui_add_service_dialog()
        add_dialog_ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def loadServiceData(self):
        dao = serviceDAO()
        services = dao.getAllServices()
        row = 0
        self.dv_form.table_service.setRowCount(len(services))
        for service in services:
            self.dv_form.table_service.setItem(row, 0, QtWidgets.QTableWidgetItem(str(service.getMaDV())))
            self.dv_form.table_service.setItem(row, 1, QtWidgets.QTableWidgetItem(service.getTen()))
            self.dv_form.table_service.setItem(row, 2, QtWidgets.QTableWidgetItem(str(service.getGia())))
            row = row +1

    # Xử lý giao diện
    def eventHandling(self):
        self.btnEmployee.clicked.connect(self.showEmployee_Pages)
        self.btnCustomer.clicked.connect(self.showCustomer_Pages)
        self.btnPets.clicked.connect(self.showPets_Pages)
        self.btnChart.clicked.connect(self.showChart_Pages)
        self.btnHome.clicked.connect(self.showHome_Pages)
        self.btnService.clicked.connect(self.showService_Pages)
        self.btnPhieuNhap.clicked.connect(self.showPhieuNhap_Pages)
        self.btnMedicine.clicked.connect(self.showMedicine_Pages)
        self.iconEmployee.clicked.connect(self.showEmployee_Pages)
        self.iconCustomer.clicked.connect(self.showCustomer_Pages)
        self.iconPets.clicked.connect(self.showPets_Pages)
        self.iconChart.clicked.connect(self.showChart_Pages)
        self.iconHome.clicked.connect(self.showHome_Pages)
        self.iconService.clicked.connect(self.showService_Pages)
        self.iconPhieuNhap.clicked.connect(self.showPhieuNhap_Pages)
        self.iconMedicine.clicked.connect(self.showMedicine_Pages)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
