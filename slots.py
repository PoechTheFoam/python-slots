import time
import random
possibilities=['👽','💀','💔','😭','🥹']
balance=1000
def spin():
    global balance
    while True:
        bet = input('Place a bet!: $')
        if not bet.isdigit():
            print('Please enter a number.')
            continue
        bet=float(bet)
        if bet <=0:
            print('Bets must be greater than 0')
            continue
        elif bet > balance:
            print('Bets cannot be more than your balance.')
            continue
        balance-=bet
        print(f'Current Balance: ${balance:.2f}')
        print('Spinning',end='')
        for dot in range (3):
            time.sleep(.5)
            print('.',end='')
        return bet
def display():
    got=[random.choice(possibilities) for _ in range (3)]
    for possibility in got:
        time.sleep(1)
        print(possibility,end='')
    return got
def payout(got, bet):
    global balance
    if got.count('👽')==3:
        print('You won!! Bet x10!!')
        balance += bet * 10
    elif ((got[0]==got[1]) and (got[0]=='👽' or got[1]=='👽')) or ((got[1]==got[2]) and (got[1]=='👽'or got[2]=='👽')):
        print('You won!! Bet x3!!')
        balance+=bet*3
    elif got.count('🥹') == 3:
        print('You won!! Bet x7!!')
        balance+=bet*7
    elif (((got[0] == got[1]) and (got[0] == '🥹' or got[1] == '🥹'))
          or ((got[1] == got[2]) and (got[1] == '🥹' or got[2] == '🥹'))):
        print('You won!! Bet x2.5!!')
        balance += bet * 2.5
    elif got.count('😭') == 3:
        print('You won!! Bet x5!!')
        balance+=bet*5
    elif (((got[0] == got[1]) and (got[0] == '😭' or got[1] == '😭'))
              or ((got[1] == got[2]) and (got[1] == '😭' or got[2] == '😭'))):
        print('You won!! Bet x2!!')
        balance += bet * 2
    elif got.count('💔') == 3:
        print('You won!! Bet x2!!')
        balance+=bet*2
    elif (((got[0] == got[1]) and (got[0] == '💔' or got[1] == '💔'))
              or ((got[1] == got[2]) and (got[1] == '💔' or got[2] == '💔'))):
        print('You won!! Bet x1.5!!')
        balance += bet * 1.5
    elif got.count('💀') == 3:
        print('You got CURSED!! Balance x0.5!!')
        balance*=0.5
    elif (((got[0] == got[1]) and (got[0] == '💀' or got[1] == '💀'))
              or ((got[1] == got[2]) and (got[1] == '💀' or got[2] == '💀'))):
        print('You got light CURSED!! Balance x0.75!!')
        balance += bet * 0.75
    else:
        print('You didn\'t win anything!')
    got.clear()
while True:
    if balance<=0:
        print('You lost!! Sorry!')
        break
    print('Welcome to New Slots')
    print(f'Your balance is ${balance:,.2f}')
    bet=spin()
    print()
    got=display()
    print()
    payout(got,bet)
    while True:
        choice=input('Would you like to continue? (y/n)').lower()
        if choice=='y':
            print('Good luck!')
            break
        elif choice =='n':
            print('99.9% of gamblers quit before making it big')
            exit()
        else:
            print('Invalid choice')
            continue
