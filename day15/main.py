# 菜单
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
stock = {"shui": 10, "kafei": 500, "niunai": 500}

# 库存自检函数

# def dui_bi_shu_ru_ku_cun(yong_hu_pei_liao):
#     for item in yong_hu_pei_liao:
#         if yong_hu_pei_liao[item] >= ku_cun[item]:
#             print(f"咖啡机中{item}不够了。")
#             return False
#     return True


# def jie_shu_an():
#     print("请你投入硬币。")
#     tou_ru_lei_ji = int(input("请你投入1元硬币")) * 1
#     tou_ru_lei_ji += int(input("请你投入5角硬币")) * 0.5
#     tou_ru_lei_ji += int(input("请你投入2角硬币")) * 0.2
#     tou_ru_lei_ji += int(input("请你投入1角硬币")) * 0.1
#     return tou_ru_lei_ji


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
        if dui_bi_shu_ru_ku_cun(make_caffes["formula"]):
            # jie_suan = jie_shu_an()
            # print(jie_shu - zhi_zuo["jiage"] )
            pass