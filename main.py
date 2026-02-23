import product_manager

def main():
    while True:
        print("=== MENU ===")
        print("1. Xem sản phẩm")
        print("2. Thêm sản phẩm")
        print("3. Tìm sản phẩm")
        print("4. Xoa san pham")
        print("5. Cap nhat san pham")
        print("0. Thoát")
        
        chon = input("Chọn: ")
        
        if chon == "1":
            product_manager.hien_thi_tat_ca()
        elif chon == "2":
            msp = input("Mã: ")
            ten = input("Tên: ")
            thuong_hieu = input("Thương hiệu: ")
            gia = int(input("Giá: "))
            sl = int(input("Số lượng: "))
            product_manager.them_sp(msp, ten, thuong_hieu, gia, sl)
        elif chon == "3":
            ma = input("Nhập mã cần tìm: ")
            ket_qua = product_manager.search_product_by_name(ma)
            if ket_qua :
                print(f"Tìm thấy: {ket_qua}")
            else:
                print("Không tìm thấy")
        elif chon =="4":
            ma = input("Nhập mã cần xoa: ")
            x= product_manager.delete_product(ma)
        elif chon=="5":
            ma = input("Nhập mã cần cap nhat: ")
            x=product_manager.update_product(ma)
        elif chon == "0":
            break
main()