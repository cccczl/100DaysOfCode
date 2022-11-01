# 菜单
from hashlib import new


MENU = {
    "natie": {
        "formula": {"shui": 50, "kafei": 18, }, "jiage": 15,
    },
    "kabuqiluo": {
        "formula": {"shui": 100, "kafei": 25, "niunai": 100}, "jiage": 25
    },
    "maqiduo": {
        "formula": {"shui": 100, "kafei": 30, "niunai": 100}, "jiage": 30
    }
}


# 营业收入
purse = 0

# #是否开机营业
is_open = True

# 库存资源
stock = {"shui": 1000, "kafei": 500, "niunai": 500}

# 自检函数

def make_caffes_test(formulas):
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
    user_inprt = input("请你输入你喜欢的咖啡,natie/kabuqiluo/maqiduo:>").lower()
    if user_inprt == "caxun":
        print(f"shui: {stock['shui']}ml")
        print(f"kafei: {stock['kafei']}g")
        print(f"niunai: {stock['niunai']}ml")
        print(f"营业收入: {purse}¥")
    else:
        make_caffes = MENU[user_inprt]
        print(make_caffes)
        if make_caffes_test(make_caffes["formula"]):
            # coin()
            newcoin = coin()
            if newcoin < make_caffes["jiage"]:            
                print("你的钱不够")
            elif newcoin == make_caffes["jiage"]:
                print("咖啡制作中")
            else:
                print("找零中完成，咖啡制作中")