def save_product():
    code = input("ma san pham: ")
    name = input("ten san pham: ")
    price = input("gia: ")
    with open("products.txt", "a", encoding="utf-8") as f:
        f.write(f"{code};{name};{price}\n")
    print("luu thanh cong")
