
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
                               QMessageBox)
from PySide6.QtCore import Qt
from client_manager import ClientManager

class ClientApp(QWidget):
    def __init__(self):
        super().__init__()

        self.manager = ClientManager()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Gestão de Clientes")

        self.layout = QVBoxLayout()

        self.form_layout = QHBoxLayout()
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Nome")
        self.telefone_input = QLineEdit(self)
        self.telefone_input.setPlaceholderText("Telefone")
        self.cpf_input = QLineEdit(self)
        self.cpf_input.setPlaceholderText("CPF")
        
        self.endereco_input = QLineEdit(self)
        self.endereco_input.setPlaceholderText("Endereço")
        self.bairro_input = QLineEdit(self)
        self.bairro_input.setPlaceholderText("Bairro")
        self.cidade_input = QLineEdit(self)
        self.cidade_input.setPlaceholderText("Cidade - UF")
        self.cep_input = QLineEdit(self)
        self.cep_input.setPlaceholderText("CEP")
        self.obs_input = QLineEdit(self)
        self.obs_input.setPlaceholderText("Obs")
        

        self.form_layout.addWidget(self.name_input)
        self.form_layout.addWidget(self.telefone_input)
        self.form_layout.addWidget(self.cpf_input)
        self.form_layout.addWidget(self.endereco_input)
        self.form_layout.addWidget(self.bairro_input)
        self.form_layout.addWidget(self.cidade_input)
        self.form_layout.addWidget(self.cep_input)
        self.form_layout.addWidget(self.obs_input)

        self.layout.addLayout(self.form_layout)

        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Adicionar", self)
        self.add_button.clicked.connect(self.add_client)
        self.remove_button = QPushButton("Remover", self)
        self.remove_button.clicked.connect(self.remove_client)
        self.search_button = QPushButton("Pesquisar", self)
        self.search_button.clicked.connect(self.search_client)
        self.update_button = QPushButton("Atualizar", self)
        self.update_button.clicked.connect(self.update_client)

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.remove_button)
        self.button_layout.addWidget(self.search_button)
        self.button_layout.addWidget(self.update_button)

        self.layout.addLayout(self.button_layout)
        
        self.client_table = QTableWidget()
       
        self.client_table.setColumnCount(8)
        
        
      
        self.client_table.setHorizontalHeaderLabels(
            ["Nome", "Telefone", "CPF", "Endereço", 
             "Bairro", "Cidade - UF", "CEP", "Obs"]
             )
        
        self.layout.addWidget(self.client_table)

        self.setLayout(self.layout)
        self.update_table()

    def add_client(self):
        client_name = self.name_input.text()
        telefone = self.telefone_input.text()
        cpf = self.cpf_input.text()
        endereco = self.endereco_input.text()
        bairro = self.bairro_input.text()
        cidade = self.cidade_input.text()
        cep = self.cep_input.text()
        obs = self.obs_input.text()
        
        

        # if not telefone.isnumeric():
        #     QMessageBox.warning(self,"erro","telefone aceita apenas numeros")
        #     return client_name
        def verificar(entrada, valores_permitidos):
            entrada_set = set(entrada)
            if entrada_set.issubset(valores_permitidos):
                return True
            else:
                    return False
        valores_permitidos = set("0123456789()-.")
        
        if client_name and telefone and cpf and endereco and bairro and cidade and cep and obs:
            client = {
                "name": client_name, "telefone": telefone, "cpf": cpf,
                "endereco": endereco, "bairro": bairro, "cidade": cidade,
                "cep": cep, "obs": obs
                }

            entrada = telefone + cep + cpf
            
            if verificar(entrada,valores_permitidos):
                
                self.manager.add_client(client)
                self.update_table()
                self.clear_form()

            else:
                QMessageBox.warning(self,'erro','entradas invalidas(Tel,cep,cpf)')
                return client_name

            
        else:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios")

    def remove_client(self):
        client_name = self.name_input.text()
        if client_name:
            self.manager.remove_client(client_name)
            self.update_table()
            self.clear_form()
        else:
            QMessageBox.warning(self, "Erro", "Nome é obrigatório")

    def search_client(self):
        client_name = self.name_input.text()
        client = self.manager.search_client(client_name)
        if client:
            self.name_input.setText(client['name'])
            self.telefone_input.setText(client['telefone'])
            self.cpf_input.setText(client['cpf'])
            self.endereco_input.setText(client['endereco'])
            self.bairro_input.setText(client['bairro'])
            self.cidade_input.setText(client['cidade'])
            self.cep_input.setText(client['cep'])
            self.obs_input.setText(client['obs'])
        else:
            QMessageBox.warning(self, "Erro", "Cliente não encontrado")

    
    def update_client(self):
        client_name = self.name_input.text()
        telefone = self.telefone_input.text()
        cpf = self.cpf_input.text()
        endereco = self.endereco_input.text()
        bairro = self.bairro_input.text()
        cidade = self.cidade_input.text()
        cep = self.cep_input.text()
        obs = self.obs_input.text()

        def verificar(entrada, valores_permitidos):
            entrada_set = set(entrada)
            if entrada_set.issubset(valores_permitidos):
                return True
            else:
                    return False
        valores_permitidos = set("0123456789()-.")

        if client_name and telefone and cpf and endereco and bairro and cidade and cep and obs:
            updated_client = {
                "name": client_name, "telefone": telefone, "cpf": cpf,
                "endereco": endereco, "bairro": bairro, "cidade": cidade,
                "cep": cep, "obs": obs
                }
            entrada = telefone + cep + cpf
            if verificar(entrada, valores_permitidos):

                if self.manager.update_client(client_name, updated_client):
                    self.update_table()
                    self.clear_form()
                else:
                    QMessageBox.warning(self, "Erro", "Cliente não encontrado")
            else:
                QMessageBox.warning(self,'erro','entradas invalidas(Tel,cep,cpf)')
                return client_name
        else:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios")

    def update_table(self):
        self.client_table.setRowCount(len(self.manager.clients))
        for row, client in enumerate(self.manager.clients):
            
            obs_item = QTableWidgetItem(client['obs'])
            obs_item.setTextAlignment(Qt.AlignTop | Qt.AlignCenter)
            obs_item.font()

            self.client_table.setItem(row, 0, QTableWidgetItem(client['name']))
            self.client_table.setItem(row, 1, QTableWidgetItem(client['telefone']))
            self.client_table.setItem(row, 2, QTableWidgetItem(client['cpf']))
            self.client_table.setItem(row, 3, QTableWidgetItem(client['endereco']))
            self.client_table.setItem(row, 4, QTableWidgetItem(client['bairro']))
            self.client_table.setItem(row, 5, QTableWidgetItem(client['cidade']))
            self.client_table.setItem(row, 6, QTableWidgetItem(client['cep']))
            self.client_table.setItem(row, 7, obs_item)
            

            self.client_table.setColumnWidth(7,540)
            self.client_table.setRowHeight(row,300)
            # self.client_table.setcol

    def clear_form(self):
        self.name_input.clear()
        self.telefone_input.clear()
        self.cpf_input.clear()
        self.endereco_input.clear()
        self.bairro_input.clear()
        self.cidade_input.clear()
        self.cep_input.clear()
        self.obs_input.clear()

    
    