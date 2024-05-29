# На осемнадесетия си рожден ден Хосе взел решение, че ще се изнесе да живее на квартира.
# Опаковал багажа си в кашони и намерил подходяща обява за апартамент под наем.
# Той започва да пренася своя багаж на части, защото не може наведнъж.
# Има ограничено свободно пространство в новото си жилище, където може да разположи вещите,
# така че мястото да бъде подходящо за живеене.
# Напишете програма, която изчислява свободния обем от жилището на Хосе, който остава, след като пренесе багажа си.
# Всеки кашон е с точни размери:  1m x 1m x 1m.


STOP_STRING = "Done"
width = int(input())
length = int(input())
high = int(input())

apartment_area = width * length * high
count_box = 0
while apartment_area > 0:
    delivery_box = input()
    if delivery_box == STOP_STRING:
        print(f"{apartment_area} Cubic meters left.")
        break
    delivery_box = int(delivery_box)
    count_box += delivery_box
    apartment_area -= delivery_box
    if apartment_area <= 0:
        print(f"No more free space! You need {abs(apartment_area)} Cubic meters more.")


