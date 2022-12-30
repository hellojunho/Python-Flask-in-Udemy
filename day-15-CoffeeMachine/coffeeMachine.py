MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 4500,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 5000,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 5500,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# 동전 계산
def process_coins():
    print("돈을 넣어주세요")
    total = 0
    total += int(input("1000원 몇 개?>> ")) * 1000
    total += int(input("500원 몇 개?>> ")) * 500
    total += int(input("100원 몇 개?>> ")) * 100
    total += int(input("50원 몇 개?>> ")) * 50

    return total



# 재료 충분 여부
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이 모두 소진되었습니다.")
            return False
        return True


# 거래 성공 여부
def is_transcation_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"거스름돈 {change}원 드리겠습니다.")
        global profit
        profit += drink_cost
        return True
    else:
        print("죄송합니다. 충분한 금액이 들어오지 않았습니다.")
        return False


# 커피 만들기
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"주문하신 {drink_name} 드리겠습니다.")


is_on = True
while(is_on):
    choice = input("음료를 선택하세요 (espresso/latte/cappuccino)>> ")

    if choice == "exit":
        print("종료합니다.")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transcation_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

