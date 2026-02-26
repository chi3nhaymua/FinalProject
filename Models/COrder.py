from datetime import datetime
from CBookList import BookList
from CUser import user

class order:
    def __init__(self, order_id, user: 'CUser', Booklist: 'CBookList', borrow_date, return_date, status):
        self.order_id = order_id
        self.user = user            
        self.Booklist = Booklist          
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.status = status
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        days = (self.return_date - self.borrow_date).days
        return sum(book.price * days for book in self.Booklist)
    
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
        return self.user

    def get_booklist(self):
        return self.Booklist

    def get_book_detail(self, book_id):
        for book in self.Booklist:
            if book.book_id == book_id:
                return {
                    "title": book_name,
                    "borrow_date": self.borrow_date,
                    "return_date": self.return_date,
                    "status": self.status,
                    "price": book.price,
                    "total_price": (self.return_date - self.borrow_date).days * book.price
                }
        return None
