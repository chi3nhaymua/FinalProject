from COrder import order
from CBook import Book
from JsonFactory import JsonFileFactory

class COrderList:
    def __init__(self):
        self.orders = []
        self.file = "data/orders.json"
        self.load_order()

    def load_order(self):
        data = JsonFileFactory.read_data(self.file)
        self.orders = []
        for item in data:
            o = order(
                item["order_id"],
                item["user"],
                item["Booklist"]
                item["borrow_date"],
                item["return_date"],
                item["status"],
            )
            self.orders.append(o)
    
    def save_orders(self):
        data = [order.to_dict() for order in self.orders]
        JsonFileFactory.write_data(self.file, data)

    def show_order(self):
        if not self.orders:
            print('Không có đơn hàng')
            return
        for o in self.orders:
            print(o.to_dict())

    def add_order(self, order):
        self.orders.append(order)

    def delete_order(self, order):
        original_orderslen = len(self.orders)
        self.orders = [o for o in self.orders if str(b.order_id) != str(order_id)]
        if len(self.orders) < original_orderslen:
            self.save_orders()
            return('Xóa thành công')
        return('Không tìm thấy đơn')

    def find_by_id(self,order_id):
        for o in self.order:
            if str(o.order_id) == str(order_id):
                return order
        return None
        
    def find_by_reader(self, reader_id):
        for i in self.orders:
            if str(i.reader_id) == str(reader_id):
                return order
        return None 
    
    def find_by_book(self,book_id):
        for i in self.orders:
            if str(i.book_id) == str(book_id):
                return order
        return None

    def find_by_status(self, status):
        for i in self.orders:
            if str(i.status) == str(status):
                return order
        return None 
        
