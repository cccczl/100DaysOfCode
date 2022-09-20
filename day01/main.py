# Band Name Generator
# 乐队名称生成器
print("欢迎使用乐队名称生成器。")

# initialize the variables as empty strings
# 将变量初始化为空字符
city = ""
pet_name = ""

# simple check to make sure the user has entered something
# 简单的检查，确保用户已经输入了内容

while True:
    print("What's the name of the city you grew up in?")
    city = input("> ")
    # if there's no input, ask again
    # 如果没有输入，再问一次
    if city == "":
        print("You haven't entered anything. Please try again.")
    # if there's any input at all, break out of the loop
    # 如果有输入，就跳出循环
    else:
        break

# do the same for the pet name
# 接受乐队名输入检查，和上段代码同样处理
while True:
    print("What's your pet's name?")
    pet_name = input("> ")
    if pet_name == "":
        print("You haven't entered anything. Please try again.")
    else:
        break

# output using f-strings makes the code much more readable
# 使用f-strings的输出使代码可读性更强
print(f"Your band name could be {city} {pet_name}.")
print("Your band name could be {} {}.".format(city,pet_name))
print("Your band name could be "+city, pet_name+". ")
