import random

listn = []


def Makenum():
    for n in range(4):
        num12 = random.randrange(0, 9)
        listn.append(num12)
    if len(listn) > len(set(listn)):
        listn.clear()
        Makenum()


def game(numd):
    count = 0

    while True:
        guess = [int(i) for i in str(input("Please guess 4-digit number: "))]
        #        while True:
        #            if len(guess) < len(set(guess)):
        #                guess. clear()
        #                guess = [int(i) for i in str(input("Please guess 4-digit number: "))]

        if guess == listn:
            print("You won.")
            print("It took you " + str(count) + " guess(es).")
            game_on = input("Do you want to play agian?: ")
            if game_on == "yes":
                Makenum()
                game(4)
            else:
                break
            break

        elif count >= 20:
            print("You lost. the number was: " + str(listn))
            game_on = input("Do you want to play agian?: ")
            if game_on == "yes":
                Makenum()
                game(4)
            break

        else:
            cow = 0
            bull = 0
            for x in range(0, numd):
                if guess[x] == listn[x]:
                    bull += 1
                elif guess[x] in listn:
                    cow += 1

        print("Cows: " + str(cow) + " Bulls: " + str(bull))
        count += 1


Makenum()

# print (str(listn))

game(4)