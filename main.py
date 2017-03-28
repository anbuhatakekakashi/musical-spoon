'''
SCOREBOARD DESIGN IDEA

    TEAM 1 - 90 pts

SGT Andrews:    20 pts
SPC Bradley:    30 pts
SGT Christian:  40 pts

    TEAM 2 - 110 pts

SGT Davis:      50 pts
SSG Eckland:    50 pts
SSG Forehand:   10 pts

'''

#  This is a dictionary consisting of question numbers as keys, and their associated hashes as values

known_hashes = {1: "AAAAAAAAAAAAAAAAAAAA",
                2: "BBBBBBBBBBBBBBBBBBBB",
                3: "CCCCCCCCCCCCCCCCCCCC"}

class Scoreboard:
    pass

class Player:
    name = ""
    rank = ""
    def add_player(self, playerName, playerRank):
        Player.name = playerName
        Player.rank = playerRank

def hash_checker(question, hash):

    # Check if hash is between 20 and 30 characters

    if (len(hash) < 20):
        raise Exception("String is too small")
    elif (len(hash) > 30):
        raise Exception("String is too large")

    if (known_hashes[question] == hash):
        print("CORRECT!")
        # send success message back to user
        # update scoreboard
    else:
        print("WRONG!")
        # notify user they got the message wrong



def display_menu():
    print("\n")
    print("1.  Add/remove player")
    print("2.  Display teams")
    print("3.  Display scores")
    print("99. Exit")

def display_scoreboard():
    pass

def main():
    valid = True
    while (valid):
        # display_scoreboard()
        display_menu()
        choice = input("Enter option: ")
        if(choice == "1"):
            pass
        elif(choice == "2"):
            pass
        elif(choice == "3"):
            pass
        elif(choice == "99"):
            valid = False
        else:
            print("ERROR:  Please choose a valid option\n")

if __name__ == '__main__':
    main()