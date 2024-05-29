# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява
# с колко най-малко монети може да стане това.

change = float(input())

remaining_change = change
coins_count = 0

while remaining_change > 0:
    remaining_change = round(remaining_change, 2)
    if remaining_change >= 2:
        coins_count += 1
        remaining_change -= 2
    elif remaining_change >=1:
        coins_count += 1
        remaining_change -= 1
    elif remaining_change >= 0.50:
        coins_count += 1
        remaining_change -= 0.50
    elif remaining_change >= 0.20:
        coins_count += 1
        remaining_change -= 0.20
    elif remaining_change >= 0.10:
        coins_count += 1
        remaining_change -= 0.10
    elif remaining_change >= 0.05:
        coins_count += 1
        remaining_change -= 0.05
    elif remaining_change >= 0.02:
        coins_count += 1
        remaining_change -= 0.02
    elif remaining_change >= 0.01:
        coins_count += 1
        remaining_change -= 0.01
print(coins_count)



