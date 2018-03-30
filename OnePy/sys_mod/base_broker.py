from OnePy.components.order_checker import SubmitOrderChecker
from OnePy.components.order_generator import OrderGenerator
from OnePy.environment import Environment


class BrokerBase(object):
    env = Environment()

    """Docstring for RiskManagerBase. """

    def __init__(self):
        self.env.brokers.update({self.__class__.__name__: self})
        self.checker = SubmitOrderChecker()
        self.order_generator = OrderGenerator()

    def run(self):
        self.generate_order()
        self.submit_order()

    def submit_order(self):
        self.checker.run()

    def generate_order(self):
        self.order_generator.run()

    def cancel_order(self, order):
        pass

    def get_open_orders(self, order_book_id):
        pass

    def get_portfolio(self):
        pass