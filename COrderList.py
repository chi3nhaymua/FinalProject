from COrder import order
from CBook import Book
from JsonFactory import *

class COrderList:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def find_by_reader(self, reader_id):
        return [i for i in self.orders if i.reader_id == reader_id]

    def find_by_book(self,book_id):
        return [i for i in self.orders if i.book_id == book_id]

    def find_by_status(self, status):
        return [i for i in self.orders if i.status == status]
