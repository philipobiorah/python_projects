name = input("What is your name? ")

print("Hello, ", name, "Welcome to the adventure game")

should_we_play = input("Do you want to play the game? (yes/no) ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("We gonna play")

elif should_we_play == "YESS":
    print("WE ARE GONNA PLAY")

else:
    print("We are  NOT playing....")