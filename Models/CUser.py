class user:
    def __init__(self,user_id, user_loginname, user_name, user_password, user_email, user_phone, user_address, role):
        self.user_id = user_id
        self.user_loginname = user_loginname
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email
        self.user_phone = user_phone
        self.user_address = user_address
        self.role = role

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "user_loginname": self.user_loginname,
            "user_name": self.user_name,
            "user_password": self.user_password,
            "user_email": self.user_email,
            "user_phone": self.user_phone,
            "user_address": self.user_address,
            "role": self.role
        }
# if __name__ == "__main__":
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
#     print(user1.to_dict())
#     print(user2.to_dict())
