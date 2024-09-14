import json
import os

class ClientManager:
    def __init__(self, filename='clients.json'):
        self.filename = filename
        self.clients = self.load_clients()

    def add_client(self, client):
        self.clients.append(client)
        self.save_clients()

    def remove_client(self, client_name):
        self.clients = [c for c in self.clients if c['name'] != client_name]
        self.save_clients()

    def search_client(self, client_name):
        search_terms = client_name.strip().lower()
        for client in self.clients:
            if search_terms in client['name'].lower():
                return client
        return None

    def update_client(self, client_name, updated_client):
        for idx, client in enumerate(self.clients):
            if client['name'] == client_name:
                self.clients[idx] = updated_client
                self.save_clients()
                return True
        return False

    def save_clients(self):
        with open(self.filename, 'w') as file:
            json.dump(self.clients, file, indent=4, ensure_ascii=False)

    def load_clients(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return [] 