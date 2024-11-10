while True:
    ticket_number = input("Введите номер транспортного билета: ")
    if len(ticket_number) == 6:
        break
    else:
        print("Номер транспортного билета должен быть из шести цифр!")

first_half = ticket_number[:3]
second_half = ticket_number[3:]

diff = 0

for digit in first_half:
    diff += int(digit)

for digit in second_half:
    diff -= int(digit)

if diff == 0:
    print("Да, вам повезло")
else:
    print("Нет, может быть в следующий раз")

# Введите номер транспортного билета: 735573
# Да, вам повезло
