from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
handler = MoneyMachine()
menu_obj = Menu()


on = True
intro = ("\nWelcome to the Cyber Cafe!\nWhere coffee is brewed from 1s and 0s!\nWhat would you like? "
         f"({menu_obj.get_items()}): ")
while on:
    selection = input(intro).lower()
    if selection == "report":
        maker.report()
        handler.report()
    elif selection == "off":
        on = False
    else:
        valid_drink = menu_obj.find_drink(selection)
        if valid_drink in menu_obj.menu:
            enough = maker.is_resource_sufficient(valid_drink)
            if enough:
                price = valid_drink.cost
                success = handler.make_payment(price)
                if success:
                    maker.make_coffee(valid_drink)
