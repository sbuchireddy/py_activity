from abc import ABC, abstractmethod

class PaymentSystem(ABC):
	@abstractmethod
	def process_payment(self,amount):
		pass

class CreditCardPayment(PaymentSystem):
	def process_paymnet(self, amount):
		print(f"Process credit card payment of {amount}")
class UpiPaymnet(PaymentSystem):
	def process_paymnet(self, amount):
		print(f"Processing UPI payment of {amount}")
payment = PaymentSystem()

'''

from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class UpiPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Processing UPI payment of {amount}")

credit = CreditCardPayment()
credit.process_payment(100)

upi = UpiPayment()
upi.process_payment(200)
'''
