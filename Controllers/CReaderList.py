from CReader import reader
from JsonFactory import JsonFileFactory

class CReaderList:
    def __init__(self):
        self.reader_list = []
        self.file = "data/Readers.json"
        self.load_reader()

    def load_reader(self):
        data = JsonFileFactory.read_data(self.file)
        self.reader_list = []
        for item in data:
            r = reader(
                item["r_id"],
                item["r_name"],
                item["r_sex"],
                item["r_dob"],
                item["r_phone"],
                item["r_address"],
            )
            self.reader_list.append(r)
    def save_reader(self):
        JsonFileFactory.write_data(self.file, [r.to_dict() for r in self.reader_list])

    def show_reader(self):
        if not self.reader_list:
            print ("Không có người đọc nào")
            return
        for r in self.reader_list:
            print(r.to_dict())

    def get_all_reader(self):
        return self.reader_list

    def find_reader(self, r_id, r_name):
        for r in self.reader_list:
            if r.r_id == r_id and r.r_name == r_name:
                return r
        return None

    def add_reader(self, reader):
        self.reader_list.append(reader)
        self.save_reader()

    def delete_reader(self, r_id, r_name):
        r = self.find_reader(r_id, r_name)
        if r:
            self.reader_list.remove(r)
            self.save_reader()
            return "Xóa thành công"
        return "Không tìm thấy người dùng"

    def update_reader(self, r_id, r_name, r_sex, r_dob, r_phone, r_address):
        r = self.find_reader(r_id, r_name)
        if r:
            r.r_sex = r_sex
            r.r_dob = r_dob
            r.r_phone = r_phone
            r.r_address = r_address
            self.save_reader()
            return "Cập nhật thành công"
        return "Không tìm thấy người đọc"
