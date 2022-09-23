import time
from typing import Tuple

from PyQt5 import QtCore, QtGui, QtWidgets

from Application import Application
from utils.Config import Config


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(30, 10, 331, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_main.setFont(font)
        self.label_main.setObjectName("label_main")
        self.lineEdit_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_a.setEnabled(True)
        self.lineEdit_a.setGeometry(QtCore.QRect(20, 40, 361, 20))
        self.lineEdit_a.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_a.setText("")
        self.lineEdit_a.setFrame(True)
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.lineEdit_b = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_b.setGeometry(QtCore.QRect(20, 70, 361, 20))
        self.lineEdit_b.setText("")
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.lineEdit_population = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_population.setGeometry(QtCore.QRect(20, 100, 361, 20))
        self.lineEdit_population.setText("")
        self.lineEdit_population.setClearButtonEnabled(False)
        self.lineEdit_population.setObjectName("lineEdit_population")

        self.lineEdit_epochs = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_epochs.setGeometry(QtCore.QRect(20, 160, 361, 20))
        self.lineEdit_epochs.setText("")
        self.lineEdit_epochs.setObjectName("lineEdit_epochs")
        self.lineEdit_best_chromosome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_best_chromosome.setGeometry(
            QtCore.QRect(20, 190, 361, 20))
        self.lineEdit_best_chromosome.setText("")
        self.lineEdit_best_chromosome.setObjectName("lineEdit_best_chromosome")
        self.lineEdit_elite_strategy = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_elite_strategy.setGeometry(
            QtCore.QRect(20, 220, 361, 20))
        self.lineEdit_elite_strategy.setText("")
        self.lineEdit_elite_strategy.setObjectName("lineEdit_elite_strategy")
        self.lineEdit_cross_prob = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cross_prob.setGeometry(QtCore.QRect(20, 250, 361, 20))
        self.lineEdit_cross_prob.setText("")
        self.lineEdit_cross_prob.setObjectName("lineEdit_cross_prob")
        self.lineEdit_mutation_prob = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mutation_prob.setGeometry(QtCore.QRect(20, 280, 361, 20))
        self.lineEdit_mutation_prob.setText("")
        self.lineEdit_mutation_prob.setObjectName("lineEdit_mutation_prob")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 340, 161, 21))
        self.label_1.setObjectName("label_1")

        self.result_lbl = QtWidgets.QLabel(self.centralwidget)
        self.result_lbl.setGeometry(QtCore.QRect(20, 550, 161, 21))
        self.result_lbl.setObjectName("result_lbl")

        self.best_result_lbl = QtWidgets.QLabel(self.centralwidget)
        self.result_lbl.setGeometry(QtCore.QRect(20, 560, 200, 200))
        self.result_lbl.setObjectName("best_result_lbl")

        self.comboBox_selection_method = QtWidgets.QComboBox(
            self.centralwidget)
        self.comboBox_selection_method.setGeometry(
            QtCore.QRect(20, 360, 161, 22))
        self.comboBox_selection_method.setObjectName(
            "comboBox_selection_method")
        self.comboBox_cross_method = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_cross_method.setGeometry(QtCore.QRect(20, 410, 161, 22))
        self.comboBox_cross_method.setObjectName("comboBox_cross_method")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 390, 161, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 161, 21))
        self.label_3.setObjectName("label_3")
        self.comboBox_mutation_method = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_mutation_method.setGeometry(
            QtCore.QRect(20, 460, 161, 22))
        self.comboBox_mutation_method.setObjectName("comboBox_mutation_method")
        self.checkBox_maxi = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_maxi.setGeometry(QtCore.QRect(20, 490, 111, 17))
        self.checkBox_maxi.setObjectName("checkBox_maxi")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(20, 520, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_erase = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_erase.setEnabled(True)
        self.pushButton_erase.setGeometry(QtCore.QRect(310, 340, 71, 23))
        self.pushButton_erase.setCheckable(False)
        self.pushButton_erase.setAutoDefault(False)
        self.pushButton_erase.setDefault(False)
        self.pushButton_erase.setFlat(False)
        self.pushButton_erase.setObjectName("pushButton_erase")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(200, 370, 181, 171))
        self.OutputLabel.setObjectName("OutputLabel")
        self.OutputLabel.hasScaledContents()

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit_list = [self.lineEdit_a, self.lineEdit_b, self.lineEdit_population,
                              self.lineEdit_epochs,
                              self.lineEdit_best_chromosome, self.lineEdit_elite_strategy, self.lineEdit_cross_prob,
                              self.lineEdit_mutation_prob]
        SELECTION_METHODS = ['Best', 'Roulette', 'Tournament']
        MUTATION_METHOD = ['Gaussian', "Uniform"]
        CROSS_METHODS = ["Arithmetic", "Heuristic"]
        self.comboBox_mutation_method.addItems(MUTATION_METHOD)
        self.comboBox_selection_method.addItems(SELECTION_METHODS)
        self.comboBox_cross_method.addItems(CROSS_METHODS)
        # ACTIONS
        self.pushButton_erase.pressed.connect(self.eraseFields)
        self.pushButton_start.pressed.connect(self.startButtonPushed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "Genetic Algorithm", "Genetic Algorithm"))
        self.label_main.setText(_translate(
            "MainWindow", "Genetic Algorithm for finding max/min in Beale Function"))
        self.lineEdit_a.setPlaceholderText(
            _translate("MainWindow", "Begin of the range - a"))
        self.lineEdit_b.setPlaceholderText(
            _translate("MainWindow", "Begin of the range - b"))
        self.lineEdit_population.setPlaceholderText(
            _translate("MainWindow", "Population amount"))

        self.lineEdit_epochs.setPlaceholderText(
            _translate("MainWindow", "Epochs amount"))
        self.lineEdit_best_chromosome.setPlaceholderText(
            _translate("MainWindow", "Best and tournament chromosome amount"))
        self.lineEdit_elite_strategy.setPlaceholderText(
            _translate("MainWindow", "Elite strategy %"))
        self.lineEdit_cross_prob.setPlaceholderText(
            _translate("MainWindow", "Cross probability"))
        self.lineEdit_mutation_prob.setPlaceholderText(
            _translate("MainWindow", "Mutation probability"))
        self.label_1.setText(_translate("MainWindow", "Selection method"))
        self.label_2.setText(_translate("MainWindow", "Cross method"))
        self.label_3.setText(_translate("MainWindow", "Mutation method"))
        self.checkBox_maxi.setText(_translate("MainWindow", "Maximization"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_erase.setText(_translate("MainWindow", "Erase"))
        self.OutputLabel.setText(_translate("MainWindow", ""))

    def eraseFields(self):
        for item in self.lineEdit_list:
            item.clear()

    def startButtonPushed(self):
        # gather variables from all fields in GUI
        if self.checkBox_maxi.checkState():
            maximization = True
        else:
            maximization = False

        cross_method = self.comboBox_cross_method.currentText()
        mutation_method = self.comboBox_mutation_method.currentText()
        selection_method = self.comboBox_selection_method.currentText()

        left_limit = self.lineEdit_a.text()
        right_limit = self.lineEdit_b.text()
        number_of_population = self.lineEdit_population.text()
        number_of_eras = self.lineEdit_epochs.text()
        crossover_percent = self.lineEdit_cross_prob.text()
        mutation_percent = self.lineEdit_mutation_prob.text()
        best_chromosome = self.lineEdit_best_chromosome.text()
        elit_strategy_amount = float(self.lineEdit_elite_strategy.text())

        config: Config = Config(
            cross_method=cross_method,
            mutation_method=mutation_method,
            left_limit=float(left_limit),
            selection_method=selection_method,
            right_limit=float(right_limit),
            number_of_population=int(number_of_population),
            number_of_eras=int(number_of_eras),
            crossover_percent=float(crossover_percent),
            mutation_percent=float(mutation_percent),
            tournament_gourps_size=int(best_chromosome),
            maximization=maximization,
            selection_percent=int(best_chromosome) / int(number_of_population),
            elite_percent=elit_strategy_amount
        )
        application = Application(config)
        start = time.time()
        best: Tuple[Tuple[float, float], float] = application.run()
        end = time.time()
        ellapsed_in = end - start
        self.OutputLabel.setText(
            "f(" + "{:.2}".format(best[0][0]) + ", " + "{:.2}".format(best[0][1]) + ")" + "=" + "{:.2}".format(best[1])
            + "\n" + "{:.4}".format(ellapsed_in) + "s"
        )

        print(ellapsed_in)
        self.result_lbl.setText("completed in " + "{:.4}".format(ellapsed_in) + "s")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
