from common.insertdanhmuc import insert_danhmuc
while True:
    ten=input("Nhập vào tên danh mục: ")
    mota=input("Nhập vào ô mô tả: ")
    insert_danhmuc(ten,mota)
    con=input("Tiếp Tục y, Thoát thì nhấn ký tự bất kỳ")
    if con!='y':
        break
