from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):
    def pay(self, amount):
        print("UPI payment:", amount)


class CardPayment(Payment):
    def pay(self, amount):
        print("Card payment:", amount)


def checkout(payment, amount):
    payment.pay(amount)


checkout(UpiPayment(), 500)
checkout(CardPayment(), 1000)