# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере
# дали ще успее да събере необходимата сума. Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.

money_needed_for_vacation = float(input())
Jesica_money = float(input())


count_all_days = 0
count_spend_days = 0


while Jesica_money < money_needed_for_vacation and count_spend_days < 5:
    transaction = input()
    transaction_money = float(input())
    count_all_days += 1
    if transaction == "spend":
        Jesica_money -= transaction_money
        count_spend_days += 1
        if Jesica_money < 0:
            Jesica_money = 0
    elif transaction == "save":
        count_spend_days = 0
        Jesica_money += transaction_money
    if count_spend_days == 5:
        print("You can't save the money.")
        print(count_all_days)
        break
    if Jesica_money >= money_needed_for_vacation:
        print(f"You saved the money for {count_all_days} days.")
        break




