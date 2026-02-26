from CBook import Book
from CBookList import BookList
from CUser import user
from CUserList import UserList
from COrder import Order
from JsonFactory import JsonFileFactory
from datetime import datetime

class OrderList:
    def __init__(self):
        self.bigorder_id = 0

        self.orderlist = []
        self.fileorder = 'data/Order.json'
        self.load_order()

    def load_order(self):
        data = JsonFileFactory.read_data(self.fileorder)
        self.orderlist = []

        for item in data: #Đã chuyển từ dict về object vì load lên cần lấy dữ liệu dict từ json chuyển thành object
            u = user(
                item['user']['user_id'],
                item['user']['user_loginname'],
                item['user']['user_name'],
                item['user']['user_password'],
                item['user']['user_email'],
                item['user']['user_phone'],
                item['user']['user_address'],
                item['user']['user_role']
            )

            b = Book(
                item['book']['book_id'],
                item['book']['book_name'],
                item['book']['book_author'],
                item['book']['book_type'],
                item['book']['published_year'],
                item['book']['book_price'],
                item['book']['book_quantity']
            )

            o = Order(
                item['order_id'],
                u,
                b,
                item['borrow_date'],
                item['return_date'],
                item['status'],
                item['price']
            )
            self.orderlist.append(o)

        if self.orderlist:
            self.bigorder_id = max(o.order_id for o in self.orderlist)

    def save_order(self): #Chuyển lại từ object --> dict để lưu vào json
        data = [o.to_dict() for o in self.orderlist]
        JsonFileFactory.write_data(self.fileorder,data)

    def get_all_orders(self):
        return self.orderlist

    def add_order(self, order):
        self.orderlist.append(order)
        self.save_order()

    def remove_order(self, order_id):
        original_len = len(self.orderlist)
        self.orderlist = [o for o in self.orderlist if str(o.order_id) != str(order_id)]
        if len(self.orderlist) < original_len:
            self.save_order()  # Lưu lại sau khi xóa
            return "Xóa thành công."
        return "Không tìm thấy ID để xóa."

    def find_order_by_id (self, order_id):
        for o in self.orderlist:
            if str(o.order_id) == str(order_id):
                return o
        return None

    def find_order_by_name (self, book_name):
        search_name = book_name.lower()
        results = [o for o in self.orderlist if o.book.book_name.lower() == search_name]
        return results if results else None

    def find_order_by_bookid(self, book_id):
        for o in self.orderlist:
            if str(o.book.book_id) == str(book_id):
                return o  # trả về object Order
        return None

    def find_order_by_status(self, status):
        search_status = str(status).lower()
        results = [o for o in self.orderlist if str(o.status).lower() == search_status]
        return results

