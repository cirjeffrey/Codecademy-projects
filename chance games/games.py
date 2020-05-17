import random

money = 100

# Write your game of chance functions here


def check(call, result, bet):
    global money
    if (call == result):
        print("You Won ", bet)
        money += bet
    elif(result == "Equal"):
        return
    else:
        print("You Lose ", bet)
        money -= bet


def coin(call, bet):
    print("COIN")
    result = "Heads" if random.randint(0, 1) == 0 else "Tails"
    print("Coin is", result)
    print("You chose", call)
    check(call, result, bet)


def choHan(call, bet):
    print("CHO HAN")
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    result = "Even" if (d1 + d2) % 2 == 0 else "Odd"
    print("Dice is", result)
    print("You chose", call)
    check(call, result, bet)


def cards(call, bet):
    print("CARDS")
    c1 = random.randint(0, 12)
    c2 = random.randint(0, 12)

    result = "Higher" if c1 > c2 else "Lower"
    result = "Equal" if c1 == c2 else result
    check(call, result, bet)


def roulette(call, bet):
    global money
    print("ROULETTE")
    result = random.randint(0, 37)
    if ((call == "Even" and result % 2 == 0) or (call == "Odd" and result % 2 != 0)):
        print("You win ")
        money = money + (bet * 2)
    elif (call == result):
        print("You Win")
        money = money + (bet * 32)
    else:
        print("You lose")
        print(result)
        money -= bet


# Call your game of chance functions here
roulette(3, 5)
