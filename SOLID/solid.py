"""
SOLID Principles
1. Single Responsiblity
Separted Order from Payment

2. Open/Closed
Designed an Abstract class for payment Open for extending and closed for modification

3. Liskov Substitution
We needed to have email in PaypalPaymentProcessor
so we needed to change the abstract class prevent violation Liskov Substitution

4. Interface Segregation

5. Dependancy Inversion
"""

from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class AbstractPaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        raise NotImplementedError
    
class AbstractAuthPaymentProcessor(AbstractPaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        raise NotImplementedError

class CreditPaymentProcessor(AbstractPaymentProcessor):
    def __init__(self, security_code) -> None:
        self.security_code = security_code
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class DebitPaymentProcessor(AbstractAuthPaymentProcessor):
    def __init__(self, security_code) -> None:
        self.security_code = security_code
    
    def auth_sms(self, code):
        print(f"Verifying SMS {code}")
        self.verified = True

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(AbstractAuthPaymentProcessor):
    def __init__(self, email) -> None:
        self.email = email
    
    def auth_sms(self, code):
        print(f"Verifying SMS {code}")
        self.verified = True
    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying email: {self.email}")
        order.status = "paid"
        
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2 , 5)

print(order.total_price())
payment_processor = PaypalPaymentProcessor("markdownpro@gmail.com")
payment_processor.pay(order)










