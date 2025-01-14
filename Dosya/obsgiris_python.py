# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'obsgiris.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_main(object):
    def setupUi(self, Form_main):
        Form_main.setObjectName("Form_main")
        Form_main.resize(1600, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_main.sizePolicy().hasHeightForWidth())
        Form_main.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        Form_main.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/amasyauniico/amasyauni.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_main.setWindowIcon(icon)
        Form_main.setStyleSheet("#form_main\n"
"{background-image: url(:/ana_arkaplan/full_arka_plan.jpg);\n"
"}")
        self.widget_giris = QtWidgets.QWidget(Form_main)
        self.widget_giris.setGeometry(QtCore.QRect(0, 0, 1600, 1000))
        self.widget_giris.setStyleSheet("#widget_giris {\n"
"    border: 2px solid #ccc; /* Kenarlık rengini ve kalınlığını ayarla */\n"
"    border-radius: 5px; /* Köşeleri yuvarla */\n"
"    padding: 10px; /* İçeriği kenarlardan ayır */\n"
"    border-image: url(:/arkaplan/ic_arkaplan.jpg);\n"
"}\n"
"")
        self.widget_giris.setObjectName("widget_giris")
        self.widget_ic = QtWidgets.QWidget(self.widget_giris)
        self.widget_ic.setGeometry(QtCore.QRect(430, 350, 741, 521))
        self.widget_ic.setStyleSheet("#widget_ic {\n"
"    background-color: #22222; /* Arka plan rengini koyu gri olarak ayarla */\n"
"    border: 2px solid #555555; /* Kenarlık rengini ve kalınlığını ayarla */\n"
"    border-radius: 5px; /* Köşeleri yuvarla */\n"
"    padding: 10px; /* İçeriği kenarlardan ayır */\n"
"    color: #cccccc; /* Yazı rengini ayarla */\n"
"}\n"
"")
        self.widget_ic.setObjectName("widget_ic")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_ic)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 621, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.lineEdit_email_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_email_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_email_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit_email_2.setFont(font)
        self.lineEdit_email_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_email_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #5e72e4; /* Kenarlık rengini değiştirin */\n"
"    border-radius: 15px;  /* Daha yuvarlak kenarlar için değeri artırın */\n"
"    padding: 10px; /* Metin içeriğinin kenarlardan içeriye olan uzaklığını belirler */\n"
"    font-size: 20px; /* Metin fontunun boyutunu biraz daha büyütün */\n"
"    color: #333; /* Metin rengini belirler */\n"
"    background-color: #f8f9fe; /* Arka plan rengini belirler */\n"
"}\n"
"")
        self.lineEdit_email_2.setText("")
        self.lineEdit_email_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_email_2.setObjectName("lineEdit_email_2")
        self.verticalLayout_8.addWidget(self.lineEdit_email_2)
        self.lineEdit_sifre_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_sifre_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_sifre_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit_sifre_4.setFont(font)
        self.lineEdit_sifre_4.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #5e72e4; /* Kenarlık rengini değiştirin */\n"
"    border-radius: 15px;  /* Daha yuvarlak kenarlar için değeri artırın */\n"
"    padding: 10px; /* Metin içeriğinin kenarlardan içeriye olan uzaklığını belirler */\n"
"    font-size: 20px; /* Metin fontunun boyutunu biraz daha büyütün */\n"
"    color: #333; /* Metin rengini belirler */\n"
"    background-color: #f8f9fe; /* Arka plan rengini belirler */\n"
"}\n"
"")
        self.lineEdit_sifre_4.setText("")
        self.lineEdit_sifre_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_sifre_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_sifre_4.setObjectName("lineEdit_sifre_4")
        self.verticalLayout_8.addWidget(self.lineEdit_sifre_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_ogrenci_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.radioButton_ogrenci_4.setFont(font)
        self.radioButton_ogrenci_4.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(225, 225, 225);")
        self.radioButton_ogrenci_4.setObjectName("radioButton_ogrenci_4")
        self.horizontalLayout_4.addWidget(self.radioButton_ogrenci_4)
        self.radioButton_akademisyen_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.radioButton_akademisyen_4.setFont(font)
        self.radioButton_akademisyen_4.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(225, 225, 225);")
        self.radioButton_akademisyen_4.setObjectName("radioButton_akademisyen_4")
        self.horizontalLayout_4.addWidget(self.radioButton_akademisyen_4)
        self.radioButton_ogrenciisleri_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.radioButton_ogrenciisleri_4.setFont(font)
        self.radioButton_ogrenciisleri_4.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(225, 225, 225);")
        self.radioButton_ogrenciisleri_4.setObjectName("radioButton_ogrenciisleri_4")
        self.horizontalLayout_4.addWidget(self.radioButton_ogrenciisleri_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.label_giris_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_giris_2.setFont(font)
        self.label_giris_2.setText("")
        self.label_giris_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_giris_2.setObjectName("label_giris_2")
        self.verticalLayout_8.addWidget(self.label_giris_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.pushButton_giris_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_giris_2.sizePolicy().hasHeightForWidth())
        self.pushButton_giris_2.setSizePolicy(sizePolicy)
        self.pushButton_giris_2.setMinimumSize(QtCore.QSize(100, 55))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_giris_2.setFont(font)
        self.pushButton_giris_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_giris_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(85, 85, 255);\n"
"    color: rgb(241, 241, 241);\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 15px;\n"
"    font: 87 15pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #88b8d6; /* Biraz daha koyu mavi tonu */\n"
"}\n"
"")
        self.pushButton_giris_2.setObjectName("pushButton_giris_2")
        self.verticalLayout_3.addWidget(self.pushButton_giris_2)
        self.label_2 = QtWidgets.QLabel(self.widget_giris)
        self.label_2.setGeometry(QtCore.QRect(700, 50, 191, 161))
        self.label_2.setStyleSheet("border-image: url(:/amasyaunipng/amasyauni.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.widget_giris)
        self.label_8.setGeometry(QtCore.QRect(340, 150, 981, 201))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 30pt \"Arial Black\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form_main)
        QtCore.QMetaObject.connectSlotsByName(Form_main)

    def retranslateUi(self, Form_main):
        _translate = QtCore.QCoreApplication.translate
        Form_main.setWindowTitle(_translate("Form_main", "OBS"))
        self.label_7.setText(_translate("Form_main", "Hoş Geldiniz"))
        self.radioButton_ogrenci_4.setText(_translate("Form_main", "Öğrenci"))
        self.radioButton_akademisyen_4.setText(_translate("Form_main", "Akademisyen"))
        self.radioButton_ogrenciisleri_4.setText(_translate("Form_main", "Öğrenci İşleri"))
        self.pushButton_giris_2.setText(_translate("Form_main", "Giriş yap"))
        self.label_8.setText(_translate("Form_main", "Amasya Üniversitesi Bilgi Sistemi"))
import ikonlar_ogrenci_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_main = QtWidgets.QWidget()
    ui = Ui_Form_main()
    ui.setupUi(Form_main)
    Form_main.show()
    sys.exit(app.exec_())
