# # import another_module
# # print(another_module.another_variable)
#
# from turtle import Turtle, Screen
# # timmy라는 객체 생성
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# 표 정렬 table.align = "l" or "r" or "c" (left, right, center)
table.align = "l"

print(table)
