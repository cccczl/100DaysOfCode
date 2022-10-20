# # import che15

# # print(che15.chezuowei)
# # print(che15.cheyanse)

# # import turtle

# # wugui = turtle.Turtle()

# # print(wugui)

# from turtle import Screen, Turtle

# caiwugui = Turtle()
# caiwugui.shape('classic')
# caiwugui.color('#a0c8f0')

# print(caiwugui)

# my_screen = Screen()
# my_screen.canvheight = 480
# my_screen.canvwidth = 360
# print(my_screen.canvwidth,my_screen.canvheight)

# caiwugui.forward(100)
# my_screen.exitonclick()


from prettytable import PrettyTable

pkqtable = PrettyTable()

pkqtable.add_column("设备名",["X12","DG15","OP34"])
pkqtable.add_column("价格表",[1500,1114,6000])
pkqtable.add_row ([ 1158259 ,  600.5 ]) 
pkqtable.align = "l"

print(pkqtable.align)

print(pkqtable)