# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 945)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_SelectionLivre = QtWidgets.QWidget()
        self.tab_SelectionLivre.setObjectName("tab_SelectionLivre")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_SelectionLivre)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 781, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_SelectionLivre = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_SelectionLivre.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_SelectionLivre.setObjectName("verticalLayout_SelectionLivre")
        self.labelLivreChoix = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelLivreChoix.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLivreChoix.setObjectName("labelLivreChoix")
        self.verticalLayout_SelectionLivre.addWidget(self.labelLivreChoix)
        self.comboBoxLivreDisponible = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxLivreDisponible.setObjectName("comboBoxLivreDisponible")
        self.verticalLayout_SelectionLivre.addWidget(self.comboBoxLivreDisponible)
        self.ButtonValiderLivre = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonValiderLivre.setObjectName("ButtonValiderLivre")
        self.verticalLayout_SelectionLivre.addWidget(self.ButtonValiderLivre)
        self.tabWidget.addTab(self.tab_SelectionLivre, "")
        self.tab_RechercheChapitre = QtWidgets.QWidget()
        self.tab_RechercheChapitre.setObjectName("tab_RechercheChapitre")
        self.layoutWidget = QtWidgets.QWidget(self.tab_RechercheChapitre)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 2, 1051, 931))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_RechercheChapitre = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_RechercheChapitre.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_RechercheChapitre.setObjectName("verticalLayout_RechercheChapitre")
        self.labelInstructionPage = QtWidgets.QLabel(self.layoutWidget)
        self.labelInstructionPage.setEnabled(True)
        self.labelInstructionPage.setMaximumSize(QtCore.QSize(780, 256))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelInstructionPage.setFont(font)
        self.labelInstructionPage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelInstructionPage.setAutoFillBackground(False)
        self.labelInstructionPage.setTextFormat(QtCore.Qt.AutoText)
        self.labelInstructionPage.setScaledContents(False)
        self.labelInstructionPage.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labelInstructionPage.setIndent(-1)
        self.labelInstructionPage.setObjectName("labelInstructionPage")
        self.verticalLayout_RechercheChapitre.addWidget(self.labelInstructionPage)
        self.lineEditChapitreVoulu = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditChapitreVoulu.setText("")
        self.lineEditChapitreVoulu.setClearButtonEnabled(False)
        self.lineEditChapitreVoulu.setObjectName("lineEditChapitreVoulu")
        self.verticalLayout_RechercheChapitre.addWidget(self.lineEditChapitreVoulu)
        self.ButtonChangerChapitre = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonChangerChapitre.setObjectName("ButtonChangerChapitre")
        self.verticalLayout_RechercheChapitre.addWidget(self.ButtonChangerChapitre)
        self.labelChapitre = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelChapitre.setFont(font)
        self.labelChapitre.setTextFormat(QtCore.Qt.PlainText)
        self.labelChapitre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelChapitre.setWordWrap(True)
        self.labelChapitre.setObjectName("labelChapitre")
        self.verticalLayout_RechercheChapitre.addWidget(self.labelChapitre)
        self.tabWidget.addTab(self.tab_RechercheChapitre, "")
        self.tab_Sauvegarde = QtWidgets.QWidget()
        self.tab_Sauvegarde.setObjectName("tab_Sauvegarde")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_Sauvegarde)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_Sauvegarde = QtWidgets.QVBoxLayout()
        self.verticalLayout_Sauvegarde.setObjectName("verticalLayout_Sauvegarde")
        self.labelSauvegarde = QtWidgets.QLabel(self.tab_Sauvegarde)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelSauvegarde.setFont(font)
        self.labelSauvegarde.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSauvegarde.setObjectName("labelSauvegarde")
        self.verticalLayout_Sauvegarde.addWidget(self.labelSauvegarde)
        self.comboBoxSauvegarde = QtWidgets.QComboBox(self.tab_Sauvegarde)
        self.comboBoxSauvegarde.setObjectName("comboBoxSauvegarde")
        self.comboBoxSauvegarde.addItem("")
        self.comboBoxSauvegarde.addItem("")
        self.comboBoxSauvegarde.addItem("")
        self.verticalLayout_Sauvegarde.addWidget(self.comboBoxSauvegarde)
        self.ButtonChargerSauvegarde = QtWidgets.QPushButton(self.tab_Sauvegarde)
        self.ButtonChargerSauvegarde.setObjectName("ButtonChargerSauvegarde")
        self.verticalLayout_Sauvegarde.addWidget(self.ButtonChargerSauvegarde)
        self.ButtonNouvelleSauvegarde = QtWidgets.QPushButton(self.tab_Sauvegarde)
        self.ButtonNouvelleSauvegarde.setObjectName("ButtonNouvelleSauvegarde")
        self.verticalLayout_Sauvegarde.addWidget(self.ButtonNouvelleSauvegarde)
        self.ButtonSupprimerSauvegarde = QtWidgets.QPushButton(self.tab_Sauvegarde)
        self.ButtonSupprimerSauvegarde.setObjectName("ButtonSupprimerSauvegarde")
        self.verticalLayout_Sauvegarde.addWidget(self.ButtonSupprimerSauvegarde)
        self.verticalLayout_5.addLayout(self.verticalLayout_Sauvegarde)
        self.tabWidget.addTab(self.tab_Sauvegarde, "")
        self.tab_FeuilleAventure = QtWidgets.QWidget()
        self.tab_FeuilleAventure.setObjectName("tab_FeuilleAventure")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_FeuilleAventure)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_FeuilleAventure = QtWidgets.QVBoxLayout()
        self.verticalLayout_FeuilleAventure.setObjectName("verticalLayout_FeuilleAventure")
        self.labelFeuille_Aventure_Titre = QtWidgets.QLabel(self.tab_FeuilleAventure)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelFeuille_Aventure_Titre.setFont(font)
        self.labelFeuille_Aventure_Titre.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFeuille_Aventure_Titre.setObjectName("labelFeuille_Aventure_Titre")
        self.verticalLayout_FeuilleAventure.addWidget(self.labelFeuille_Aventure_Titre)
        self.label_objet = QtWidgets.QLabel(self.tab_FeuilleAventure)
        self.label_objet.setObjectName("label_objet")
        self.verticalLayout_FeuilleAventure.addWidget(self.label_objet)
        self.lineEdit_objets = QtWidgets.QLineEdit(self.tab_FeuilleAventure)
        self.lineEdit_objets.setObjectName("lineEdit_objets")
        self.verticalLayout_FeuilleAventure.addWidget(self.lineEdit_objets)
        self.label_repas = QtWidgets.QLabel(self.tab_FeuilleAventure)
        self.label_repas.setObjectName("label_repas")
        self.verticalLayout_FeuilleAventure.addWidget(self.label_repas)
        self.lineEdit_repas = QtWidgets.QLineEdit(self.tab_FeuilleAventure)
        self.lineEdit_repas.setObjectName("lineEdit_repas")
        self.verticalLayout_FeuilleAventure.addWidget(self.lineEdit_repas)
        self.label_ObjetSpeciaux = QtWidgets.QLabel(self.tab_FeuilleAventure)
        self.label_ObjetSpeciaux.setObjectName("label_ObjetSpeciaux")
        self.verticalLayout_FeuilleAventure.addWidget(self.label_ObjetSpeciaux)
        self.lineEdit_objetsSpeciaux = QtWidgets.QLineEdit(self.tab_FeuilleAventure)
        self.lineEdit_objetsSpeciaux.setObjectName("lineEdit_objetsSpeciaux")
        self.verticalLayout_FeuilleAventure.addWidget(self.lineEdit_objetsSpeciaux)
        self.labelArmesActuek = QtWidgets.QLabel(self.tab_FeuilleAventure)
        self.labelArmesActuek.setObjectName("labelArmesActuek")
        self.verticalLayout_FeuilleAventure.addWidget(self.labelArmesActuek)
        self.comboBoxArmesActuel = QtWidgets.QComboBox(self.tab_FeuilleAventure)
        self.comboBoxArmesActuel.setObjectName("comboBoxArmesActuel")
        self.verticalLayout_FeuilleAventure.addWidget(self.comboBoxArmesActuel)
        self.labelDisciplinesKaiActuel = QtWidgets.QLabel(self.tab_FeuilleAventure)
        self.labelDisciplinesKaiActuel.setObjectName("labelDisciplinesKaiActuel")
        self.verticalLayout_FeuilleAventure.addWidget(self.labelDisciplinesKaiActuel)
        self.comboBoxDisciplinesKaiActuel = QtWidgets.QComboBox(self.tab_FeuilleAventure)
        self.comboBoxDisciplinesKaiActuel.setObjectName("comboBoxDisciplinesKaiActuel")
        self.verticalLayout_FeuilleAventure.addWidget(self.comboBoxDisciplinesKaiActuel)
        self.labelArmes = QtWidgets.QLabel(self.tab_FeuilleAventure)
        self.labelArmes.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labelArmes.setObjectName("labelArmes")
        self.verticalLayout_FeuilleAventure.addWidget(self.labelArmes)
        self.comboBoxArmes = QtWidgets.QComboBox(self.tab_FeuilleAventure)
        self.comboBoxArmes.setObjectName("comboBoxArmes")
        self.verticalLayout_FeuilleAventure.addWidget(self.comboBoxArmes)
        self.labelDisciplinesKai = QtWidgets.QLabel(self.tab_FeuilleAventure)
        self.labelDisciplinesKai.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labelDisciplinesKai.setObjectName("labelDisciplinesKai")
        self.verticalLayout_FeuilleAventure.addWidget(self.labelDisciplinesKai)
        self.comboBoxDisciplinesKai = QtWidgets.QComboBox(self.tab_FeuilleAventure)
        self.comboBoxDisciplinesKai.setObjectName("comboBoxDisciplinesKai")
        self.verticalLayout_FeuilleAventure.addWidget(self.comboBoxDisciplinesKai)
        self.ButtonAjouterFeuilleAventure = QtWidgets.QPushButton(self.tab_FeuilleAventure)
        self.ButtonAjouterFeuilleAventure.setObjectName("ButtonAjouterFeuilleAventure")
        self.verticalLayout_FeuilleAventure.addWidget(self.ButtonAjouterFeuilleAventure)
        self.verticalLayout_3.addLayout(self.verticalLayout_FeuilleAventure)
        self.tabWidget.addTab(self.tab_FeuilleAventure, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>Sélection livres</p></body></html>"))
        self.labelLivreChoix.setText(_translate("MainWindow", "Veuillez choisir le livre voulu !"))
        self.ButtonValiderLivre.setText(_translate("MainWindow", "Valider le livre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SelectionLivre), _translate("MainWindow", "Sélection livres"))
        self.labelInstructionPage.setText(_translate("MainWindow", "Veuillez sélectionner la page voulue"))
        self.ButtonChangerChapitre.setText(_translate("MainWindow", "Rechercher"))
        self.labelChapitre.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_RechercheChapitre), _translate("MainWindow", "Recherche chapitres"))
        self.labelSauvegarde.setText(_translate("MainWindow", "Menu des sauvegardes"))
        self.comboBoxSauvegarde.setItemText(0, _translate("MainWindow", "Sauvegarde 1"))
        self.comboBoxSauvegarde.setItemText(1, _translate("MainWindow", "Sauvegarde 2"))
        self.comboBoxSauvegarde.setItemText(2, _translate("MainWindow", "Sauvegarde 3"))
        self.ButtonChargerSauvegarde.setText(_translate("MainWindow", "Charger"))
        self.ButtonNouvelleSauvegarde.setText(_translate("MainWindow", "Nouvelle sauvegarde"))
        self.ButtonSupprimerSauvegarde.setText(_translate("MainWindow", "Supprimer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Sauvegarde), _translate("MainWindow", "Sauvegardes"))
        self.labelFeuille_Aventure_Titre.setText(_translate("MainWindow", "Vous pouvez changer vos armes et vos disciplines Kai içi !"))
        self.label_objet.setText(_translate("MainWindow", "objets"))
        self.label_repas.setText(_translate("MainWindow", "repas"))
        self.label_ObjetSpeciaux.setText(_translate("MainWindow", "objets spéciaux"))
        self.labelArmesActuek.setText(_translate("MainWindow", "Armes actuels"))
        self.labelDisciplinesKaiActuel.setText(_translate("MainWindow", "Disciplines Kai actuels"))
        self.labelArmes.setText(_translate("MainWindow", "Armes disponibles"))
        self.labelDisciplinesKai.setText(_translate("MainWindow", "Disciplines Kai disponibles"))
        self.ButtonAjouterFeuilleAventure.setText(_translate("MainWindow", "Ajouter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_FeuilleAventure), _translate("MainWindow", "Feuille d\'aventure"))
