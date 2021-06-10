import random

game = True
past_winners = []
winner = 0
bank = int(input("How much money are you starting with? "))

while game != False:
    play = input("do you want to play or leave ")
    if play == "l":
        game = False
    else:
        winner = random.randint(0, 1)
        past_winners.append(winner)
        bet = int(input("What number do you think it will be? "))
        bet_amount = int(input("How much money are you betting? "))
        if bet == winner:
            bank = +bet_amount
        else:
            bank = -bet_amount
        bank_rep_str = "\nYou have " + str(bank) + " left"
        winner_rep_str = "\nThe winning number is " + str(winner)
        past_winners_rep_str = "\nThe past winning numbers are " + str(
            past_winners)
        print(winner_rep_str)
        print(past_winners_rep_str)
        print(bank_rep_str)
