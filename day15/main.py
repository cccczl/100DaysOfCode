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
ku_cun = {"shui": 10, "kafei": 500, "niunai": 500}

def dui_bi_shu_ru_ku_cun(yong_hu_pei_liao):
    for item in yong_hu_pei_liao:
        if yong_hu_pei_liao[item] >= ku_cun[item]:
            print(f"咖啡机中{item}不够了。")
            return False
    return True


def jie_shu_an():
    print("请你投入硬币。")
    tou_ru_lei_ji = int(input("请你投入1元硬币")) * 1
    tou_ru_lei_ji += int(input("请你投入5角硬币")) * 0.5
    tou_ru_lei_ji += int(input("请你投入2角硬币")) * 0.2
    tou_ru_lei_ji += int(input("请你投入1角硬币")) * 0.1
    return tou_ru_lei_ji


while shi_fou_kai_ji:
    yong_hu_shu_ru = input("请你输入你喜欢的咖啡,natie/kabuqiluo/maqiduo:>").lower()
    if yong_hu_shu_ru == "caxun":
       print(f"shui: {ku_cun['shui']}ml")
       print(f"kafei: {ku_cun['kafei']}g")
       print(f"niunai: {ku_cun['niunai']}ml")
       print(f"营业收入: {ying_ye_shou_ru}¥")
    else:
        zhi_zuo = MENU[yong_hu_shu_ru]
        print(zhi_zuo)
        if dui_bi_shu_ru_ku_cun(zhi_zuo["peiliao"]):
            # jie_suan = jie_shu_an()
            # print(jie_shu - zhi_zuo["jiage"] )        