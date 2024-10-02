
from PySide6 import QtCore, QtGui, QtWidgets 
from client_manager import ClientManager



class Ui_QListView(object):
    def setupUi(self, QListView):
        QListView.setObjectName("QListView")
        QListView.resize(357, 300)
        self.centralwidget = QtWidgets.QWidget(QListView)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(45, 34, 256, 192))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(141, 238, 75, 23))
        self.pushButton.setObjectName("pushButton")
        QListView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QListView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 357, 21))
        self.menubar.setObjectName("menubar")
        QListView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QListView)
        self.statusbar.setObjectName("statusbar")
        QListView.setStatusBar(self.statusbar)

        self.retranslateUi(QListView)
        QtCore.QMetaObject.connectSlotsByName(QListView)

    def retranslateUi(self, QListView):
        _translate = QtCore.QCoreApplication.translate
        QListView.setWindowTitle(_translate("QListView", "List View"))
        self.pushButton.setText(_translate("QListView", "Selected"))

class ListView(QtWidgets.QMainWindow, Ui_QListView):
    def __init__(self):
        super().__init__()
        self.manager = ClientManager()
        self.setupUi(self)
        
        self.pushButton.setEnabled(False)
        self.model = QtGui.QStandardItemModel()
        self.update_list()

        # name_ = self.manager.clients        
        # for x in name_:          
        #     model.appendRow(QtGui.QStandardItem(str(x['name'])))
        # self.listView.setModel(model)
        

        self.listView.selectionModel().selectionChanged.connect(
            self.handle_selection_changed
        )
        self.pushButton.clicked.connect(self.handle_clicked)

        
    def update_list(self):
        
        self.manager.clients = self.manager.load_clients()
        self.model.clear() 
        name_ = self.manager.clients
       
        for x in name_:
            self.model.appendRow(QtGui.QStandardItem(str(x['name'])))
        
        self.listView.setModel(self.model)
        

    def handle_selection_changed(self):
        self.pushButton.setEnabled(bool(self.listView.selectedIndexes()))

    def handle_clicked(self):
        for index in self.listView.selectedIndexes():
            item = self.listView.model().itemFromIndex(index)
            print(item.text())
    
