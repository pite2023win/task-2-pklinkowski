class Bank():
    def __init__(self):
        self.num_of_clients = 0
        self.clients = []

    def __str__(self):
        for client in self.clients:
            print(client)

    def add_client(self, client, balance = 0):
        self.clients.append(client)
        self.num_of_clients += 1
        client.bank = self
        client.balance = balance

class Client():
    bank = ""

    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname
        self.balance = 0


    def __str__(self):
        print("Client: {} {}\nBalance: {}".format(first_name, surname, balance))

    def cash_input(self, value):
        self.balance += value
        info = "You have added {}$ to your account and now have {}$.".format(value, self.balance)
        print(info)

    def withdraw(self, value):
        if self.balance + 1000 < value:
            print("{} can't withdraw that much money".format(self.first_name))
        elif self.balance < value:
            self.balance -= value
            print("{} have withdrawn {}$ from your account and now have {}$ of debt".format(self.first_name, value, self.balance))
        else:
            self.balance -= value
            print("{} have withdrawn {}$ from your account and now have {}$ left".format(self.first_name, value, self.balance))
    
    def transfer(self, recipient, value):
        if recipient.bank != self.bank:
            value += 10
            print("There is a 10$ fee for transfering money to another bank")
        if self.balance < value:
            print("{} don't have enough money to transfer".format(self.first_name))
        else:
            self.balance -= value
            recipient.balance += value
            print("{} have transferred {}$ to {} {}".format(self.first_name, value, recipient.first_name, recipient.surname))


if __name__ == "__main__":
    def main():
        Bank1 = Bank()
        Bank2 = Bank()
        John =  Client("John", "Smith")
        Bob = Client("Bob", "Jones")
        Alice = Client("Alice", "Cooper")
        Bank1.add_client(John)
        Bank1.add_client(Bob, 10000)
        Bank2.add_client(Alice, 5000)

        John.cash_input(1000)
        John.withdraw(500)
        John.transfer(Bob, 200)

        Bob.transfer(Alice, 5000)
        Alice.withdraw(15000)

        Alice.withdraw(7000)
    
    main()

