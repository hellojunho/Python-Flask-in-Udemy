from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like?({options})>> ")

    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        print("bye")
        is_on = False

    # else:
    #     drink = menu.find_drink(choice)
    #     if coffee_maker.is_resource_sufficient(drink):
    #         print(money_machine.make_payment(drink.cost))
    else:
        drink = menu.find_drink(choice)
        # 재료가 충분한가?(변수)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        # 거래가 성공적인가?(변수)
        is_payment_seccessful = money_machine.make_payment(drink.cost)
        # 둘 다 참이면 커피 만들기 진행
        if is_enough_ingredients and is_payment_seccessful:
            coffee_maker.make_coffee(drink)
