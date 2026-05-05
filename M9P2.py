def compute_battingAverage(hits, atbats):
    average = hits / atbats
    return average

start = str(input("This program computes the batting average of the player. Enter (y/n) to start or stop the program. "))
num_players = 0

while start.lower() == "y":
    last = str(input("Enter player's last name: "))
    hits = int(input("Enter the number of hits: "))
    atbats = int(input("Enter the number of at bats: "))

    num_players += 1

    total = compute_battingAverage(hits, atbats)
    print(last, round(total, 3))

    start = str(input("Do you want to enter another player? (y/n): "))

print("Number of players enter: ", num_players)

