# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта.
# Той обаче не знае колко парчета могат да си вземат гостите от нея. Вашата задача е да напишете програма,
# която изчислява броя на парчетата, които гостите са взели преди тя да свърши.
# Ще получите размерите на тортата
# (широчина и дължина – цели числа и след това на всеки ред, до получаване на командата "STOP"
# или докато не свърши тортата, броят на парчетата, които гостите вземат от нея. Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# •	"{брой парчета} pieces are left." -  ако стигнете до STOP и не са свършили парчетата торта;
# •	"No more cake left! You need {брой недостигащи парчета} pieces more."


width = int(input())
length = int(input())
PIECE_AREA = 1
cake_area = width * length
pieces_count = cake_area / PIECE_AREA
pieces_taken = 0

while pieces_taken < pieces_count:
    current_pieces_taken = input()
    if current_pieces_taken == "STOP":
        break
    pieces_taken += int(current_pieces_taken)
pieces_diff = int(abs(pieces_count - pieces_taken))
if pieces_taken < pieces_count:
    print(f"{pieces_diff} pieces are left.")
else:
    print(f"No more cake left! You need {pieces_diff} pieces more.")


