#TODO2 处理菜单问题
MENU = {
    "natie": {
        "peiliao": {"shui": 50, "kafei": 18, }, "jiage": 15,
    },
    "kabuqiluo": {
        "peiliao": {"shui": 100, "kafei": 25, "niunai": 100}, "jiage": 25
    },
    "maqiduo": {
        "peiliao": {"shui": 100, "kafei": 30, "niunai": 100}, "jiage": 30
    }
}

ying_ye_shou_ru = 0    #营业款

#是否开机营业
shi_fou_kai_ji = True

#TODO 处理库存问题
#库存资源
ku_cun = {"shui": 1000, "kafei": 300, "niunai": 1000}



while shi_fou_kai_ji:
    yong_hu_shu_ru = input("请你输入你喜欢的咖啡,natie/kabuqiluo/maqiduo:>").lower()
    if yong_hu_shu_ru == "caxun":
       print(f"shui: {ku_cun['shui']}ml")
       print(f"kafei: {ku_cun['kafei']}g")
       print(f"niunai: {ku_cun['niunai']}ml")
       print(f"营业收入: {ying_ye_shou_ru}¥")
    elif yong_hu_shu_ru == "natie":
        pass
    elif yong_hu_shu_ru == "kabuqiluo":
        pass
    elif yong_hu_shu_ru == "maqiduo":
        pass
    else:
        pass