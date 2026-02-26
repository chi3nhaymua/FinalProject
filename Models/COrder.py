from datetime import datetime
from CBook import Book
from CBookList import BookList
from CUser import user


class Order:
    def __init__(self, order_id, user, book, borrow_date, return_date, status,price):
        self.order_id = order_id
        self.user = user
        self.book = book
        self.borrow_date = datetime.strptime(borrow_date, "%Y-%m-%d")
        self.return_date = datetime.strptime(return_date, "%Y-%m-%d")
        self.status = status
        self.price = price


    def to_dict(self):
        return {
            'order_id': self.order_id,
            'user': self.user.to_dict(),
            'book': self.book.to_dict(),
            'borrow date': self.borrow_date.strftime("%Y-%m-%d"),
            'return date': self.return_date.strftime("%Y-%m-%d"),
            'status': self.status,
            'price': self.price
        }

    def calculate_total_price(self):
        days = (self.return_date - self.borrow_date).days
        return self.book.price * days

    def update_status(self, actual_return_date=None):
        today = datetime.now()

        if actual_return_date:
            self.return_date = actual_return_date
            self.status = "Đã trả"
        else:
            if today > self.return_date:
                self.status = "Quá hạn"
            else:
                self.status = "Đang mượn"
        return self.status

    def get_user_info(self):
        return self.user.to_dict()

    def get_book_detail(self, book_id):
        return {

                "title": self.book.book_name,
                "borrow_date": self.borrow_date.strptime("%Y-%m-%d"),
                "return_date": self.return_date.strptime("%Y-%m-%d"),
                "status": self.status,
                "price": self.book.price,
                "total_price": (self.return_date - self.borrow_date).days * self.book.price
                }

    def __str__(self):
        return(f"Mã đơn hàng: {self.order_id}, Khách hàng: {self.user.user_loginname}, "
               f"Tên sách: {self.book.book_name}, Ngày mượn: {self.borrow_date},"
               f"Trạng thái: {self.status}")

# user = user('U001','HongPhuc', 'Phuc', '121207', '0972750970', 'phucnthk25416@st.uel.edu.vn', 'Ho Chi Minh', 'Sinhvien')
# book = Book('B009', 'Nếu Biết Trăm Năm Là Hữu Hạn','Phạm Lữ Ân','Tản Văn','2012','10000','2')
# order1 = Order('O001', user, book, '2026-02-10','2026-02-20','Quá hạn','10000')
# #
# # print(order1)
# # print('Tổng tiền: ', order1.calculate_total_price())
# # print('Trạng thái: ', order1.update_status())
# print(order1.to_dict())
# print(order1.calculate_total_price())

