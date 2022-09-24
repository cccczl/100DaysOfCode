
# 问候语生成器
print("欢迎使用问候生成器。")

# 将变量初始化为空字符
chengshi = ""
xing_ming = ""


# 简单的检查，确保chengshi已经输入了内容

while True:
    print("请输入你来自那个城市！")
    chengshi = input("> ")
    # 如果没有输入，再问一次
    if chengshi == "":
        print("你没有输入任何东西. 请检查.")
    # 如果有输入，就跳出循环
    else:
        break

# 简单的检查，确保xing_ming已经输入了内容
while True:
    print("请输入你的名字！")
    xing_ming = input("> ")
    # 如果没有输入，再问一次
    if xing_ming == "":
        print("你没有输入任何东西. 请检查.")
    # 如果有输入，就跳出循环
    else:
        break

# 使用f-strings的输出使代码可读性更强
print(f"欢迎你，来自{chengshi}的{xing_ming}.")

print("欢迎你，来自{}的{}.".format(chengshi,xing_ming))
print("欢迎你，来自"+ chengshi + "的" + xing_ming + ". ")
