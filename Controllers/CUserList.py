from CUser import user
from JsonFactory import JsonFileFactory


class UserList:
    def __init__(self):
        self.user_list = []
        self.file = "data/Users.json"
        self.load_user()

    def load_user(self):
        data = JsonFileFactory.read_data(self.file)
        self.user_list = []
        for item in data:
            u = user(
                item["user_id"],
                item["user_loginname"],
                item["user_name"],
                item["user_password"],
                item["user_email"],
                item["user_phone"],
                item["user_address"],
                item["role"],
            )
            self.user_list.append(u)

    def save_user(self):
        JsonFileFactory.write_data(self.file, [u.to_dict() for u in self.user_list])

    def show_user(self):
        if not self.user_list:
            print("Không có người dùng nào")
            return
        for u in self.user_list:
            print(u.to_dict())

    def get_all_users(self):
        return self.user_list

    def find_user(self, user_id, user_name):
        for u in self.user_list:
            if u.user_id == user_id and u.user_name == user_name:
                return u
        return None

    def add_user(self, user):
        self.user_list.append(user)
        self.save_user()

    def delete_user(self, user_id, user_name):
        u = self.find_user(user_id, user_name)
        if u:
            self.user_list.remove(u)
            self.save_user()
            return "Xóa thành công"
        return "Không tìm thấy người dùng"

# if __name__ == "__main__":
#     ul = UserList()
#     user1 = user(
#         user_id=1,
#         user_loginname="chithao01",
#         user_name="Chi Thảo",
#         user_password="123456",
#         user_email="chithao@gmail.com",
#         user_phone="0901234567",
#         user_address="Đà Lạt, Lâm Đồng",
#         role="admin"
#     )
#
#     user2 = user(
#         user_id=2,
#         user_loginname="user02",
#         user_name="Nguyễn Văn A",
#         user_password="password02",
#         user_email="vana@gmail.com",
#         user_phone="0912345678",
#         user_address="TP. Hồ Chí Minh",
#         role="user"
#     )
#
#     ul.add_user(user1)
#     ul.add_user(user2)
#
#     ul.show_user()
#
#     print(ul.delete_user(user1.user_id, user1.user_name))
#     ul.show_user()
