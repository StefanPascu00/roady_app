# Form implementation generated from reading ui file '.\roady_gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from roady import Roady


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 578)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.departure_city_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.departure_city_label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.departure_city_label.setObjectName("departure_city_label")
        self.departure_city_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.departure_city_input.setGeometry(QtCore.QRect(100, 20, 113, 21))
        self.departure_city_input.setObjectName("departure_city_input")
        self.destination_city_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.destination_city_input.setGeometry(QtCore.QRect(100, 50, 113, 21))
        self.destination_city_input.setObjectName("destination_city_input")
        self.destination_city_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.destination_city_label.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.destination_city_label.setObjectName("destination_city_label")
        self.fuel_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.fuel_comboBox.setGeometry(QtCore.QRect(10, 90, 68, 22))
        self.fuel_comboBox.setObjectName("fuel_comboBox")
        self.fuel_comboBox.addItem("")
        self.fuel_comboBox.addItem("")
        self.fuel_usage_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.fuel_usage_label.setGeometry(QtCore.QRect(10, 130, 49, 16))
        self.fuel_usage_label.setObjectName("fuel_usage_label")
        self.consum_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.consum_input.setGeometry(QtCore.QRect(70, 130, 51, 21))
        self.consum_input.setObjectName("consum_input")
        self.person_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.person_label.setGeometry(QtCore.QRect(10, 170, 49, 16))
        self.person_label.setObjectName("person_label")
        self.person_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.person_input.setGeometry(QtCore.QRect(70, 170, 31, 21))
        self.person_input.setObjectName("person_input")
        self.calculate_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculate_button.clicked.connect(self.calculate_btn)
        self.calculate_button.setGeometry(QtCore.QRect(94, 300, 131, 61))
        self.calculate_button.setObjectName("calculate_button")
        self.add_return_radio_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.add_return_radio_button.setGeometry(QtCore.QRect(140, 90, 89, 20))
        self.add_return_radio_button.setObjectName("add_return_radio_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.departure_city_label.setText(_translate("MainWindow", "Departure City"))
        self.destination_city_label.setText(_translate("MainWindow", "Destination City"))
        self.fuel_comboBox.setItemText(0, _translate("MainWindow", "Benzina"))
        self.fuel_comboBox.setItemText(1, _translate("MainWindow", "Diesel"))
        self.fuel_usage_label.setText(_translate("MainWindow", "Consum"))
        self.person_label.setText(_translate("MainWindow", "Persoane"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.add_return_radio_button.setText(_translate("MainWindow", "Dus-Intors"))

    def calculate_btn(self):
        departure_city = self.departure_city_input.text()
        destination_city = self.destination_city_input.text()
        number_of_person = self.person_input.text()
        fuel_type = self.fuel_comboBox.currentText()
        fuel_usage = self.consum_input.text()
        roady = Roady(departure_city, destination_city, int(number_of_person), float(fuel_usage), fuel_type)
        price = roady.calculate_price_per_person()
        if self.add_return_radio_button.isEnabled():
            print(price)
        else:
            print(price * 2)


if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
