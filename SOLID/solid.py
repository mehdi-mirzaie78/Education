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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        raise NotImplementedError

class SMSAuth(Authorizer):
    authorized = False
    
    def verify_code(self, code):
        print(f" Verifying code: {code}")
        self.authorized = True 
    def is_authorized(self):
        return self.authorized

class NotRobot(Authorizer):
    authorized = False
    
    def not_robot(self):
        print("Are you a Robot? Naaa...")
        self.authorized = True
        
    def is_authorized(self):
        return self.authorized
class AbstractPaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        raise NotImplementedError
    

class CreditPaymentProcessor(AbstractPaymentProcessor):
    def __init__(self, security_code) -> None:
        self.security_code = security_code
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class DebitPaymentProcessor(AbstractPaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer) -> None:
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(AbstractPaymentProcessor):
    def __init__(self, email, authorizer: Authorizer) -> None:
        self.email = email
        self.authorizer = authorizer
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email: {self.email}")
        order.status = "paid"
        
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2 , 5)

print(order.total_price())
authorizer = NotRobot()
payment_processor = PaypalPaymentProcessor("markdownpro@gmail.com", authorizer)
authorizer.not_robot()
payment_processor.pay(order)










