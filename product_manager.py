import json
san_pham=[
    {
        "id": "LT01",
        "ten": "Laptop Gaming Acer Nitro 5",
        "thuong_hieu": "Acer",
        "gia": 22990000,
        "so_luong": 15
    },
    {
        "id": "LT02",
        "ten": "Laptop Dell Inspiron 15",
        "thuong_hieu": "Dell",
        "gia": 17990000,
        "so_luong": 8
    }
]
def load_data():
     try:
        with open ("san_pham","r") as f:    
            print (f.read())
     except FileNotFoundError:
        print("Khong tim thay sp")
def save_data():
        with open ("san_pham","w") as f:
            json.dump(san_pham,f)
def add_product(msp, ten, thuong_hieu, gia, so_luong):
    """Thêm sản phẩm mới"""
    sp_moi = {
        "id": msp,
        "ten": ten,
        "thuong_hieu": thuong_hieu,
        "gia": gia,
        "so_luong": so_luong
    }

    with open ("san_pham","a") as f:
        f.write(f"{sp_moi}")

def display_all_product():

    if len(san_pham) == 0:
        print("Kho hàng trống!")
    else:
        for sp in san_pham:
            print(sp)

def search_product_by_name(ma):
   print( """Tìm sản phẩm theo mã""")
   for sp in san_pham:
      if sp["id"] == ma:
            print(sp)
      else:
            return None
def delete_product(ma):
   for sp in san_pham:
      if sp["id"] == ma:
          san_pham.clear()
          print(f"da xoa sp{ma}")
      else:
          print("khong hop le")
def update_product(products):
    ma = input("Nhập mã sp cần sửa: ")
    
    for sp in san_pham:
        if sp["id"] == ma:
            sp["ten"] = input("Ten moi: ")
            sp["thuong_hieu"] = input("Thuong hieu moi: ")
            sp["gia"] = input("Gia moi : ")
            sp["so_luong"] = input("Số lượng mới: ") 
            print("da cap nhat!")
            return
    print("Khong tim thay!")
def fndksn
