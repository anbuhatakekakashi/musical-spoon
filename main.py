
class Player:
    name = ""
    rank = ""

    def add_player(self, playerName, playerRank):
        Player.name = playerName
        Player.rank = playerRank

def display_menu():
    print("1.  Display teams")
    print("2.  Display scores")
    print("99. Exit")

def main():
    valid = True
    while (valid):
        print("\n")
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