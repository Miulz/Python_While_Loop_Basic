# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.
# Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня
# и когато постигне целта си да се изписва "Goal reached! Good job!"
# и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките,
# които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си,
# на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."

target = 10000
sum_steps = 0
command = "Going home"


while sum_steps < target:
    new_steps = input()
    if new_steps == "Going home":
        sum_steps += int(input())
        break
    sum_steps += int(new_steps)
if sum_steps >= target:
    print("Goal reached! Good job!")
    print(f"{sum_steps - target} steps over the goal!")
else:
    print(f"{(target - sum_steps)} more steps to reach goal.")















