class reader:
    def __init__(self, r_id, r_name, r_sex, r_dob, r_phone, r_address):
        self.r_id = r_id
        self.r_name = r_name
        self.r_sex = r_sex
        self.r_dob = r_dob
        self.r_phone = r_phone
        self.r_address = r_address

    def to_dict(self):
        return {
            "r_id": self.r_id,
            "r_name": self.r_name,
            "r_sex": self.r_sex,
            "r_dob": self.r_dob,
            "r_phone": self.r_phone,
            "r_address": self.r_address
        }

# if __name__ == "__main__":
#     r1 = reader(
#         r_id="R001",
#         r_name="Nguyễn Văn A",
#         r_sex="Nam",
#         r_dob="2002-05-18",
#         r_phone="0912345678",
#         r_address="Đà Lạt, Lâm Đồng"
#     )
#
#     print(r1.to_dict())
