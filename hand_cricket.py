import random

compRuns = random.randint(1, 6)
userRuns = 0
runs = 0
balls = 130
while balls > 120:
    try:
        balls = int(input("How many balls you want to play? "))
        if balls > 120:
            print("You cannot add balls more than 120 because this is a T20 match")
    except Exception as e:
        print("Please enter a valid number and not a text")

while compRuns != userRuns:
    try:
        balls -= 1
        print("Computer's Turn: ")
        compRuns = random.randint(1, 6)
        # print(compRuns)
        userRuns = int(input("Your Turn! Enter the runs you want: "))
        if compRuns == userRuns:
            print("Clean Bold! You are out!")
        elif compRuns != userRuns and userRuns<= 6:
            runs += userRuns
            print(f"You scored {userRuns} runs!")
        if userRuns > 6:
            runs = 0
            print("Clean Bold! You are out!")
            print("It is not allowed to enter runs more than 6. Your runs have made will be 0")
            break
        if userRuns == 6 and userRuns != compRuns:
            print("Fabulous! That was a amazing six!")
        elif userRuns == 4 and userRuns != compRuns:
            print("Wow! What a wonderful four!")
        elif userRuns == 3 and userRuns != compRuns:
            print("You run well between the wickets!")
        if runs >= 50 and runs <= 55:
            print("Congragulations! You have made half century!")
        if balls == 0:
            print("The match is over because balls remaining are 0")
            break
    except Exception as e:
        print("Please enter a valid number and not a text")


print(f"The total runs you made are {runs}")

with open("score.txt", "r") as high:
    h = high.read()
    h = int(h)

if h < runs:
    print("You have broken the hiscore! Good Job!")
    with open("score.txt", "w") as high:
        high.write(str(runs))
else:
    print(f"The hiscore is {h} runs. Do more practise to beat the record.")
