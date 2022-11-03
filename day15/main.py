# 菜单
from hashlib import new


MENU = {
    "latte": {
        "formula": {"water": 50, "coffee": 18, }, "price": 15,
    },
    "cappuccino": {
        "formula": {"water": 100, "coffee": 25, "milk": 100}, "price": 25
    },
    "macchiatto": {
        "formula": {"water": 100, "coffee": 30, "milk": 100}, "price": 30
    }
}


# 营业收入
purse = 0

# #是否开机营业
is_open = True

# 库存资源
stock = {"water": 1000, "coffee": 500, "milk": 500}

# 自检函数

def make_coffees_test(formulas):
    for item in formulas:
        if formulas[item] >= stock[item]:
            print(f"咖啡机中{item}不够了。")
            return False
    return True

# 投币系统
def coin():
    print("请你投入硬币。")
    coin_pay = int(input("请你投入1元硬币")) * 1
    coin_pay += int(input("请你投入5角硬币")) * 0.5
    return coin_pay


while is_open:
    user_input = input("请你输入你喜欢的咖啡,latte/cappuccino/macchiatto:>").lower()
    if user_input == "inquire":
        print(f"shui: {stock['water']}ml")
        print(f"kafei: {stock['coffee']}g")
        print(f"niunai: {stock['milk']}ml")
        print(f"营业收入: {purse}¥")
    else:
        make_coffees = MENU[user_input]
        print(make_coffees)
        if make_coffees_test(make_coffees["formula"]):
            # coin()
            newcoin = coin()
            if newcoin < make_coffees["price"]:            
                print("你的钱不够")
            elif newcoin == make_coffees["price"]:
                print("咖啡制作中")
            else:
                print("找零中完成，咖啡制作中")