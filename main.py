class Bank:
    def __init__(self):
        self.clients = []
    
    def add_client(self, client):
        self.clients.append(client)
    def remove_client(self, client):
        self.clients = list(filter(clients, lambda x: x.id != client.id))
    def all_cash(self):
        res = 0 
        for client i self.clients:
            res += client.money
        
        return res