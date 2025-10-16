class SinhVien:
    def __init__(self, ma_sv, ho_ten, diem_mon):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.__diem = diem_mon

    def xuat_thong_tin_sv(self):
        print(f"Mã SV: {self.ma_sv}, Họ Tên: {self.ho_ten}, Điểm TB: {self.__diem}")
    
class SinhVienXLDL:
    def __init__(self, ma_sv, ho_ten, diem_mon,lap_trinh):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.__diem = diem_mon
        self.lap_trinh = lap_trinh

    def xuat_thong_tin_sv(self):
        print(f"Mã SV: {self.ma_sv}, Họ Tên: {self.ho_ten}, Điểm TB: {self.__diem}, Lập trình: {self.lap_trinh}")
SV1 = SinhVienXLDL("PS44508","Tấn Đạt ",10,"Python")
SV1.xuat_thong_tin_sv()