#Welcome to stock portfolio tracker
stocks = {"APPLE":180,
          "TESLA":250,
          "SAMSUNG":200,
          "GOOGLE":300,
          "MICROSOFT":400}
def available_stocks ():
    print("🪙 Available stocks 🪙")
    print()
    for stock,value in stocks.items():
        print(f"   {stock:<9} : ₹{value}")
    print()
    print("🪙  "*6)

def get_stock_name():
     while True:
         stock_name = input("🔹 Enter stock name 📈 :"
                            " ").upper()
         if stock_name not in stocks:
             print("⚠️ Invalid !")
         else:
             break
     return stock_name

def get_stock_qty():
    while True:
        try:
            stock_qty = int(input("▫️ Enter stock qty : "))
            if stock_qty <= 0:
                print("⚠️ Qty must be greater than 0 !")
            else:
                break
        except ValueError:
            print("⚠️ INVALID !")
    return stock_qty

def get_stock_price(stock_name):
    print(f"🔹 Price per stock : ₹{stocks[stock_name]}")

def get_total(stock_name,stock_qty):
    total = stocks[stock_name] * stock_qty
    print(f"▫️ Total : ₹{total}")
    return total

def add_stock():
    while True:
        add=input("🔺 Add stock (y/n) : ")
        if add not in ["y","n"]:
            print("⚠️ Invalid !")
        else:
            break
    return add

def get_final_total(price_list):
    final_total = 0
    for price in price_list:
        final_total += price
    print(f"▫️ Total investment value : ₹{final_total}")
    return final_total

def main():
    print("📈 Welcome to stock portfolio tracker 📈")
    print()
    available_stocks()
    print()
    price_list = []
    selected_stock_details =[]

    while True:
        stock_name = get_stock_name()
        stock_qty = get_stock_qty()

        selected_stock_details.append(f"{stock_name:<10}  -  {stock_qty}")

        get_stock_price(stock_name)
        total = get_total(stock_name,stock_qty)
        price_list.append(total)

        print()
        add = add_stock()
        print()
        if add == "y":
            pass
        else:
            break

    total_investment=get_final_total(price_list)
    file_path="Stock_Portfolio_Tracker.txt"

    with open(file=file_path,mode="w") as file:
        file.write("Stock Name  - Stock Quantity\n")
        for stock_detail in selected_stock_details:
            file.write(f"{stock_detail}\n")
        file.write(f"Total Investment Value : Rs {total_investment}")
        print(f"'{file_path}' was created")

main()