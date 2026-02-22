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
def save_data():
        with open ("san_pham","w") as f:
            json.dump(san_pham,f)
def them_sp(msp, ten, thuong_hieu, gia, so_luong):
    """Thêm sản phẩm mới"""
    sp_moi = {
        "id": msp,
        "ten": ten,
        "thuong_hieu": thuong_hieu,
        "gia": gia,
        "so_luong": so_luong
    }
    san_pham.append(sp_moi)
    print(f"Đã thêm: {ten}")

def display_all_product():
    if len(san_pham) == 0:
        print("Kho hàng trống!")
    else:
        for sp in san_pham:
            print(sp)

def tim_theo_id(ma):
    """Tìm sản phẩm theo mã"""
    for sp in san_pham:
        if sp["id"] == ma:
            return sp
    return None

    
