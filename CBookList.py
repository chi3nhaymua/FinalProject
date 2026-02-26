from Models.CBook import *
from Dataset.JsonFactory import *

class BookList:
    def __init__(self):
        self.book_list = []
        self.file = "../Dataset/Books.json"
        self.load_book()

    def load_book (self):
        data = JsonFileFactory.read_data(self.file)
        self.book_list = []

        for item in data:
            book = Book(
                item.get("book_id", ""),
                item.get("book_name", ""),
                item.get("author", ""),
                item.get("type", ""),
                item.get("published_year", 0),
                item.get("price", 0),
                item.get("quantity", 0)
            )
            self.book_list.append(book)

    def get_all_books(self):
        return self.book_list

    def save_book(self):
        JsonFileFactory.write_data(self.file, [book.to_dict() for book in self.book_list])

    def add_book(self, book):
        for b in self.book_list:
             if str(b.book_id) == str(book.book_id): # Tránh 1 =! 001
                return False, "Sách đã tồn tại!"
        self.book_list.append(book)
        self.save_book()  # Lưu lại sau khi thêm
        return True, "Thêm sách thành công!"

    def delete_book(self, book_id):
        for book in self.book_list:
            if str(book.book_id) == str(book_id):
                self.book_list.remove(book)
                self.save_book()
                return True, "Xóa thành công."
        return False, "Không tìm thấy sách để xóa."

    def search_book(self, keyword):
        keyword = keyword.lower().strip()
        results = []
        for book in self.book_list:
            if (keyword in str(book.book_name).lower() or
                keyword in str(book.author).lower() or
                keyword in str(book.book_id).lower() or
                keyword in str(book.book_type).lower()):
                results.append(book)
        return results

    def update_book(self, updated_book):
        for i, b in enumerate(self.book_list):
            if str(b.book_id) == str(updated_book.book_id):
                self.book_list[i] = updated_book
                self.save_book()
                return True, "Cập nhật thành công!"
        return False, "Không tìm thấy ID sách để cập nhật!"

    def show_book(self):
        if not self.book_list:
            return
        else:
            for book in self.book_list:
                book.hienthithongtin()
