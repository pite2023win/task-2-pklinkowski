import logging as log

class Bank:
    num_of_banks = 0

    def __init__(self, name):
        self.num_of_clients = 0
        self.clients = []
        self.name = name
        Bank.num_of_banks += 1

    def __str__(self):
        info = "Bank {}, Number of clients: {}\nClients:\n".format(self.name, self.num_of_clients)
        for client in self.clients:
            info += "{}. ".format(self.clients.index(client) + 1) + str(client) + "\n"
        return info

    def add_client(self, client, balance = 0):
        self.clients.append(client)
        self.num_of_clients += 1
        client.bank = self
        client.balance = balance
    
    def __del__(self):
        Bank.num_of_banks -= 1
        log.info("Bank {} has been closed".format(self.name))

    @staticmethod
    def calculate():
        return Bank.num_of_banks
    
    def save_to_file(self):
        with open("data.txt", "a") as f:
            f.write(str(self))

class Client:
    num_of_people = 0

    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname
        self.balance = 0
        self.bank = ""
        Client.num_of_people += 1


    def __str__(self):
        return "{} {}, Balance: {}".format(self.first_name, self.surname, self.balance)

    def operation(func):
        def wrapper(self, value):
            log.info("{} {} wants to make {} operation for {}$".format(self.first_name, self.surname, func.__name__, value))
            func(self, value)
            log.info("After {} operation {} {} have {}$ in the bank.".format(func.__name__, self.first_name, self.surname, self.balance))
            if self.balance < 0:
                log.info("{} {} have {}$ of debt".format(self.first_name, self.surname, self.balance))
        return wrapper

    @operation
    def cash_input(self, value):
        self.balance += value

    @operation
    def withdraw(self, value):
        if self.balance + 1000 < value:
            log.error("{} can't withdraw that much money".format(self.first_name))
        else:
            self.balance -= value

    def transfer(self, recipient, value):
        if recipient.bank != self.bank:
            value += 10
            log.info("There is a 10$ fee for transfering money to another bank")
        if self.balance < value:
            log.error("{} don't have enough money to transfer".format(self.first_name))
        else:
            self.balance -= value
            recipient.balance += value
            log.info("{} have transferred {}$ to {} {}".format(self.first_name, value, recipient.first_name, recipient.surname))
    
if __name__ == "__main__":
    def main():
        log.basicConfig(level=log.INFO)
        Bank1 = Bank("ING")
        Bank2 = Bank("PKO")
        John =  Client("John", "Smith")
        Bob = Client("Bob", "Jones")
        Alice = Client("Alice", "Cooper")
        Martin = Client("Martin", "King")
        Kyle = Client("Kyle", "Walker")
        Jack = Client("Jack", "Daniels")
        Bank1.add_client(John)
        Bank1.add_client(Bob, 10000)
        Bank1.add_client(Martin, 5000)
        Bank2.add_client(Alice, 5000)
        Bank2.add_client(Kyle, 10000)
        Bank2.add_client(Jack, 1000)
        John.cash_input(1000)
        Kyle.cash_input(500)
        Martin.cash_input(1000)
        John.withdraw(500)
        John.transfer(Bob, 200)
        Bob.transfer(Alice, 5000)
        Kyle.transfer(Alice, 1000)
        Alice.withdraw(15000)
        Alice.withdraw(11500)
        Jack.withdraw(1000)
        print('\nNumber of banks: {}'.format(Bank.calculate()))
        print('Number of clients in all banks: {}\n'.format(Client.num_of_people))
        print(Bank1)
        print(Bank2)
        Bank1.save_to_file()
        Bank2.save_to_file()
    
    main()









