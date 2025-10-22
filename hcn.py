class hcn:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def get_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
    def get_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    def xuat_thong_tin(self):
        print(f"chieu dai hinh chu nhat: {self.chieu_dai}")
        print(f"chieu rong hinh chu nhat: {self.chieu_rong}")
        print(f"chu vi hinh chu nhat: {self.get_chu_vi()}")
        print(f"dien tich hinh chu nhat: {self.get_dien_tich()}")
class Hinhvuong(hcn):
    def __init__(self, canh):
        self.canh = canh
        super().__init__(self.canh, self.canh)
    def xuat(self):
        print(f"canh hinh vuong: {self.canh}")
        print(f"chu vi hinh vuong: {self.get_chu_vi()}")
        print(f"dien tich hinh vuong: {self.get_dien_tich()}")
        
       